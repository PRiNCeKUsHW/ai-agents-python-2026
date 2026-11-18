"""Write modules/<module>/youtube.md: titles, descriptions, chapter timestamps and search terms.

Timestamps come from the built lesson timelines (identical to the rendered videos, which
`tools/module.py validate` checks to within half a second).

usage: python tools/youtube.py 1
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/PRiNCeKUsHW/ai-agents-python-2026/tree/main/ai-agents-course"

MODULES = {
    0: {
        "title": "Your Developer Setup",
        "language": "hinglish",
        "project": "Your First GitHub Repository",
        "project_dir": "my-first-repo",
        "project_blurb": "a first repository with a setup checker that confirms Python 3.11+, an active "
                         "virtual environment, pinned packages, a complete .env, a .gitignore that keeps "
                         ".env and .venv out of git, and a git repository, with 26 pytest tests.",
        "prereq": "None: this is where the course starts. Install Python 3.11+ and Git (on Windows, Git for "
                  "Windows includes Git Bash).",
        "style": "Explained in Hinglish (Hindi + English) with Hinglish captions. Every command is run for real "
                 "on screen, with real-life analogies, comparison tables, an interview corner and practice "
                 "questions (answers in quiz.md).",
        "closing": "Every lesson ends with quick-check questions and a recap. Lesson 3 adds the project wrap-up "
                   "and an extension challenge.",
        "terms": ["terminal for beginners", "command line basics hindi", "python virtual environment",
                  "venv pip requirements.txt", "python dotenv env file", "git and github for beginners",
                  "git tutorial hindi", "git commit push pull", "gitignore env", "first github repository"],
        "tags": "#Git #GitHub #Python #Terminal #AIAgents",
        "docs": "docs.python.org/3/library/venv.html · pip.pypa.io · git-scm.com/book · docs.github.com",
        "parts": [
            {"lessons": [1, 2],
             "title": "Terminal, venv, pip and .env",
             "blurb": "the terminal from zero (folders, paths, files, running Python, exit codes, PATH and "
                      "the two most common errors), then virtual environments, pip, requirements.txt, "
                      "environment variables and a .env file, and the project's setup checker (5 of 6).",
             "tags": ["terminal for beginners", "command line basics", "bash commands", "python venv",
                      "pip install requirements", "python dotenv", "env file python", "environment variables",
                      "hinglish coding tutorial", "python setup"]},
            {"lessons": [3],
             "title": "Git and GitHub + Your First Repository",
             "blurb": "Git from zero: commits, the staging area, .gitignore, diff, restore, branches and "
                      "merge; then remotes the way GitHub works (push, clone, pull), what to do if a secret "
                      "is pushed, and the project: {project_blurb}",
             "tags": ["git tutorial", "github for beginners", "git commit push pull", "git branch merge",
                      "gitignore", "git restore", "github repository", "git hindi", "first github project",
                      "version control"]},
        ],
    },
    1: {
        "title": "Python for AI Engineering",
        "language": "hinglish",  # remade in Hinglish 2026-11-18 (the English first version is in git history)
        "project": "Python AI Toolkit",
        "project_dir": "python-ai-toolkit",
        "project_blurb": "a command-line tool that validates a JSON log of LLM API calls and reports "
                         "requests, success rate, tokens, estimated cost, latency and top tags, as "
                         "Markdown or JSON, with concurrent downloads and 42 pytest tests.",
        "prereq": "No AI experience needed. Any programming experience helps, but every Python concept is explained.",
        "terms": ["python for ai", "python tutorial for beginners", "ai engineering", "ai agents python",
                  "python dataclasses", "python json", "httpx", "python async await", "pytest tutorial",
                  "python cli project", "python hindi", "python for ai hindi"],
        "tags": "#Python #AIAgents #AIEngineering #PythonTutorial #LLM",
        "docs": "docs.python.org/3/tutorial · www.python-httpx.org · docs.pytest.org",
        "style": "Explained in Hinglish (Hindi + English) with Hinglish captions. Real-life analogies, code next "
                 "to its real output, comparison tables, an interview corner and practice questions in every "
                 "lesson (answers in quiz.md).",
        "closing": "Every lesson ends with quick-check questions and a recap. Lesson 7 adds the module quiz, an "
                   "extension challenge and the documentation links.",
        "parts": [
            {"lessons": [1, 2, 3, 4],
             "title": "Agents, Python Data, Functions, Classes, Files and JSON",
             "blurb": "what an AI agent is and the agent loop in plain Python, the course map, then the Python "
                      "AI code is made of: variables, f-strings, lists, dictionaries, sets and comprehensions; "
                      "functions, classes, dataclasses and exceptions; modules, packages, files, JSON and "
                      "environment variables.",
             "tags": ["what is an ai agent", "agent loop python", "python lists dictionaries sets",
                      "python functions classes", "python dataclasses", "python exceptions", "python json",
                      "python modules packages", "python hindi", "hinglish python tutorial"]},
            {"lessons": [5, 6, 7],
             "title": "Type Hints, HTTP, Async + Project: Python AI Toolkit",
             "blurb": "type hints and mypy, HTTP requests with httpx, async and await, then the project: "
                      "{project_blurb}",
             "tags": ["python type hints", "mypy", "httpx tutorial", "python async await", "asyncio gather",
                      "python cli project", "argparse", "pytest tutorial", "python project hindi",
                      "llm usage report"]},
        ],
    },
    2: {
        "title": "LLM Fundamentals and API Integration",
        "project": "AI Study Assistant",
        "project_dir": "ai-study-assistant",
        "project_blurb": "a command-line tutor built on the Anthropic Python SDK that streams "
                         "explanations, writes quizzes as validated JSON, chats with trimmed history, "
                         "and tracks the cost of every call against a budget, with 23 tests.",
        "prereq": "Module 1 (Python for AI Engineering) or equivalent Python. An Anthropic API key is "
                  "optional: every demo also runs in an offline mode with a built-in fake API.",
        "terms": ["llm api python", "anthropic api tutorial", "claude api python", "tokens and context window",
                  "llm streaming python", "structured output json", "api rate limits retries",
                  "llm api cost", "ai study assistant project", "llm in hindi", "claude api hindi",
                  "ai agents course hindi", "python ai hinglish"],
        "tags": "#Python #LLM #ClaudeAPI #AIAgents #Hinglish #PythonInHindi",
        "language": "hinglish",
        "docs": "platform.claude.com/docs/en/build-with-claude/structured-outputs · "
                "platform.claude.com/docs/en/api/errors · platform.claude.com/docs/en/about-claude/pricing",
    },
    3: {
        "title": "Prompt Engineering and Structured Outputs",
        "project": "AI Resume Analyzer",
        "project_dir": "ai-resume-analyzer",
        "project_blurb": "a command-line tool that compares a resume with a job posting and writes a "
                         "skills-gap report, with versioned prompts, structured outputs validated by "
                         "Pydantic, a grounding check, an evaluation set and 27 tests.",
        "prereq": "Module 2 (LLM Fundamentals and API Integration) or equivalent. An Anthropic API key "
                  "is optional: every demo also runs offline with a built-in fake API (keyword rules, "
                  "not a model).",
        "terms": ["prompt engineering", "prompt engineering python", "structured output llm",
                  "pydantic llm", "llm json output", "prompt versioning", "llm evaluation",
                  "prompt injection", "ai resume analyzer", "claude api python"],
        "tags": "#PromptEngineering #Python #LLM #Pydantic #AIAgents",
        "docs": "platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices · "
                "platform.claude.com/docs/en/build-with-claude/structured-outputs · "
                "platform.claude.com/docs/en/test-and-evaluate/develop-tests",
    },
    4: {
        "title": "AI Agent Architecture",
        "project": "Smart Calculator Agent",
        "project_dir": "smart-calculator-agent",
        "project_blurb": "an AI agent built from scratch that solves everyday maths questions with two "
                         "safe tools (an allow-list calculator and a unit converter), prints a trace of "
                         "every action, stops safely, and has 34 tests.",
        "prereq": "Modules 2 and 3, or equivalent. An Anthropic API key is optional: every demo also "
                  "runs offline with a built-in scripted fake API (not a model).",
        "terms": ["ai agent python", "build an ai agent from scratch", "agent loop", "tool use claude",
                  "function calling python", "ai agent tutorial for beginners", "agent vs workflow",
                  "claude api python", "anthropic tool use"],
        "tags": "#AIAgents #Python #ClaudeAPI #LLM #AIEngineering",
        "docs": "platform.claude.com/docs/en/agents-and-tools/tool-use/overview · "
                "platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use · "
                "platform.claude.com/docs/en/build-with-claude/handling-stop-reasons",
    },
    5: {
        "title": "Tool Calling and Function Execution",
        "project": "Personal Productivity Agent",
        "project_dir": "productivity-agent",
        "project_blurb": "an agent that manages tasks and notes with six tools in a registry, schemas "
                         "generated from Pydantic, input validation, per-tool timeouts, read/write/danger "
                         "permissions with human approval for deletes, parallel tool calls, and 43 tests.",
        "prereq": "Module 4 (AI Agent Architecture), or equivalent. An Anthropic API key is optional: every "
                  "demo also runs offline with a built-in scripted fake API (not a model).",
        "terms": ["tool calling python", "function calling claude", "claude tool use tutorial",
                  "parallel tool calls", "pydantic json schema", "ai agent safety", "human in the loop ai",
                  "tool input validation", "ai agent permissions", "productivity agent python"],
        "tags": "#AIAgents #Python #ClaudeAPI #ToolCalling #AIEngineering",
        "docs": "platform.claude.com/docs/en/agents-and-tools/tool-use/overview · "
                "platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use · "
                "platform.claude.com/docs/en/build-with-claude/structured-outputs",
    },
    6: {
        "title": "Agent Memory and Conversation State",
        "project": "Persistent AI Study Companion",
        "project_dir": "study-companion",
        "project_blurb": "a study companion that remembers you across days: long-term facts saved with "
                         "memory tools (secrets refused in code), a running summary for long chats, "
                         "sessions in SQLite with user isolation, retention and delete-my-data, and 41 tests.",
        "prereq": "Module 5 (Tool Calling), or equivalent. An Anthropic API key is optional: every demo also "
                  "runs offline with a built-in scripted fake API (not a model).",
        "terms": ["ai agent memory", "llm conversation history", "claude api memory", "context window tokens",
                  "conversation summary memory", "long term memory ai agent", "sqlite python tutorial",
                  "sql injection python", "chatbot memory python", "study companion ai"],
        "tags": "#AIAgents #Python #ClaudeAPI #AgentMemory #SQLite",
        "docs": "platform.claude.com/docs/en/build-with-claude/context-windows · "
                "platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool · "
                "docs.python.org/3/library/sqlite3.html",
        "parts": [
            {"lessons": [1, 2, 3, 4],
             "title": "Chat History, Context Windows, Summaries, Memory",
             "blurb": "why model APIs forget (stateless), conversation history and a chat loop, tokens and "
                      "the context window, sliding windows that keep tool calls valid, running summaries, "
                      "and long-term facts saved with memory tools and recalled into the system prompt.",
             "other": "SQLite, user isolation, retention, deletion + the Persistent AI Study Companion project",
             "tags": ["ai agent memory", "llm conversation history", "stateless api", "context window tokens",
                      "sliding window chat history", "conversation summary memory", "long term memory ai",
                      "memory tools claude", "claude api python", "chatbot memory python"]},
            {"lessons": [5, 6, 7],
             "title": "SQLite Memory + AI Study Companion Project",
             "blurb": "SQLite from scratch (tables, parameterised queries, SQL injection, transactions, "
                      "schema versions), one user's data kept apart, retention and delete-my-data, and when "
                      "to use PostgreSQL. Then the project: Persistent AI Study Companion, {project_blurb} "
                      "Ends with the module quiz and an extension challenge.",
             "other": "stateless APIs, context windows, summaries and long-term memory",
             "tags": ["sqlite python tutorial", "sql injection python", "sqlite transactions",
                      "ai agent memory database", "user data privacy ai", "postgresql vs sqlite",
                      "persistent chatbot python", "ai study companion", "claude api project",
                      "python sqlite3"]},
        ],
    },
}


def stamp(t):
    t = int(t)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def two_parts(m, info, lessons, datas, src):
    """The module as uploaded in parts: each part's chapters start at 00:00."""
    parts = info.get("parts")
    if not parts:
        return []
    # No length limit: a module is as long as its syllabus needs, split into as many
    # parts as it takes. Every lesson must be in exactly one part, in order.
    covered = [n for part in parts for n in part["lessons"]]
    assert covered == sorted(lessons), f"parts must cover every lesson once, in order: {covered}"
    words = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
    out = [f"## Uploaded in {words.get(len(parts), len(parts))} parts", ""]
    bank = src.replace("/tree/", "/blob/") + "/QUESTIONS.md"
    for k, part in enumerate(parts, 1):
        t, yt, last = 0.0, [], -99.0
        for n in part["lessons"]:
            d = datas[n]
            for c in d["chapters"]:
                if t + c["t"] - last >= 10:
                    yt.append(f"{stamp(t + c['t'])} " + (f"L{n} {d['title']}" if c["t"] == 0 else c["title"]))
                    last = t + c["t"]
            t += d["durationInFrames"] / d["fps"]
        first, final = part["lessons"][0], part["lessons"][-1]
        span = f"Lesson {first}" if first == final else f"Lessons {first}–{final}"
        title = f"AI Agents with Python 2026 · Module {m} (Part {k}/{len(parts)}): {part['title']}"
        assert len(title) <= 100, (len(title), title)
        others = [f"Part {j} ({part['other'] if len(parts) == 2 and 'other' in part else p['title']}): "
                  "https://youtu.be/XXXX" for j, p in enumerate(parts, 1) if j != k]
        blurb = part["blurb"].format(project_blurb=info["project_blurb"])
        text = [f"Module {m} of \"AI Agents with Python: Beginner to Production (2026)\": {info['title']}. "
                f"Part {k} of {len(parts)} ({span}).", "",
                f"In this part: {blurb}", "",
                *others, "",
                "Every lesson explains the concept, shows real code on the left with its real output on the "
                "right, covers common errors, and ends with a quick check, an interview corner and "
                "pause-and-try questions.", "",
                f"Prerequisites: {info['prereq']} You need Python 3.11+ and a code editor.", "",
                f"Source code + README: {src}",
                f"Question bank (every question from the videos, with answers): {bank}", "",
                "Chapters", *yt, "", f"Official docs: {info['docs']}", "", info["tags"]]
        body = "\n".join(text)
        assert "<" not in body and ">" not in body.replace("->", ""), "YouTube rejects angle brackets"
        out += [f"### Part {k}: {span} ({stamp(t)})", "", f"**Title:** {title}", "",
                "```text", body, "```", "", "**Tags:** " + ", ".join(part["tags"]), ""]
    return out


