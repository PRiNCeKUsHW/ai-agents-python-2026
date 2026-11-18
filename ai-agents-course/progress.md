# Course progress

Source of truth: `COURSE_MANIFEST.json` (update only with `tools/manifest.py`, and only after real checks).

## Plan revised 2026-11-16: 20 modules, 153 lessons

- New **Module 0: Your Developer Setup** (terminal, virtual environments and .env, Git and GitHub; project:
  Your First GitHub Repository) and new **Module 19: AI Career Switch** (project: Your AI Engineer Portfolio).
- Modules 7–18 expanded: 7 has 10 lessons (providers, model routing, context engineering), 8 has 8
  (remote MCP, OAuth), 10 has 11 (hybrid search, vision PDFs, access control, a read-only SQL agent:
  "Ask Your Database"), 14–16 have 9, 9 and 10 (observability, OWASP, Redis, background jobs).
- Modules 1–6 are unchanged and stay COMPLETED.
- Full lesson list with sub-topics: `COURSE_SYLLABUS.md`; per-lesson titles and topics also in the manifest.
- Done: 6 of 20 modules, 40 of 153 lessons. Remaining: Module 0 and Modules 7–19 (113 lessons).
  Update 2026-11-17: Module 0 done, so 7 of 20 modules, 43 of 153 lessons; remaining Modules 7–19 (110 lessons).

## Module 1: Python for AI Engineering: COMPLETED

- 7 lessons rendered (1920x1080, 60 fps, H.264 + AAC, about -17 LUFS); full module video 56:58 with 66 chapters
- `validation-report.md`: 69/69 checks passed (formats, durations, captions, loudness, no black frames,
  no long silences, fresh-venv install, 42 tests, mypy, documented CLI commands)
- Lessons 4 and 5 were re-rendered after a fix: compare scenes now show dimmed panels during intro narration
- **Remade 2026-11-18 in Hinglish** (learner's request): voice `hf_beta` at 0.95 (the learner's pick of
  sample 2; Priyamvada/Piper was rejected for its non-commercial licence), new theme **Python Notebook**,
  the newer teaching style (analogy, What → Why → How → Where, code + real output, interview corner,
  practice, two quick checks per lesson). Lesson 1 now shows a 30-line agent loop with a labelled fake
  model and the 20-module map; setup is only checked (Module 0 teaches it). Full video 1:20:48,
  84 chapters, 1325 captions; validation 69/69. Two YouTube parts: lessons 1–4 (46:33), 5–7 (34:14).
  Panel colour tokens (`codePrompt`, `codeCmd`, ...) added so terminal text is readable on any theme.
- 2026-11-18: Hinglish lesson videos downloaded by the learner; local videos, narration audio and
  studio audio deleted (rebuild with `python tools/build_lesson.py 1 all` and `python tools/module.py render 1`;
  the voice cache is kept).
- Videos and audio are not in git (too large); they were delivered from the cloud session

## Local Windows machine (set up 2026-10-29)

- Git Bash runs the demo commands (no WSL). `tools/build_lesson.py` and `tools/module.py` pick
  `.venv/Scripts` on Windows, add a `python3` shim (the Windows `python3` is the Microsoft Store stub),
  and map `.venv/bin/` to `.venv/Scripts/` in `run:` commands. On Linux, nothing changes.
- Two environments. `.venv` (Python 3.14.3) runs every demo shown on screen. `.venv-tools`
  (Python 3.12, kokoro-onnx 0.6.1) runs the build tools, because kokoro-onnx ≥ 0.4.8 needs
  Python < 3.14. Run `.venv-tools/Scripts/python tools/build_lesson.py …` (and module.py the same way).
- Kokoro model: the default `~/.cache/hyperframes/tts` already has it; `KOKORO_DIR` isn't needed.
- Remotion downloads its own Chrome Headless Shell on the first render or still.
- Windows-built captures show Windows details (Python 3.14.3, `.venv/Scripts/python`). Module 1 was
  not rebuilt here. Module 2 lessons avoid OS-specific output where possible.
- Fixed: Module 1 `test_friendly_error_for_missing_file` now builds the expected path with `Path`, so it
  passes on Windows too (project code unchanged, so it still matches the videos).

## Module 2: LLM Fundamentals and API Integration: COMPLETED (2026-10-29)

