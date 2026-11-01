"""Short-term memory: the conversation the model sees on every call.

The API is stateless, so the whole conversation is sent every time, and it
grows with every turn. When it gets too big, the oldest turns are replaced
by a running summary, and only the most recent turns are kept word for word.
"""
import json
import math
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

Message = dict[str, Any]


def estimate_tokens(data: Any) -> int:
    """Rough estimate (about 4 characters per token). Real counts differ."""
    text = data if isinstance(data, str) else json.dumps(data)
    return max(1, math.ceil(len(text) / 4))


def is_turn_start(message: Message) -> bool:
    """A new turn starts with the user's own words, not with tool results."""
    return message["role"] == "user" and isinstance(message["content"], str)


def transcript(messages: list[Message]) -> str:
    """Messages as plain text lines, for the summarizer to read."""
    lines = []
    for m in messages:
        if isinstance(m["content"], str):
            lines.append(f"{m['role'].capitalize()}: {m['content']}")
            continue
        for block in m["content"]:
            if block.get("type") == "text":
                lines.append(f"Companion: {block['text']}")
            elif block.get("type") == "tool_use":
                args = json.dumps(block["input"])
                lines.append(f"(used {block['name']}: {args})")
    return "\n".join(lines)


@dataclass
class Conversation:
    summary: str = ""
    messages: list[Message] = field(default_factory=list)

    def tokens(self) -> int:
        return estimate_tokens(self.messages) + estimate_tokens(self.summary)

    def turns(self) -> list[int]:
        """The index where each turn starts."""
        return [i for i, m in enumerate(self.messages) if is_turn_start(m)]

    def window(self, keep_turns: int) -> list[Message]:
        """Only the last `keep_turns` turns (a sliding window)."""
        starts = self.turns()
        if len(starts) <= keep_turns:
            return list(self.messages)
        return self.messages[starts[-keep_turns]:]

    def compact(self, summarize: Callable[[str, list[Message]], str],
                keep_turns: int, limit: int) -> int:
        """Above `limit` tokens: fold all but the last turns into the summary.

        Cuts only where a turn starts, so a tool_use and its tool_result are
        never separated. Returns how many messages were folded in (0 = none).
        """
        if self.tokens() <= limit:
            return 0
        starts = self.turns()
        if len(starts) <= keep_turns:
            return 0
        cut = starts[-keep_turns]
        old = self.messages[:cut]
        self.summary = summarize(self.summary, old)   # if this fails, keep all
        self.messages = self.messages[cut:]
        return len(old)
