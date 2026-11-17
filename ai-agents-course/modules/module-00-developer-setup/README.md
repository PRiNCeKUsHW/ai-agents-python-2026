# Module 0: Your Developer Setup

Start here · **AI Agents with Python: Beginner to Production (2026)** · narrated in **Hinglish**

Before any AI code, every AI engineer needs three everyday tools: the **terminal**, a **virtual
environment** per project (with `pip` and a `.env` file for settings and secrets), and **Git with
GitHub**. This module teaches all three from zero, with every command run for real on screen, and ends
with your first GitHub repository: a small project with a **setup checker** that confirms the project
is set up the way every project in this course is.

> **About the demos:** every command and its output on screen is a real run. Git demos use a made-up
> identity (`Riya Sharma <riya@example.com>`) set in a throwaway config. So that no account or password
> appears, the "GitHub" remote in Lesson 3 is a **bare repository in a local folder** (`fake-github/`),
> and the video says so; the commands are the same as with GitHub, only the URL differs. No API key is
> used anywhere in this module: `.env` holds placeholder values only.

## Learning objectives

- Explain terminal vs shell; move around with `pwd`, `ls`, `cd`, absolute and relative paths
- Create, read, copy, move and delete files; see hidden files; avoid the `rm` traps
- Run Python with arguments; read exit codes; fix "No such file" and "command not found" (PATH)
- Explain why projects need virtual environments; create, activate and rebuild a `.venv`
- Install exact versions with `pip`, record them in `requirements.txt`, rebuild from it
- Keep settings and secrets in environment variables and a git-ignored `.env`; commit `.env.example`
- Use Git: `init`, `status`, `add`, `commit`, `log`, `diff`, `restore`, branches and merges
- Use a remote the way GitHub works: `remote add`, `push -u`, `clone`, `pull`; handle a leaked secret

## Prerequisites

None. A computer with Python 3.11+ and Git installed (Windows: Git for Windows, which includes Git
Bash). New terms are in the course [glossary](../../GLOSSARY.md).

## Video chapters

| # | Lesson | Length | Script |
|---|---|---|---|
| 1 | The Terminal: Folders, Files and Running Commands | 17:59 | `scripts/lesson-01.yaml` |
| 2 | Virtual Environments, pip and the .env File: Why Every Project Gets Its Own | 18:05 | `scripts/lesson-02.yaml` |
| 3 | Git and GitHub: Save, Commit, Push and Share Your Work | 20:49 | `scripts/lesson-03.yaml` |

Full module: **56:54**. All runnable code is in the project folder. Plan:
[lesson-plan.md](lesson-plan.md). Every lesson follows the course teaching style
([TEACHING_STYLE.md](../../TEACHING_STYLE.md)): an analogy, What → Why → How → Where, real terminal
output, a comparison or table, practice questions, an interview corner, a quick check and a recap.

## Project: Your First GitHub Repository

[`project/my-first-repo/`](project/my-first-repo/README.md)

| File | What it does |
|---|---|
| `hello.py` | the first program: reads its arguments, returns an exit code |
| `show_config.py` | reads settings from `.env` with python-dotenv; never prints the secret |
| `check_setup.py` | six checks: Python 3.11+, venv active, pinned packages, `.env` complete, `.gitignore` protects `.env` and `.venv/`, git repository; exit code 0 only when all pass |
| `requirements.txt`, `.env.example`, `.gitignore` | the recipe, the settings template, what git must never track |
| `tests/` | 26 pytest tests (pass and fail cases of every check) |

In Lesson 2 the checker reports **5/6** (not a git repository yet); in Lesson 3, after `git init`,
**6/6**. mypy `--strict` is clean.

## Deliverables

| What | Where |
|---|---|
| Lesson videos and full module video (1920×1080, 60 fps, H.264 + AAC) | `renders/` (not committed) |
| Narration scripts / audio | `scripts/*.yaml` / `audio/` (audio not committed) |
| Captions (Roman Hinglish) | `captions/module-00-full.srt` and `captions/lesson-NN.srt` |
| Quiz, practice answers, extension challenge | [quiz.md](quiz.md) |
| Question bank: every question from the videos, answers hidden | [QUESTIONS.md](QUESTIONS.md) |
| Thumbnail | `assets/thumbnail-module-00.png` |
| YouTube packaging | [youtube.md](youtube.md) |
| Validation report | [validation-report.md](validation-report.md) |

## Versions used

Python 3.13 · python-dotenv 1.2.4 · pytest 9.2.0 · pip 26.2 · Git 2.43 · bash · Remotion 4.0.538 ·
Kokoro v1.0 (Hinglish, Indian female voice `hf_beta`) · recorded sound effects
([credits](../../shared/sfx/CREDITS.md)).

**Theme: "Terminal Night"**, new for this module (every module now gets its own look; see the
register in [COURSE_DESIGN_SYSTEM.md](../../COURSE_DESIGN_SYSTEM.md)): a GitHub-dark page, terminal
green for the prompt and success, Git orange for highlights.