- **Remade 2026-10-30 in Hinglish** (learner's request): Indian female voice B at 0.85, Roman Hinglish
  captions, light Paper theme, What → Why → How → Where → Practice with analogies, code + real output
  side by side, dry-run tables, interview corner and practice questions per lesson (answers in quiz.md).
  Full video 1:05:33, 73 chapters, 995 captions; validation 70/70. Pronunciation fixes from the
  learner's review: "API" spelled with Indian letter names, "model" said mo-DEL.
  The original English details below describe the first version.
- **Uploaded to YouTube 2026-10-31 in two parts:** Part 1 lessons 1-4 (36:31), Part 2 lessons 5-7
  (29:02). Titles, descriptions, chapters and tags: `modules/module-02-llm-fundamentals/youtube.md`.

- 7 lessons rendered (1920x1080 60 fps), full module video 41:05 with 59 chapters and 632 captions.
- Project: AI Study Assistant, 23 tests passing; every demo runs offline against `study/fake_api.py`.
- Validation: 70/70 checks (`modules/module-02-llm-fundamentals/validation-report.md`).
- Upload kits: `modules/module-02-llm-fundamentals/youtube-uploads.md` (videos #8-#14).

## Module 3: Prompt Engineering and Structured Outputs: COMPLETED (2026-10-29)

- Delivered as ONE full-module video (user request): 30:32, 49 chapters, 478 captions (6 parts rendered, then joined).
- Project: AI Resume Analyzer, 27 tests, mypy clean; offline fake uses keyword rules (not a model) and says so.
- Validation: 62/62 checks (`modules/module-03-prompt-engineering/validation-report.md`).
- Upload kit: `modules/module-03-prompt-engineering/youtube-uploads.md` (video #15).

## Module 4: AI Agent Architecture: COMPLETED (2026-10-30)

- ONE full-module video: 36:45, 56 chapters, 546 captions, beginner pacing + a Pause-and-try in every part.
- Project: Smart Calculator Agent, 34 tests, mypy clean; offline fake is a fixed script (not a model) and says so.
- Validation: 62/62 checks. Upload kit: `modules/module-04-agent-architecture/youtube-uploads.md` (video #16).
- Rendering: `studio/render.mjs` renders all parts from one bundle and deletes it (avoids /tmp build-up).

## Module 5: Tool Calling and Function Execution: COMPLETED (2026-10-31)

- English narration (am_michael, 0.92), light theme, the learner's teaching style (analogies, code +
  real output, dry-run tables, interview corner, practice with answers in quiz.md).
- 7 lessons, full video 52:47, 67 chapters, 817 captions. Validation 70/70.
- Project: Personal Productivity Agent: registry + Pydantic schemas (strict), validation, per-tool
  timeouts, read/write/danger permissions with read-only mode and human approval, parallel tool calls,
  atomic JSON store. 43 tests, mypy clean.
- Renders resume after a container restart (`studio/render.mjs` skips lessons already rendered).
- **Uploaded to YouTube 2026-10-31 in two parts:** Part 1 lessons 1-4 (29:41), Part 2 lessons 5-7
  (23:06). Titles, descriptions, chapters and tags: `modules/module-05-tool-calling/youtube.md`.
  Question bank: `modules/module-05-tool-calling/QUESTIONS.md`. Local video files deleted after upload
  (rebuild with `python tools/module.py render 5`).

## Module 6: Agent Memory and Conversation State: COMPLETED (2026-11-01)

- English narration (am_michael, 0.92), light theme, the learner's teaching style.
- 7 lessons, full video 54:40, 75 chapters, 841 captions. Validation 71/71.
- Project: Persistent AI Study Companion: long-term facts saved with memory tools (secrets refused in
  code), relevant facts in the system prompt, running summary above a token limit, sessions in SQLite
  with user isolation, retention (`purge`) and deletion (`delete-me`). 41 tests, mypy --strict clean.
- First module with **recorded sound effects** (user request): `tools/sfx.py` sets up `shared/sfx/`
  from the media-use skill's bundled set (Pixabay licence); Openverse and Earshot were blocked by the
  session's network policy (the tool can fetch Openverse CC0/CC BY effects once allowed, and import
  Earshot files downloaded by hand). Keyboard sounds play under typed commands. Modules 1-5 unchanged.
- Ready for a two-part upload: Part 1 lessons 1-4 (28:53), Part 2 lessons 5-7 (25:46); packaging in
  `modules/module-06-agent-memory/youtube.md`.
- Lesson 7's terminal demo continues lesson 6's data: build lesson 6 before lesson 7.
- 2026-11-01: videos downloaded by the learner for the two-part upload; local video files and studio
  audio deleted to free space (rebuild with `python tools/build_lesson.py 6 all` and
  `python tools/module.py render 6`; the voice cache is kept, so rebuilding needs no new narration).

## Module 0: Your Developer Setup: COMPLETED (2026-11-17)

- **Hinglish** narration (Kokoro `hf_beta`), Roman-script captions, on-screen text in English.
- First module with its own theme: **Terminal Night** (GitHub-dark, terminal green, Git orange); see the
  theme register in `COURSE_DESIGN_SYSTEM.md`. First module made under the no-length-limit rule.
- 3 lessons (17:59, 18:05, 20:49); full video 56:54, 50 chapters, 928 captions. Validation 38/38.
- Project: Your First GitHub Repository (`hello.py`, `show_config.py`, `check_setup.py` with six checks:
  5/6 before `git init`, 6/6 after). 26 tests, mypy --strict clean.
- Git demos use the made-up identity Riya Sharma <riya@example.com> in a throwaway global config; the
  "GitHub" remote is a local bare repository, and the video says so.
- Ready for a two-part upload: Part 1 lessons 1-2 (36:05), Part 2 lesson 3 (20:49); packaging in
  `modules/module-00-developer-setup/youtube.md`.
- 2026-11-18: videos (full, Part 1, lessons) downloaded by the learner; local video files, narration
  audio and studio audio deleted (rebuild with `python tools/build_lesson.py 0 all` and
  `python tools/module.py render 0`; the voice cache is kept).

## Next: Module 7: Reliable and Efficient Agents (project: Resilient API Agent)

All scripts follow `TEACHING_STYLE.md` (the learner's brief): What → Why → How → Where → Practice,
real-life analogies, line-by-line code with dry runs, an interview section, and practice at the end.

Beginner-friendliness rules from Module 4 on (user request, 2026-10-30):
- Slower pacing: `tools/build_lesson.py` applies `BEGINNER_PACING` for module >= 4 (voice speed 0.92,
  longer pauses between beats and sentences). Modules 1-3 keep the original pacing.
- More explanation time: explain every new term the first time it's used (and add it to
  `GLOSSARY.md`), say why before how, and recap the previous step before a new one.
- One "Pause and try" moment per lesson: a `callout` (kind: tip) with a short task and a 5 s pause beat.
- Update `GLOSSARY.md` with the module's new terms.

From Module 5 on (user request, 2026-10-30): explain code with the split `run` scene, code on the
left and the real output of running it on the right. The builder runs `cmd` in `cwd` once; each
step highlights code `lines` and can point at output lines with `out: "2"` (the command is typed at
the first such step, and output appears up to the furthest line pointed at). Keep plain `code`
scenes for files that don't run on their own (classes, tool definitions).

    - type: run
      heading: "mini_agent.py: code and what it printed"
      title: mini_agent.py
      file: source/lesson-03/mini_agent.py
      cwd: source/lesson-03
      cmd: python mini_agent.py
      steps:
        - {lines: "17-21", out: "2", note: "...", say: "..."}

Notes carried over from Module 1:

Notes for the next modules, learned in Module 1:
- Keep project code ≤ 84 characters per line so code panels stay ≥ 27 px.
- Prefer `repl: true` terminal scenes for exploring objects; keep each statement ≤ ~85 characters.
- Terminal commands must fit one line (~95 characters at 28 px; set `font: 25` for longer ones).
- Links scenes: at most 8 items. Code `notes` sit beside short code, below wide code (≤ 2 short lines).
- Edge labels in diagrams sit on the curve midpoint; keep boxes off the curve paths.
- Never use a real API key in recorded output. Module 2 needs an LLM API: use a mock/fake transport
  for tests and recorded demos unless a key is configured in the environment; say clearly on screen
  which outputs come from a real model call.

## Rule added 2026-11-17: no video length limit
- Each module is as long as its full syllabus needs. Nothing is cut to fit a time.
- Long modules are uploaded in as many parts as needed, not only two. `tools/youtube.py` now supports any number of parts and checks that every lesson is covered exactly once. Module 6's packaging is unchanged.
- The "19–20 hours" in the plan is an estimate, not a cap.

## Rule added 2026-11-17: a new theme and style per module
- Each module gets a theme and style chosen from its syllabus, never repeating an earlier module.
- `studio/src/theme.ts` now has per-module `THEMES` and `applyTheme(module)`; the register is in `COURSE_DESIGN_SYSTEM.md`.
- Module 0 uses **Terminal Night** (dark, terminal green, Git orange).
