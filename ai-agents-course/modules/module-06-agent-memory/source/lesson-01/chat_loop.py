"""A chat loop: the history list IS the conversation's memory."""
import sys

import project  # noqa: F401
from companion.client import make_client
from companion.config import load_settings

client = make_client(load_settings(force_offline=True))
history: list[dict] = []                     # grows by 2 every turn

for line in sys.stdin:                       # one message per line
    text = line.strip()
    print(f"you> {text}")
    history.append({"role": "user", "content": text})
    reply = client.messages.create(model="claude-opus-5-5",
                                   max_tokens=500, messages=history)
    answer = reply.content[0].text
    history.append({"role": "assistant", "content": answer})
    print(f"bot> {answer}")
    print(f"     [{len(history)} messages sent next time, "
          f"{reply.usage.input_tokens} input tokens this time]")
