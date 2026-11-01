# Module 6 YouTube packaging

Thumbnail: `assets/thumbnail-module-06.png` (1280×720). Captions: `captions/lesson-NN.srt`, `captions/module-06-full.srt`.

Source-code links point at `https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course`; adjust the branch if the course is not merged into `main`.

## Full module video (`renders/module-06-full.mp4`)

**Title**

AI Agents with Python 2026 · Module 6: Agent Memory and Conversation State (Full Module + Project)

**Description**

```text
Module 6 of "AI Agents with Python: Beginner to Production (2026)": Agent Memory and Conversation State.

Project: Persistent AI Study Companion, a study companion that remembers you across days: long-term facts saved with memory tools (secrets refused in code), a running summary for long chats, sessions in SQLite with user isolation, retention and delete-my-data, and 41 tests.

Prerequisites: Module 5 (Tool Calling), or equivalent. An Anthropic API key is optional: every demo also runs offline with a built-in scripted fake API (not a model). You need Python 3.11+ and a code editor.

Every lesson explains the concept, shows real code with real output, covers common errors, and ends with a quick check. The module closes with a recap, a 5-question quiz and an extension challenge.

Source code + README: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

Chapters
00:00 L1 Why Agents Forget: Stateless APIs and Conversation History
00:47 What is stateless?
01:39 Proving it
02:39 How conversation history works
03:14 A chat loop
04:08 Four kinds of memory
05:12 Pause and try
05:50 Interview corner
06:51 Quick check
07:13 Recap
07:46 L2 Short-Term Memory: Context Windows and Sliding Windows
08:24 The context window
09:23 Measuring growth
10:16 Windows by turns or by tokens
10:48 Cutting safely
12:10 Pause and try
12:42 Interview corner
13:44 Quick check
14:04 Recap
14:38 L3 Summary Memory: Compressing a Long Conversation
15:14 What is summary memory?
16:02 How it works
16:36 Summary in code
18:33 Window or summary?
19:05 Pause and try
19:44 Interview corner
20:45 Quick check
21:04 Recap
21:33 L4 Long-Term Memory: Facts That Outlive a Conversation
22:09 What is long-term memory?
22:58 Facts in code
24:04 Memory as tools
24:58 Facts in the system prompt
25:24 Three layers together
25:45 Privacy rules
26:19 Pause and try
27:00 Interview corner
28:01 Quick check
28:20 Recap
28:53 L5 Saving Memory in SQLite: Sessions, Users, Retention and Deletion
29:32 What is SQLite?
30:33 SQLite in code
31:57 SQL injection
32:36 The project's schema
33:48 Retention and deletion
34:15 SQLite or PostgreSQL?
34:50 Pause and try
35:35 Interview corner
36:39 Quick check
37:01 Recap
37:34 L6 Project, Part 1: The Persistent AI Study Companion
37:55 The brief
38:34 Architecture
39:12 Settings
39:44 An honest fake
40:20 The command line
40:51 First conversation
41:47 Pause and try
42:24 Interview corner
43:26 Quick check
43:46 Recap
44:21 L7 Project, Part 2: One Turn, a Two-Day Demo, Privacy, Tests and Wrap-up
44:44 The system prompt
45:12 One turn, line by line
46:24 Two-day demo
47:10 Privacy on purpose
48:00 Testing
48:47 Troubleshooting
49:21 Interview corner
50:34 Module recap
51:08 Module quiz
52:42 Practice
53:27 Extension challenge
53:57 Documentation
54:18 Next up

Official docs: platform.claude.com/docs/en/build-with-claude/context-windows · platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool · docs.python.org/3/library/sqlite3.html

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

**Search terms**: ai agent memory, llm conversation history, claude api memory, context window tokens, conversation summary memory, long term memory ai agent, sqlite python tutorial, sql injection python, chatbot memory python, study companion ai

## Individual lesson videos (`renders/lesson-NN.mp4`)

### Lesson 1 (07:46)

**Title:** Why Agents Forget: Stateless APIs and Conversation History | AI Agents with Python, Module 6 Lesson 1

```text
Lesson 1 of Module 6 (Agent Memory and Conversation State) in "AI Agents with Python: Beginner to Production (2026)".

Source code: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

00:00 Introduction
00:47 What is stateless?
01:39 Proving it
02:39 How conversation history works
03:14 A chat loop
04:08 Four kinds of memory
05:12 Pause and try
05:50 Interview corner
06:51 Quick check
07:13 Recap

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

### Lesson 2 (06:51)

**Title:** Short-Term Memory: Context Windows and Sliding Windows | AI Agents with Python, Module 6 Lesson 2

