"""Long-term memory: facts that outlive a conversation."""
from datetime import date
from pathlib import Path

import project  # noqa: F401
from companion.db import Database
from companion.errors import ToolError
from companion.memory import LongTermMemory, describe

db = Database(Path(":memory:"))              # a throwaway database
memory = LongTermMemory(db, user="anuj", today=date(2026, 11, 2))

print(describe(memory.remember("The learner's name is Anuj", "profile")))
print(describe(memory.remember("The learner finds recursion hard", "struggle")))
print(describe(memory.remember("The learner prefers short examples",
                               "preference")))

hits = memory.recall("can you help with recursion?")
print("recall:", [describe(f) for f in hits])

try:
    memory.remember("My password is hunter2", "profile")
except ToolError as exc:
    print("tool error:", exc)

print("forgot", describe(memory.forget(3)))
print("for the system prompt:")
for fact in memory.for_prompt("quiz me"):
    print("-", describe(fact))
