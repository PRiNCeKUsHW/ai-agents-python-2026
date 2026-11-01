"""Three calls. The API keeps nothing between them: you send the history."""
import project  # noqa: F401  (lets us import the companion package)
from companion.client import make_client
from companion.config import load_settings

client = make_client(load_settings(force_offline=True))
MODEL = "claude-opus-5-5"


def ask(messages: list[dict]) -> str:
    reply = client.messages.create(model=MODEL, max_tokens=500,
                                   messages=messages)
    return reply.content[0].text


# call 1: introduce yourself
print("1:", ask([{"role": "user", "content": "Hi, my name is Anuj."}]))

# call 2: a NEW request that doesn't include call 1
print("2:", ask([{"role": "user", "content": "What's my name?"}]))

# call 3: send the earlier messages again, then the question
history = [
    {"role": "user", "content": "Hi, my name is Anuj."},
    {"role": "assistant", "content": "Nice to meet you, Anuj!"},
    {"role": "user", "content": "What's my name?"},
]
print("3:", ask(history))