```text
Lesson 2 of Module 6 (Agent Memory and Conversation State) in "AI Agents with Python: Beginner to Production (2026)".

Source code: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

00:00 Introduction
00:37 The context window
01:36 Measuring growth
02:29 Windows by turns or by tokens
03:01 Cutting safely
04:23 Pause and try
04:55 Interview corner
05:58 Quick check
06:18 Recap

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

### Lesson 3 (06:55)

**Title:** Summary Memory: Compressing a Long Conversation | AI Agents with Python, Module 6 Lesson 3

```text
Lesson 3 of Module 6 (Agent Memory and Conversation State) in "AI Agents with Python: Beginner to Production (2026)".

Source code: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

00:00 Introduction
00:36 What is summary memory?
01:24 How it works
01:58 Summary in code
03:55 Window or summary?
04:27 Pause and try
05:06 Interview corner
06:07 Quick check
06:25 Recap

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

### Lesson 4 (07:19)

**Title:** Long-Term Memory: Facts That Outlive a Conversation | AI Agents with Python, Module 6 Lesson 4

```text
Lesson 4 of Module 6 (Agent Memory and Conversation State) in "AI Agents with Python: Beginner to Production (2026)".

Source code: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

00:00 Introduction
00:35 What is long-term memory?
01:25 Facts in code
02:30 Memory as tools
03:24 Facts in the system prompt
03:50 Three layers together
04:11 Privacy rules
04:46 Pause and try
05:26 Interview corner
06:27 Quick check
06:46 Recap

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

### Lesson 5 (08:41)

**Title:** Saving Memory in SQLite: Sessions, Users, Retention and Deletion | AI Agents with Python, Module 6 Lesson 5

```text
Lesson 5 of Module 6 (Agent Memory and Conversation State) in "AI Agents with Python: Beginner to Production (2026)".

Source code: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

00:00 Introduction
00:39 What is SQLite?
01:39 SQLite in code
03:03 SQL injection
03:43 The project's schema
04:55 Retention and deletion
05:21 SQLite or PostgreSQL?
05:56 Pause and try
06:41 Interview corner
07:46 Quick check
08:07 Recap

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

### Lesson 6 (06:46)

**Title:** Project, Part 1: The Persistent AI Study Companion | AI Agents with Python, Module 6 Lesson 6

```text
Lesson 6 of Module 6 (Agent Memory and Conversation State) in "AI Agents with Python: Beginner to Production (2026)".

Source code: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

00:00 Introduction
00:21 The brief
00:59 Architecture
01:37 Settings
02:09 An honest fake
02:46 The command line
03:17 First conversation
04:13 Pause and try
04:49 Interview corner
05:51 Quick check
06:11 Recap

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

### Lesson 7 (10:18)

**Title:** Project, Part 2: One Turn, a Two-Day Demo, Privacy, Tests and Wrap-up | AI Agents with Python, Module 6 Lesson 7

```text
Lesson 7 of Module 6 (Agent Memory and Conversation State) in "AI Agents with Python: Beginner to Production (2026)".

Source code: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory

00:00 Introduction
00:23 The system prompt
00:50 One turn, line by line
02:03 Two-day demo
02:48 Privacy on purpose
03:39 Testing
04:26 Troubleshooting
05:00 Interview corner
06:12 Module recap
06:47 Module quiz
08:21 Practice
09:05 Extension challenge
09:36 Documentation
09:57 Next up

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

## Uploaded in two parts

### Part 1: Lessons 1–4 (28:53)

**Title:** AI Agents with Python 2026 · Module 6 (Part 1/2): Chat History, Context Windows, Summaries, Memory

