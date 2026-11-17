# Module 0 lesson plan

| # | Lesson | Ideas | Analogies | Demo (real output) |
|---|---|---|---|---|
| 1 | The terminal | terminal vs shell vs command; why developers use it; opening it on each OS; anatomy of a command; folder tree, absolute vs relative paths; `pwd` `mkdir` `ls` `cd` `..` `~`; `echo` `>` `>>` `cat` `touch` `wc` `cp` `mv` `rm` `rm -r`; hidden dotfiles and `ls -a`; running Python with arguments; exit codes and `$?`; "No such file" and "command not found"; PATH and `which`; PowerShell equivalents; speed habits | pointing at a menu vs telling the waiter; folders as a building, a path as an address | navigation and files in a fresh folder; `hello.py Riya`; three real errors |
| 2 | venv, pip, .env | the version clash; isolation; `python3 -m venv .venv`; activate per shell; what activate does (PATH); pip and PyPI; `==`, `>=`, `~=`; `pip freeze`; rebuild from `requirements.txt`; commit vs never commit; `python -m pip`, uv; environment variables; `.env` and `.env.example`; reading settings safely; leaked keys; the setup checker | each project's own toolbox; pip as the app store; recipe vs cooked dish; the ATM PIN | `sys.prefix` before/after, `pip list`, install + freeze, delete and rebuild the venv, `export`, `show_config.py`, `check_setup.py` → 5/6 |
| 3 | Git and GitHub | version control; Git vs GitHub; working folder → staging → repository → remote; one-time config; `init` `status`; `.gitignore` and `check-ignore`; `add` `commit` `log`; good messages; `diff`; `restore`; branches, `switch -c`, merge; creating a GitHub repo and signing in; remote, `push -u`, `clone`, `pull`; a pushed secret; README; project wrap-up | save points in a video game; packing, sealing and shipping a parcel | a full Git history built live: 4 commits, a branch, a merge, push to a local bare remote, a second clone, pull; `check_setup.py` → 6/6; 26 tests |

Language: Hinglish narration (Roman script in captions), on-screen text in English. Voice `hf_beta`
at the course's Hinglish speed. Each lesson: objectives, analogy, What → Why → How → Where, real
terminal output, a table or comparison, practice questions (answers in [quiz.md](quiz.md)), an
interview corner, quick checks, a recap and a "coming next" card. Lesson 3 adds the extension
challenge and the documentation links.

Length: no limit (course rule from 2026-11-17). The three lessons run 17:59, 18:05 and 20:49.

Build notes:

- Terminal scenes with `cwd: tmp:projects` share one fresh folder per lesson build, so a lesson's
  demos continue from each other (the folder is shown as `/home/student/projects`).
- Git runs with a throwaway global config (`GIT_CONFIG_GLOBAL`), so the demo identity is the only one
  that ever appears; the machine's own Git settings are removed from the demo environment.
- `run:` lines may prefix `cd my-first-repo &&` (each step runs in its own shell) and use
  `ls -C -T 0` / `git log --decorate` so the output looks exactly as it does in an interactive
  terminal.
