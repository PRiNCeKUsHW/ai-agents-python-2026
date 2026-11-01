"""Memory tools: the model decides what to remember, recall and forget.

Your code still decides what is allowed: inputs are validated with Pydantic,
and LongTermMemory refuses secrets. Any problem becomes a ToolError, which
goes back to the model as an observation instead of a crash.
"""
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Literal

from anthropic.types import ToolParam
from pydantic import BaseModel, Field, ValidationError

from companion.errors import ToolError
from companion.memory import LongTermMemory, describe

Topic = Literal["profile", "goal", "struggle", "progress", "preference"]


class RememberFact(BaseModel):
    text: str = Field(min_length=3, max_length=200,
                      description="One short fact, e.g. 'The learner's name "
                                  "is Anuj'")
    topic: Topic = Field(description="profile: who they are; goal: what they "
                                     "want to learn; struggle: what is hard; "
                                     "progress: what they finished; "
                                     "preference: how they like to learn")


class RecallFacts(BaseModel):
    query: str = Field(min_length=1, description="Words to look for")


class ForgetFact(BaseModel):
    fact_id: int = Field(ge=1, description="The fact's number, from "
                                           "recall_facts")


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    params: type[BaseModel]
    func: Callable[[LongTermMemory, Any], str]


def remember_fact(memory: LongTermMemory, p: RememberFact) -> str:
    return f"saved {describe(memory.remember(p.text, p.topic))}"


def recall_facts(memory: LongTermMemory, p: RecallFacts) -> str:
    facts = memory.recall(p.query)
    return "\n".join(describe(f) for f in facts) if facts else "no matching facts"


def forget_fact(memory: LongTermMemory, p: ForgetFact) -> str:
    return f"forgot {describe(memory.forget(p.fact_id))}"


TOOLS = {t.name: t for t in [
    Tool("remember_fact",
         "Saves one lasting fact about the learner to long-term memory, so "
         "you still know it in future conversations. Use it when the learner "
         "shares their name, goals, what they find hard, what they finished, "
         "or how they like to learn. Save facts, not whole messages. Never "
         "save passwords, keys or other secrets.",
         RememberFact, remember_fact),
    Tool("recall_facts",
         "Searches long-term memory and returns matching facts with their "
         "numbers. Use it when the learner asks what you remember, or before "
         "forget_fact to find a fact's number.",
         RecallFacts, recall_facts),
    Tool("forget_fact",
         "Deletes one fact from long-term memory by its number. Use it when "
         "the learner asks you to forget something.",
         ForgetFact, forget_fact),
]}

UNSUPPORTED = ("title", "default", "minLength", "maxLength", "minimum", "maximum")


def _clean(node: Any) -> Any:
    """Strip keywords strict tool schemas don't accept; Pydantic still checks."""
    if isinstance(node, dict):
        out = {k: ({name: _clean(sub) for name, sub in v.items()}
                   if k == "properties" else _clean(v))
               for k, v in node.items() if k not in UNSUPPORTED}
        if out.get("type") == "object":
            out["additionalProperties"] = False
            out["required"] = list(out.get("properties", {}))
        return out
    if isinstance(node, list):
        return [_clean(v) for v in node]
    return node


def definitions() -> list[ToolParam]:
    return [{"name": t.name, "description": t.description,
             "input_schema": _clean(t.params.model_json_schema()),
             "strict": True} for t in TOOLS.values()]


def run_tool(memory: LongTermMemory, name: str, raw: dict[str, Any]) -> str:
    if name not in TOOLS:
        raise ToolError(f"unknown tool {name!r}")
    t = TOOLS[name]
    try:
        params = t.params.model_validate(raw)
    except ValidationError as exc:
        problems = "; ".join(
            f"{'.'.join(str(p) for p in e['loc']) or 'input'}: {e['msg']}"
            for e in exc.errors(include_url=False))
        raise ToolError(f"invalid input for {name}: {problems}") from None
    return t.func(memory, params)
