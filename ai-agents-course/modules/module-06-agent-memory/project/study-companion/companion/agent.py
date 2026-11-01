from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any

import anthropic
from anthropic.types import Message

from companion.config import Settings
from companion.conversation import Conversation, transcript
from companion.db import Database
from companion.errors import AgentError, ToolError
from companion.memory import LongTermMemory, describe
from companion.pricing import CostTracker
from companion.tools import definitions, run_tool

SYSTEM = (
    "You are a friendly, patient study companion for someone learning Python "
    "and AI agents. You remember the learner between conversations through "
    "long-term memory, because a conversation alone is forgotten. When they "
    "share something lasting (their name, goals, what they find hard, what "
    "they finished, how they like to learn), save it with remember_fact, one "
    "fact per call. Use what you remember to personalise explanations and "
    "quizzes. Never save passwords, keys or other secrets. Today is {today}.")
SUMMARIZE = (
    "You keep a short running summary of a tutoring conversation. Merge the "
    "summary so far with the new messages. Keep facts about the learner, "
    "topics covered, open questions and promises made. At most 120 words.")


@dataclass
class Step:
    """One memory tool call, and what it returned."""

    tool: str
    input: dict[str, Any]
    output: str
    is_error: bool = False


@dataclass
class Reply:
    answer: str
    stop: str              # answered, max_steps, refused, cut_off, budget
    steps: list[Step] = field(default_factory=list)
    folded: int = 0        # old messages folded into the summary this turn
    tokens: int = 0        # estimated size of the conversation afterwards
    cost_usd: float = 0.0

    @property
    def ok(self) -> bool:
        return self.stop == "answered"


@contextmanager
def friendly_errors() -> Iterator[None]:
    """Turn SDK exceptions into one clear AgentError each."""
    try:
        yield
    except anthropic.AuthenticationError:
        raise AgentError("the API key was rejected: check "
                         "ANTHROPIC_API_KEY") from None
    except anthropic.RateLimitError:
        raise AgentError("rate limited, even after retries: wait and try "
                         "again") from None
    except anthropic.APIConnectionError:
        raise AgentError("could not reach the API: check your "
                         "connection") from None
    except anthropic.APIStatusError as exc:
        raise AgentError(f"the API failed with status "
                         f"{exc.status_code}") from None


class StudyCompanion:
    """One user's companion, inside one session (one conversation)."""

    def __init__(self, client: anthropic.Anthropic, settings: Settings,
                 tracker: CostTracker, db: Database, user: str,
                 session: str) -> None:
        self.client = client
        self.settings = settings
        self.tracker = tracker
        self.db = db
        self.user = user
        self.session = session
        self.memory = LongTermMemory(db, user, settings.today)
        summary, messages = db.load_session(user, session)      # resume
        self.conv = Conversation(summary, messages)

    def system_prompt(self, request: str) -> str:
        facts = self.memory.for_prompt(request)
        known = "\n".join(f"- {describe(f)}" for f in facts) or "(nothing yet)"
        prompt = SYSTEM.format(today=self.settings.today.isoformat())
        prompt += f"\n\nWhat you remember about the learner:\n{known}"
        if self.conv.summary:
            prompt += f"\n\nSummary of earlier conversation:\n{self.conv.summary}"
        return prompt

    def create(self, **kwargs: Any) -> Message:
        self.tracker.check()
        with friendly_errors():
            response: Message = self.client.messages.create(
                model=self.settings.model, max_tokens=8000, **kwargs)
        self.tracker.add(self.settings.model, response.usage.input_tokens,
                         response.usage.output_tokens)
        return response

    def summarize(self, previous: str, old: list[dict[str, Any]]) -> str:
        """One extra model call: old summary + old messages -> new summary."""
        prompt = (f"Summary so far:\n{previous or '(none)'}\n\n"
                  f"New messages:\n{transcript(old)}\n\n"
                  "Write the updated summary.")
        response = self.create(system=SUMMARIZE, messages=[
            {"role": "user", "content": prompt}])
        return "".join(b.text for b in response.content if b.type == "text")

    def act(self, name: str, raw: dict[str, Any]) -> Step:
        try:
            return Step(name, raw, run_tool(self.memory, name, raw))
        except ToolError as exc:
            return Step(name, raw, f"Error: {exc}", is_error=True)

    def chat(self, text: str,
             on_step: Callable[[Step], None] | None = None) -> Reply:
        """One turn: answer, using and updating memory, then save it all."""
        before = len(self.conv.messages)
        try:
            reply = self._turn(text, on_step)
            if not reply.ok:                    # never save half a turn
                del self.conv.messages[before:]
                return reply
            reply.folded = self.conv.compact(self.summarize,
                                             self.settings.keep_turns,
                                             self.settings.summarize_at)
        except AgentError:
            del self.conv.messages[before:]
            raise
        self.db.save_session(self.user, self.session, self.conv.summary,
                             self.conv.messages, self.settings.today)
        reply.tokens = self.conv.tokens()
        reply.cost_usd = self.tracker.spent_usd
        return reply

    def _turn(self, text: str, on_step: Callable[[Step], None] | None) -> Reply:
        messages = self.conv.messages
        messages.append({"role": "user", "content": text})
        system = self.system_prompt(text)
        steps: list[Step] = []
        for _ in range(self.settings.max_steps):
            response = self.create(system=system, tools=definitions(),
                                   messages=messages)
            messages.append({"role": "assistant", "content": [
                b.model_dump(mode="json", exclude_none=True)
                for b in response.content]})
            if response.stop_reason == "refusal":
                return Reply("", "refused", steps)
            if response.stop_reason == "max_tokens":
                return Reply("", "cut_off", steps)
            calls = [b for b in response.content if b.type == "tool_use"]
            if not calls:
                answer = "".join(b.text for b in response.content
                                 if b.type == "text")
                return Reply(answer, "answered", steps)
            results: list[dict[str, Any]] = []
            for call in calls:
                step = self.act(call.name, call.input)
                steps.append(step)
                if on_step:
                    on_step(step)
                results.append({"type": "tool_result", "tool_use_id": call.id,
                                "content": step.output,
                                "is_error": step.is_error})
            messages.append({"role": "user", "content": results})
        return Reply("", "max_steps", steps)
