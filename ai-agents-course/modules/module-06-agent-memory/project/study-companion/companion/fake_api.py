"""An offline stand-in for the Anthropic Messages API.

It speaks the same HTTP protocol as the real API, so the real `anthropic`
SDK and the agent run unchanged. Instead of a model it follows a fixed
script, and, like a real model, it only knows what is IN the request: the
system prompt (summary and remembered facts) and the messages. That makes it
good for showing memory: drop the history and it can't know your name.

The script: "my name is ...", "I'm learning ...", "I find ... hard",
"I prefer ...", "I finished ...", "remember that ..." become remember_fact
calls (several in one turn); "what do you remember about me" becomes
recall_facts; "forget ..." becomes recall_facts, then forget_fact. Answers
are placeholders marked "(offline demo)". Summaries are extracts marked
"(offline summary)". None of it is model output.
"""
import json
import math
import os
import re
from typing import Any

import httpx2

DEMO_MARK = "(offline demo)"
SUMMARY_MARK = "(offline summary)"
SUMMARY_SYSTEM = "You keep a short running summary"      # see agent.SUMMARIZE
ERROR_TYPES = {400: "invalid_request_error", 401: "authentication_error",
               429: "rate_limit_error", 500: "api_error"}
CLAUSE = r"([^.,;!?]+?)"
REMEMBER: list[tuple[re.Pattern[str], str, str]] = [
    (re.compile(r"\bmy name is (\w+)", re.I), "The learner's name is {}",
     "profile"),
    (re.compile(rf"\bi(?:'m| am) learning {CLAUSE}(?=[.,;!?]|$| and )", re.I),
     "The learner is learning {}", "goal"),
    (re.compile(rf"\bi (?:find|struggle with) {CLAUSE} "
                r"(?:hard|difficult|confusing)", re.I),
     "The learner finds {} hard", "struggle"),
    (re.compile(rf"\bi prefer {CLAUSE}(?=[.,;!?]|$)", re.I),
     "The learner prefers {}", "preference"),
    (re.compile(rf"\bi finished {CLAUSE}(?=[.,;!?]|$| and )", re.I),
     "The learner finished {}", "progress"),
    (re.compile(r"\bremember (?:that )?([^.;!?]+)", re.I), "{}", "progress"),
]
QUESTIONS = {
    "recursion": "What two parts does every recursive function need?",
    "decorator": "What does a decorator receive, and what does it return?",
    "loop": "What is the difference between a for loop and a while loop?",
    "dict": "How do you read a key from a dict without a KeyError?",
    "class": "What is self in a method?",
    "async": "What does await do while a task waits?",
}


def estimate_tokens(text: str) -> int:
    return max(1, math.ceil(len(text) / 4))


def facts_in(system: str) -> list[str]:
    """The remembered facts the agent put into the system prompt."""
    return [line[2:] for line in system.splitlines() if line.startswith("- #")]


def outcome(result: str) -> str:
    """A tool result in a few words: 'saved #1', 'found #1, #2', 'refused'."""
    if result.startswith("Error: "):
        return result.removeprefix("Error: ").split(":")[0]
    verb = result.split()[0]
    if verb not in ("saved", "forgot"):
        verb = "found"
    ids = ", ".join(re.findall(r"#\d+", result))
    return f"{verb} {ids}" if ids else result


def plan(request: str) -> list[tuple[str, dict[str, Any]]]:
    """The first tool calls the script makes for a request (may be none)."""
    text = request.strip()
    if re.search(r"\bforget\b", text, re.I):
        m = re.search(r"\bforget (?:that )?(?:i )?([^.;!?]+)", text, re.I)
        return [("recall_facts", {"query": m.group(1) if m else text})]
    if re.search(r"what do you (?:remember|know) about me", text, re.I):
        return [("recall_facts", {"query": "learner"})]
    calls = []
    for pattern, template, topic in REMEMBER:
        for m in pattern.finditer(text):
            value = m.group(1).strip()
            value = value[0].upper() + value[1:] if template == "{}" else value
            calls.append(("remember_fact", {"text": template.format(value),
                                            "topic": topic}))
        if calls and template == "{}":
            break
    return calls


