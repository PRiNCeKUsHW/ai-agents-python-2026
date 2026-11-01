"""Every turn makes the next request bigger. A window keeps the last few."""
import project  # noqa: F401
from companion.client import make_client
from companion.config import load_settings
from companion.conversation import Conversation, estimate_tokens

client = make_client(load_settings(force_offline=True))
conv = Conversation()
for i, text in enumerate(["My name is Anuj", "Explain lists", "Explain dicts",
                          "Explain loops", "Explain classes"], start=1):
    conv.messages.append({"role": "user", "content": text})
    conv.messages.append({"role": "assistant",
                          "content": "A long explanation. " * 25})
    print(f"turn {i}: {len(conv.messages):>2} messages, "
          f"~{conv.tokens():>4} tokens")

recent = conv.window(keep_turns=2)           # only the last 2 turns
print(f"window: {len(recent)} messages, ~{estimate_tokens(recent)} tokens")
print("oldest kept:", recent[0]["content"])

question = {"role": "user", "content": "What's my name?"}
reply = client.messages.create(model="claude-opus-5-5", max_tokens=500,
                               messages=recent + [question])
print(reply.content[0].text)
