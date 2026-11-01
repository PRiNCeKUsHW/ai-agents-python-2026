# Persistent AI Study Companion

Module 6 project of **AI Agents with Python: Beginner to Production (2026)**.

A study companion that **remembers you**: your name, your goals, what you find hard, across days and
restarts. It keeps each conversation small, stores everything in SQLite, keeps every user's data apart,
and lets you see, forget, purge or delete everything it knows.

- **Short-term memory** (`companion/conversation.py`): the messages of the current session. Above a
  token limit, older turns are folded into a **running summary** by one extra model call; the last
  `COMP_KEEP_TURNS` turns stay word for word. Cuts happen only where a turn starts, so a `tool_use`
  and its `tool_result` are never separated, and old turns are dropped only after the summary arrived.
- **Long-term memory** (`companion/memory.py`): short facts with a topic (profile, goal, struggle,
  progress, preference). The model manages them with three tools (`companion/tools.py`):
  `remember_fact`, `recall_facts`, `forget_fact`. Inputs are validated with Pydantic, and passwords,
  API keys and card numbers are **refused in code**. The relevant facts (the profile first) go into
  the system prompt of every request.
- **SQLite** (`companion/db.py`): tables `facts`, `sessions` (with the summary) and `messages`. Every
  row has a `user_id` and every query filters by it; values are always `?` parameters; each turn is
  saved in one transaction; deleting a session cascades to its messages; `PRAGMA user_version` is the
  schema version.
- **Privacy**: `memory` shows everything stored, `forget N` deletes one fact, `purge --days N` deletes
  old sessions (retention), `delete-me` deletes all of one user's data.
- **Sessions**: one conversation per session id (default: today's date), resumed from the database.

## Offline mode (no key needed)

Without `ANTHROPIC_API_KEY`, the companion uses `companion/fake_api.py`, a local stand-in that speaks
the Messages API protocol, so the real SDK, agent, tools and database run unchanged. **It is not a
model.** Like a model, it only knows what is in the request (system prompt and messages), which makes
memory visible: drop the history and it can't know your name. It follows a script: "my name is ...",
"I'm learning ...", "I find ... hard", "I prefer ...", "I finished ...", "remember that ..." become
`remember_fact` calls; "what do you remember about me" becomes `recall_facts`; "forget ..." becomes
`recall_facts` then `forget_fact`; "what's my name", "quiz me" and "what did we talk about" are answered
from the request. Answers start with `(offline demo)`, summaries with `(offline summary)` (an extract of
what the learner said, not a written summary). `COMP_FAKE_FAIL=401` (or 429, 500) simulates API errors.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."   # optional; omit for offline mode
```

## Usage

```bash
python -m companion ask "My name is Anuj and I find recursion hard" --session mon
python -m companion ask "What's my name?" --session tue     # new session, same facts
python -m companion chat                                     # chat until "bye" (piped input works)
python -m companion memory                                   # everything remembered about you
python -m companion forget 2                                 # delete one fact
python -m companion sessions                                 # your conversations
python -m companion history mon                              # one conversation, with its summary
python -m companion purge --days 30                          # delete sessions unused for 30 days
python -m companion delete-me                                # delete ALL your data (asks first)
python -m companion --user riya ask "What's my name?"        # another user: separate memory
```

| Setting | Default | Meaning |
|---|---|---|
| `ANTHROPIC_API_KEY` | (none) | real Claude calls; without it, offline mode |
| `COMP_MODEL` | `claude-opus-5-5` | model id |
| `COMP_HOME` | `.companion` | folder with `companion.db` |
| `COMP_USER` | `me` | default user (or `--user`) |
| `COMP_KEEP_TURNS` | `4` | recent turns kept word for word |
| `COMP_SUMMARIZE_AT` | `1500` | estimated tokens that trigger a summary |
| `COMP_BUDGET_USD` | `0.50` | stop before spending more per run |
| `COMP_MAX_STEPS` | `6` | tool turns per message |
| `COMP_MAX_RETRIES` | `2` | SDK retries for 429/5xx |
| `COMP_TODAY` | today | fixed date (tests, demos) |

In a real app, the user id comes from your login system, never from the model or the message.

## Tests

```bash
python -m pytest -q        # 41 tests: memory, db, conversation, tools, agent, CLI
mypy --strict companion
```

The tests run the real agent, tools and SQLite against the fake API, each with a temporary database.
They never use a key, the network or your data.

## Layout

```
companion/
  cli.py           commands: ask, chat, memory, forget, sessions, history, purge, delete-me
  agent.py         one turn: system prompt with facts + summary, the tool loop, compaction, saving
  conversation.py  short-term memory: turns, window, running summary
  memory.py        long-term facts: remember, recall, forget, for_prompt; refuses secrets
  tools.py         the three memory tools: Pydantic inputs, strict schemas, run_tool
  db.py            SQLite schema, sessions, retention (purge), deletion (delete_user)
  client.py        real client, or the same SDK pointed at the fake
  fake_api.py      offline scripted stand-in (not a model)
  config.py        settings from environment variables
  pricing.py       cost per call and a budget
tests/             41 tests
```