class FakeAnthropicAPI:
    """Callable handler for httpx2.MockTransport."""

    def __init__(self, failures: list[str] | None = None) -> None:
        env = os.environ.get("COMP_FAKE_FAIL", "")    # e.g. "429,401"
        self.failures = failures if failures is not None else [
            f for f in env.split(",") if f]
        self.requests: list[dict[str, Any]] = []
        self.calls = 0

    def __call__(self, request: httpx2.Request) -> httpx2.Response:
        body = json.loads(request.content or b"{}")
        self.requests.append(body)
        tokens = estimate_tokens(json.dumps(body.get("messages", []))
                                 + json.dumps(body.get("system", "")))
        if self.failures:
            failure = self.failures.pop(0)
            if failure.isdigit():
                return self._error(int(failure))
        system = body.get("system", "")
        if system.startswith(SUMMARY_SYSTEM):
            content = [{"type": "text", "text": self._summary(body)}]
            return self._message(body, content, "end_turn", tokens)
        content, stop = self._turn(body, system)
        return self._message(body, content, stop, tokens)

    # ------------------------------------------------------------ summaries
    @staticmethod
    def _summary(body: dict[str, Any]) -> str:
        """An extract, not a summary: the old summary + each user line, cut."""
        text = body["messages"][-1]["content"]
        previous = re.search(r"Summary so far:\n(.*?)\n\n", text, re.S)
        kept = []
        if previous and previous.group(1).strip() != "(none)":
            kept.append(previous.group(1).strip().removeprefix(SUMMARY_MARK)
                        .strip())
        for line in text.splitlines():
            if line.startswith("User: "):
                said = line[6:]
                kept.append(said if len(said) <= 70 else said[:67] + "...")
        return f"{SUMMARY_MARK} The learner said: " + " | ".join(kept)

    # ------------------------------------------------------------ the script
    def _turn(self, body: dict[str, Any], system: str
              ) -> tuple[list[dict[str, Any]], str]:
        messages = body["messages"]
        start = max(i for i, m in enumerate(messages)
                    if m["role"] == "user" and isinstance(m["content"], str))
        request = messages[start]["content"]
        results = [b for m in messages[start + 1:] if m["role"] == "user"
                   for b in m["content"] if b.get("type") == "tool_result"]
        if body.get("tools"):
            if not results:
                calls = plan(request)
                if calls:
                    return [self._tool_use(n, a) for n, a in calls], "tool_use"
            elif re.search(r"\bforget\b", request, re.I) and len(results) == 1:
                found = re.match(r"#(\d+) ", str(results[0]["content"]))
                if found:
                    return [self._tool_use("forget_fact",
                                           {"fact_id": int(found.group(1))})
                            ], "tool_use"
        text = self._answer(request, system, messages[:start], results)
        return [{"type": "text", "text": f"{DEMO_MARK} {text}"}], "end_turn"

    @staticmethod
    def _answer(request: str, system: str, history: list[dict[str, Any]],
                results: list[dict[str, Any]]) -> str:
        context = system + "\n" + json.dumps(history)
        facts = facts_in(system)
        if results:
            return ("A real model would reply in its own words. Memory: "
                    + "; ".join(outcome(str(r["content"])) for r in results))
        if re.search(r"what(?:'s| is) my name", request, re.I):
            m = re.search(r"name is (\w+)", context)
            return (f"Your name is {m.group(1)}." if m else
                    "I don't know your name: nothing in this request says it.")
        if re.search(r"quiz me", request, re.I):
            hard = [f for f in facts if "[struggle]" in f]
            for key, question in QUESTIONS.items():
                if hard and key in hard[0].lower():
                    return f"You find {key} hard, so: {question}"
            return "A real model would pick a question from your goals here."
        if re.search(r"what did we|where were we", request, re.I):
            m = re.search(r"Summary of earlier conversation:\n(.+)", system)
            said = [msg["content"] for msg in history if msg["role"] == "user"
                    and isinstance(msg["content"], str)]
            parts = ([m.group(1)] if m else []) + [f"you said: {s}" for s in said]
            return ("I can see: " + " | ".join(parts) if parts else
                    "This is the start of our conversation: I see nothing earlier.")
        turns = sum(1 for m in history if m["role"] == "user"
                    and isinstance(m["content"], str))
        summary = "yes" if "Summary of earlier conversation" in system else "no"
        return (f"A real model would answer here. I can see {turns} earlier "
                f"turns, summary: {summary}, remembered facts: {len(facts)}.")

    def _tool_use(self, name: str, args: dict[str, Any]) -> dict[str, Any]:
        self.calls += 1
        return {"type": "tool_use", "id": f"toolu_offline_{self.calls:02d}",
                "name": name, "input": args}

    # ------------------------------------------------------------ responses
    @staticmethod
    def _message(body: dict[str, Any], content: list[dict[str, Any]],
                 stop: str, input_tokens: int) -> httpx2.Response:
        out = estimate_tokens(json.dumps(content))
        return httpx2.Response(200, headers={"request-id": "req_offline"}, json={
            "id": "msg_offline", "type": "message", "role": "assistant",
            "model": body["model"], "content": content, "stop_reason": stop,
            "stop_sequence": None,
            "usage": {"input_tokens": input_tokens, "output_tokens": out},
        })

    @staticmethod
    def _error(status: int) -> httpx2.Response:
        kind = ERROR_TYPES.get(status, "api_error")
        return httpx2.Response(status, headers={"retry-after": "0"}, json={
            "type": "error", "error": {"type": kind,
                                       "message": f"offline demo {kind}"}})
