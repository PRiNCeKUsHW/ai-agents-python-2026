# Module 6: Agent Memory and Conversation State

Part II, Build Agents from Scratch · **AI Agents with Python: Beginner to Production (2026)**

A model API is stateless: it remembers nothing between calls. This module teaches every kind of agent
memory: conversation history, short-term windows, running summaries and long-term facts. Then it
covers storing memory safely in SQLite, with user isolation, retention and deletion, and how this
compares with PostgreSQL. It ends with a complete, tested project: a study companion that remembers you
across days.

> **About the demos:** no API key was used while recording. Model turns on screen come from the
> project's offline fake API (`project/study-companion/companion/fake_api.py`), a fixed script that is
> **not a model**. Like a model, it only knows what is in the request, which makes memory visible. Its
> replies are labelled `(offline demo)` and its summaries `(offline summary)`. The memory, tools,
> conversation handling and SQLite code are real. With `ANTHROPIC_API_KEY` set, the same code calls
> Claude (default model `claude-opus-5-5`).

## Learning objectives

- Explain why model APIs are stateless, and keep a conversation by resending its history
- Measure conversation growth in tokens, and know what the context window is
- Keep the last turns with a sliding window, cutting only where a turn starts
- Fold old turns into a running summary, safely (summary first, then drop)
- Save, recall and forget long-term facts through tools, and put relevant facts in the system prompt
- Refuse secrets in code; let users see and delete what's stored
- Use SQLite: tables, parameterised queries, transactions, schema versions, user isolation, retention
  and deletion; know when to move to PostgreSQL

## Prerequisites

Module 5 (or equivalent). Python 3.11+. An Anthropic API key is optional. New terms are in the course
[glossary](../../GLOSSARY.md).

## Video chapters

| # | Part | Script | Runnable code |
|---|---|---|---|
| 1 | Why Agents Forget: Stateless APIs and Conversation History | `scripts/lesson-01.yaml` | `source/lesson-01/` |
| 2 | Short-Term Memory: Context Windows and Sliding Windows | `scripts/lesson-02.yaml` | `source/lesson-02/`, project |
| 3 | Summary Memory: Compressing a Long Conversation | `scripts/lesson-03.yaml` | `source/lesson-03/`, project |
| 4 | Long-Term Memory: Facts That Outlive a Conversation | `scripts/lesson-04.yaml` | `source/lesson-04/`, project |
| 5 | Saving Memory in SQLite: Sessions, Users, Retention and Deletion | `scripts/lesson-05.yaml` | `source/lesson-05/`, project |
| 6 | Project, Part 1: The Persistent AI Study Companion | `scripts/lesson-06.yaml` | `project/study-companion/` |
| 7 | Project, Part 2: One Turn, a Two-Day Demo, Privacy, Tests and Wrap-up | `scripts/lesson-07.yaml` | `project/study-companion/` |

Plan: [lesson-plan.md](lesson-plan.md). Every lesson follows the course teaching style
([TEACHING_STYLE.md](../../TEACHING_STYLE.md)): an analogy, code on the left with its real output on
the right, dry runs and comparisons, a pause-and-try, an interview corner and a quick check.

## Project: Persistent AI Study Companion

[`project/study-companion/`](project/study-companion/README.md): long-term facts saved with three
memory tools (secrets refused in code), relevant facts in every system prompt, sessions that resume
from SQLite, a running summary above a token limit, user isolation, retention (`purge`) and deletion
(`delete-me`). 41 pytest tests, mypy `--strict` clean.

## Deliverables

| What | Where |
|---|---|
| Full module video (1920×1080, 60 fps, H.264 + AAC) | `renders/module-06-full.mp4` (not committed) |
| Narration scripts / audio | `scripts/*.yaml` / `audio/` (audio not committed) |
| Captions | `captions/module-06-full.srt` (and per part: `captions/lesson-NN.srt`) |
| Quiz, practice answers, challenge | [quiz.md](quiz.md) |
| Question bank: every question from the videos, answers hidden | [QUESTIONS.md](QUESTIONS.md) |
| Thumbnail | `assets/thumbnail-module-06.png` |
| YouTube packaging | [youtube.md](youtube.md) |
| Validation report | [validation-report.md](validation-report.md) |

## Versions used

Python 3.13 · anthropic 2.3.0 · pydantic 2.14.1 · pytest 9.2.0 · mypy 2.4.1 · SQLite (Python's
`sqlite3`) · Remotion 4.0.538 · Kokoro v1.0 (English voice `am_michael`, speed 0.92) · light "Paper"
theme.

Sound effects: recorded effects (Pixabay Content License) from Claude's media-use skill, set up with
`python tools/sfx.py setup`; credits in [`shared/sfx/CREDITS.md`](../../shared/sfx/CREDITS.md). The
tool can also add CC0/CC BY effects from Openverse, or files you downloaded (for example from Earshot).