def main(m):
    info = MODULES[m]
    hinglish = info.get("language") == "hinglish"
    mdir = next((ROOT / "modules").glob(f"module-{m:02d}-*"))
    lessons = sorted(int(p.stem.split("-")[1]) for p in (mdir / "scripts").glob("lesson-*.yaml"))
    datas = {n: json.loads((ROOT / f"studio/src/data/m{m:02d}-l{n:02d}.json").read_text()) for n in lessons}
    src = f"{REPO}/{mdir.relative_to(ROOT).as_posix()}"
    out = [f"# Module {m} YouTube packaging", "",
           f"Thumbnail: `assets/thumbnail-module-{m:02d}.png` (1280×720). Captions: `captions/lesson-NN.srt`, "
           f"`captions/module-{m:02d}-full.srt`.", "",
           f"Source-code links point at `{REPO}`; adjust the branch if the course is not merged into `main`.", ""]

    # full module video
    total, chapters = 0.0, []
    for n in lessons:
        d = datas[n]
        for c in d["chapters"]:
            chapters.append((total + c["t"], f"L{n} {d['title']}" if c["t"] == 0 else c["title"]))
        total += d["durationInFrames"] / d["fps"]
    yt, last = [], -99.0
    for t, title in chapters:
        if t - last >= 10:
            yt.append(f"{stamp(t)} {title}")
            last = t
    out += [f"## Full module video (`renders/module-{m:02d}-full.mp4`)", "",
            "**Title**", "", f"AI Agents with Python 2026 · Module {m}: {info['title']} (Full Module + Project)"
            + (" | Hinglish" if hinglish else ""), "",
            "**Description**", "", "```text",
            f"Module {m} of \"AI Agents with Python: Beginner to Production (2026)\": {info['title']}.",
            "",
            f"Project: {info['project']}, {info['project_blurb']}",
            "",
            f"Prerequisites: {info['prereq']} You need Python 3.11+ and a code editor.",
            "",
            *([info.get("style", "Explained in Hinglish (Hindi + English) with Hinglish captions. Every concept "
                "goes What → Why → How → Where → Practice, with real-life analogies, code on the left and its real "
                "output on the right, dry-run tables, an interview corner and practice questions (answers in "
                "quiz.md)."), ""] if hinglish else []),
            info.get("closing", "Every lesson explains the concept, shows real code with real output, covers common "
                     "errors, and ends with a quick check. The module closes with a recap, a 5-question quiz and "
                     "an extension challenge."),
            "",
            f"Source code + README: {src}",
            "",
            "Chapters", *yt, "",
            f"Official docs: {info['docs']}",
            "", info["tags"], "```", "",
            "**Search terms**: " + ", ".join(info["terms"]), ""]

    # per-lesson videos
    out += ["## Individual lesson videos (`renders/lesson-NN.mp4`)", ""]
    for n in lessons:
        d = datas[n]
        dur = d["durationInFrames"] / d["fps"]
        lines, last = [], -99.0
        for c in d["chapters"]:
            if c["t"] - last >= 10:
                lines.append(f"{stamp(c['t'])} {c['title']}")
                last = c["t"]
        title = f"{d['title']} | AI Agents with Python, Module {m} Lesson {n}"
        if len(title) > 100:                   # YouTube's limit: drop the series name first
            title = f"{d['title']} | Module {m} Lesson {n}"
        if len(title) > 100:
            title = f"{d['title'].split(':')[0]} | AI Agents with Python, Module {m} Lesson {n}"
        assert len(title) <= 100, (len(title), title)
        out += [f"### Lesson {n} ({stamp(dur)})", "",
                f"**Title:** {title}", "",
                "```text",
                f"Lesson {n} of Module {m} ({info['title']}) in \"AI Agents with Python: Beginner to Production (2026)\".",
                "",
                f"Source code: {src}",
                "",
                *lines, "", info["tags"], "```", ""]
    out += two_parts(m, info, lessons, datas, src)
    (mdir / "youtube.md").write_text("\n".join(out), encoding="utf-8")
    print(f"youtube.md: full module {stamp(total)}, {len(yt)} chapters")


if __name__ == "__main__":
    main(int(sys.argv[1]))
