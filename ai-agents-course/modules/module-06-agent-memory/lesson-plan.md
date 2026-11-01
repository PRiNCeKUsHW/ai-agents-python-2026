# Module 6 lesson plan

| # | Lesson | Ideas | Analogy | Demo (real output) |
|---|---|---|---|---|
| 1 | Why agents forget | stateless API; history = the messages you resend; chat loop; four kinds of memory | a tutor with no memory of yesterday, and your notebook | `stateless.py`, `chat_loop.py` |
| 2 | Short-term memory | tokens, context window, growth per turn; sliding window by turns or tokens; cut at turn starts | a fixed-size whiteboard | `window.py`; dry run of a window over a tool call |
| 3 | Summary memory | running summary; summarize above a limit; summary first, then drop; what to keep | minutes of a meeting | `summary.py` |
| 4 | Long-term memory | facts by topic; remember/recall/forget tools; relevant facts in the system prompt; privacy rules | a tutor's index cards | `memory_demo.py` |
| 5 | SQLite | tables, `?` parameters, injection, transactions, `user_version`; schema; retention and deletion; SQLite vs PostgreSQL | a filing cabinet with strict drawers | `sqlite_demo.py` |
| 6 | Project 1 | brief, architecture, settings, the honest fake, sessions, first conversation | — | `ask`, `memory`, `chat` |
| 7 | Project 2 | system prompt, `chat()` and `_turn()`, two-day demo, privacy on purpose, tests, wrap-up | — | next-day demo, `history`, `purge`, `delete-me`, pytest (41), mypy |

Pacing: beginner pacing (voice 0.92, longer pauses). Each lesson: objectives, analogy, What → Why → How
→ Where, code on the left with real output on the right, a dry run or comparison, a pause-and-try, an
interview corner, a quick check and a recap. Lesson 7 adds the module recap, the 5-question quiz,
practice questions, the extension challenge and the docs.

Sound: from this module on the mix uses recorded sound effects (`shared/sfx/`, see
`tools/sfx.py`), with keyboard sounds under every typed command.

Lesson 7's terminal demo continues the data created in lesson 6: build lesson 6 before lesson 7.