```text
Module 6 of "AI Agents with Python: Beginner to Production (2026)": Agent Memory and Conversation State. Part 1 of 2 (Lessons 1–4).

In this part: why model APIs forget (stateless), conversation history and a chat loop, tokens and the context window, sliding windows that keep tool calls valid, running summaries, and long-term facts saved with memory tools and recalled into the system prompt.

Part 2 (SQLite, user isolation, retention, deletion + the Persistent AI Study Companion project): https://youtu.be/XXXX

Every lesson explains the concept, shows real code on the left with its real output on the right, covers common errors, and ends with a quick check, an interview corner and pause-and-try questions.

Prerequisites: Module 5 (Tool Calling), or equivalent. An Anthropic API key is optional: every demo also runs offline with a built-in scripted fake API (not a model). You need Python 3.11+ and a code editor.

Source code + README: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory
Question bank (every question from the videos, with answers): https://github.com/PRiNCeKUsHW/ai-agents-python-2026/blob/main/ai-agents-course/modules/module-06-agent-memory/QUESTIONS.md

Chapters
00:00 L1 Why Agents Forget: Stateless APIs and Conversation History
00:47 What is stateless?
01:39 Proving it
02:39 How conversation history works
03:14 A chat loop
04:08 Four kinds of memory
05:12 Pause and try
05:50 Interview corner
06:51 Quick check
07:13 Recap
07:46 L2 Short-Term Memory: Context Windows and Sliding Windows
08:24 The context window
09:23 Measuring growth
10:16 Windows by turns or by tokens
10:48 Cutting safely
12:10 Pause and try
12:42 Interview corner
13:44 Quick check
14:04 Recap
14:38 L3 Summary Memory: Compressing a Long Conversation
15:14 What is summary memory?
16:02 How it works
16:36 Summary in code
18:33 Window or summary?
19:05 Pause and try
19:44 Interview corner
20:45 Quick check
21:04 Recap
21:33 L4 Long-Term Memory: Facts That Outlive a Conversation
22:09 What is long-term memory?
22:58 Facts in code
24:04 Memory as tools
24:58 Facts in the system prompt
25:24 Three layers together
25:45 Privacy rules
26:19 Pause and try
27:00 Interview corner
28:01 Quick check
28:20 Recap

Official docs: platform.claude.com/docs/en/build-with-claude/context-windows · platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool · docs.python.org/3/library/sqlite3.html

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

**Tags:** ai agent memory, llm conversation history, stateless api, context window tokens, sliding window chat history, conversation summary memory, long term memory ai, memory tools claude, claude api python, chatbot memory python

### Part 2: Lessons 5–7 (25:46)

**Title:** AI Agents with Python 2026 · Module 6 (Part 2/2): SQLite Memory + AI Study Companion Project

```text
Module 6 of "AI Agents with Python: Beginner to Production (2026)": Agent Memory and Conversation State. Part 2 of 2 (Lessons 5–7).

In this part: SQLite from scratch (tables, parameterised queries, SQL injection, transactions, schema versions), one user's data kept apart, retention and delete-my-data, and when to use PostgreSQL. Then the project: Persistent AI Study Companion, a study companion that remembers you across days: long-term facts saved with memory tools (secrets refused in code), a running summary for long chats, sessions in SQLite with user isolation, retention and delete-my-data, and 41 tests. Ends with the module quiz and an extension challenge.

Part 1 (stateless APIs, context windows, summaries and long-term memory): https://youtu.be/XXXX

Every lesson explains the concept, shows real code on the left with its real output on the right, covers common errors, and ends with a quick check, an interview corner and pause-and-try questions.

Prerequisites: Module 5 (Tool Calling), or equivalent. An Anthropic API key is optional: every demo also runs offline with a built-in scripted fake API (not a model). You need Python 3.11+ and a code editor.

Source code + README: https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course/modules/module-06-agent-memory
Question bank (every question from the videos, with answers): https://github.com/PRiNCeKUsHW/ai-agents-python-2026/blob/main/ai-agents-course/modules/module-06-agent-memory/QUESTIONS.md

Chapters
00:00 L5 Saving Memory in SQLite: Sessions, Users, Retention and Deletion
00:39 What is SQLite?
01:39 SQLite in code
03:03 SQL injection
03:43 The project's schema
04:55 Retention and deletion
05:21 SQLite or PostgreSQL?
05:56 Pause and try
06:41 Interview corner
07:46 Quick check
08:07 Recap
08:41 L6 Project, Part 1: The Persistent AI Study Companion
09:02 The brief
09:40 Architecture
10:18 Settings
10:50 An honest fake
11:27 The command line
11:58 First conversation
12:54 Pause and try
13:30 Interview corner
14:32 Quick check
14:53 Recap
15:27 L7 Project, Part 2: One Turn, a Two-Day Demo, Privacy, Tests and Wrap-up
15:50 The system prompt
16:18 One turn, line by line
17:31 Two-day demo
18:16 Privacy on purpose
19:06 Testing
19:53 Troubleshooting
20:28 Interview corner
21:40 Module recap
22:14 Module quiz
23:49 Practice
24:33 Extension challenge
25:04 Documentation
25:25 Next up

Official docs: platform.claude.com/docs/en/build-with-claude/context-windows · platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool · docs.python.org/3/library/sqlite3.html

#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite
```

**Tags:** sqlite python tutorial, sql injection python, sqlite transactions, ai agent memory database, user data privacy ai, postgresql vs sqlite, persistent chatbot python, ai study companion, claude api project, python sqlite3
