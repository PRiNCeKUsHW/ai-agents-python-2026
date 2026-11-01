"""Fold old turns into a summary, keep recent turns word for word."""
import project  # noqa: F401
from companion.agent import SUMMARIZE
from companion.client import make_client
from companion.config import load_settings
from companion.conversation import Conversation, transcript

client = make_client(load_settings(force_offline=True))
MODEL = "claude-opus-5-5"
conv = Conversation()
for text in ["My name is Anuj", "Explain lists", "Explain dicts",
             "Explain loops", "Explain classes"]:
    conv.messages.append({"role": "user", "content": text})
    conv.messages.append({"role": "assistant",
                          "content": "A long explanation. " * 25})


def summarize(previous: str, old: list[dict]) -> str:
    prompt = (f"Summary so far:\n{previous or '(none)'}\n\n"
              f"New messages:\n{transcript(old)}\n\nWrite the updated summary.")
    reply = client.messages.create(model=MODEL, max_tokens=1000, system=SUMMARIZE,
                                   messages=[{"role": "user", "content": prompt}])
    return reply.content[0].text


before = conv.tokens()
folded = conv.compact(summarize, keep_turns=2, limit=300)
print(f"folded {folded} messages: ~{before} -> ~{conv.tokens()} tokens")
print("summary:", conv.summary)

question = {"role": "user", "content": "What's my name?"}
reply = client.messages.create(
    model=MODEL, max_tokens=500, messages=conv.messages + [question],
    system=f"Summary of earlier conversation:\n{conv.summary}")
print(reply.content[0].text)
