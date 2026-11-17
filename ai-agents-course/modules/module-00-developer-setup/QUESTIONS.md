# Module 0 question bank: Your Developer Setup

Every question asked in the Module 0 videos, with answers. **32 questions.**

How to use it: read the question, answer it out loud or on paper, *then* click **Show answer**. Getting one wrong is useful: rewatch that lesson's chapter.

The videos are narrated in Hinglish; the questions here are the English text shown on screen.

Short answer key, practice answers and the extension challenge: [quiz.md](quiz.md) · Module guide: [README.md](README.md)

## Lesson 1: The Terminal: Folders, Files and Running Commands

### Module quiz

**Q1. You are in `/home/student/projects/my-first-repo`. What does `cd ..` then `pwd` print?**

- A) `/home/student/projects/my-first-repo`
- B) `/home/student/projects`
- C) `/home/student`
- D) `/`

<details>
<summary>Show answer</summary>

**B) `/home/student/projects`**

`..` is the parent folder: one level up from `my-first-repo` is `projects`.

</details>

**Q2. Which command adds a line to the END of `notes.txt` without deleting what is there?**

- A) `echo "hi" > notes.txt`
- B) `echo "hi" >> notes.txt`
- C) `cat "hi" notes.txt`
- D) `touch notes.txt "hi"`

<details>
<summary>Show answer</summary>

**B) `echo "hi" >> notes.txt`**

`>>` appends. A single `>` overwrites the file.

</details>

### Try these before the next lesson

Easy to hard.

**1. Make `~/projects/practice/notes` in one command (hint: `mkdir -p`)**

<details>
<summary>Show answer</summary>

`mkdir -p ~/projects/practice/notes`. `-p` creates every missing
parent folder and doesn't complain if a folder already exists.

</details>

**2. Write two lines to `todo.txt`, then show only the file's line count with `wc -l`**

<details>
<summary>Show answer</summary>

```bash
echo "buy milk" > todo.txt
echo "learn git" >> todo.txt
wc -l todo.txt        # 2 todo.txt
wc -l < todo.txt      # 2   (only the number)
```
The second line must use `>>`, or it replaces the first.

</details>

**3. Run `python3 hello.py` from the parent folder. What path do you need?**

<details>
<summary>Show answer</summary>

`python3 my-first-repo/hello.py` (a relative path from
`projects`), or the absolute path `python3 ~/projects/my-first-repo/hello.py`. Python runs the file
either way, but anything the program opens with a relative path is looked up from where you ran it.

</details>

**4. Scenario: a script works in your folder but fails when a teammate runs it. Find three causes.**

<details>
<summary>Show answer</summary>

(a) a relative path such as `open("data.csv")`
and the script is run from a different folder; (b) a different Python, or a package missing because
their venv isn't active or they skipped `pip install -r requirements.txt`; (c) a setting that only
exists on your machine: an environment variable or a `.env` they don't have. Also common: `python`
vs `python3` on Windows, and file names that differ only in capital letters (Linux and macOS
treat `Data.csv` and `data.csv` differently).

</details>

### Interview corner

**Interviewer:** What is the difference between an absolute and a relative path?

<details>
<summary>Show answer</summary>

**A good answer:** An **absolute** path starts at the root (`/home/student/projects/app.py`) and works from anywhere. A **relative** path starts from the current working directory (`app.py`, `../data/x.csv`), so it depends on where you run the command.

**Trap to avoid:** Code that opens `data.csv` works on your machine and fails in production because it was run from a different folder.

</details>

**Interviewer:** What does an exit code tell you?

<details>
<summary>Show answer</summary>

**A good answer:** Whether a command succeeded: **0 means success**, anything else is a failure. Scripts, CI pipelines and tools like `&&` use it to decide what runs next.

**Trap to avoid:** Checking only the printed text. A program can print "done" and still fail with a non-zero code.

</details>

**Interviewer:** You type `python3` and get "command not found". What do you check?

<details>
<summary>Show answer</summary>

**A good answer:** Spelling first; then whether Python is installed; then whether its folder is on **PATH** (`which python3`, `echo $PATH`). On Windows, try `python` or `py`.

**Trap to avoid:** Reinstalling everything before reading the error.

</details>

## Lesson 2: Virtual Environments, pip and the .env File: Why Every Project Gets Its Own

### Module quiz

**Q1. Which file should you commit so a teammate can rebuild your environment?**

- A) `.venv/`
- B) `.env`
- C) `requirements.txt`
- D) `__pycache__/`

<details>
<summary>Show answer</summary>

**C) `requirements.txt`**

`requirements.txt` is the recipe. `.venv` is rebuilt from it, `.env` holds private values, and `__pycache__` is generated.

</details>

**Q2. `os.environ.get("DEBUG")` returns `"False"`. What is `bool("False")`?**

- A) `False`
- B) `True`
- C) `None`
- D) an error

<details>
<summary>Show answer</summary>

**B) `True`**

Any non-empty string is truthy. Compare the text instead: `value.lower() == "true"`, as `show_config.py` does.

</details>

### One laptop, two projects, one clash

Project A was built with **library v1**. Project B needs **library v2**. Without isolation, Python keeps **one copy** of each library for the whole computer: installing v2 for B silently breaks A. This is where "but it works on my machine!" comes from.

**1. Projects need different versions of the same package**

**2. A global install changes every project at once**

**3. Your teammate's computer has different versions than yours**

<details>
<summary>Show answer</summary>

the venv is **not** active. Every window starts fresh. Check with the prompt (no
`(.venv)`), with `which python` (not inside `.venv`), or with
`python -c "import sys; print(sys.prefix != sys.base_prefix)"` → `False`. Run
`source .venv/bin/activate` again.

with the venv active,
`pip install requests==<version>` (pick one from `pip index versions requests` or pypi.org), then
`pip freeze > requirements.txt`. The file now also lists requests' own dependencies (`certifi`,
`charset-normalizer`, `idna`, `urllib3`) at exact versions: that is what makes the install
repeatable.

add `GREETING=Hello` to `.env.example` **and** `.env`, then:
```python
import os
from dotenv import load_dotenv

load_dotenv()

def greet(name: str = "world") -> str:
    greeting = os.environ.get("GREETING", "Hello")
    return f"{greeting}, {name}!"
```
With `GREETING=Namaste` in `.env`, `python hello.py Riya` prints `Namaste, Riya!`. The default keeps
the existing tests passing. `check_setup.py` will now report a `.env` that lacks `GREETING`.

the package is installed on your machine but not
on theirs. Usually you installed it without updating `requirements.txt` (or installed it globally,
outside the venv), or they didn't run `pip install -r requirements.txt` inside an **activated**
venv. Fix: `pip freeze > requirements.txt`, commit it; they activate the venv and run
`pip install -r requirements.txt`.

</details>

### Try these before the next lesson

Easy to hard.

**1. Open a NEW terminal. Is your venv still active? How do you check?**

<details>
<summary>Show answer</summary>

the venv is **not** active. Every window starts fresh. Check with the prompt (no
`(.venv)`), with `which python` (not inside `.venv`), or with
`python -c "import sys; print(sys.prefix != sys.base_prefix)"` → `False`. Run
`source .venv/bin/activate` again.

</details>

**2. Install `requests` at an exact version, then update `requirements.txt`**

<details>
<summary>Show answer</summary>

with the venv active,
`pip install requests==<version>` (pick one from `pip index versions requests` or pypi.org), then
`pip freeze > requirements.txt`. The file now also lists requests' own dependencies (`certifi`,
`charset-normalizer`, `idna`, `urllib3`) at exact versions: that is what makes the install
repeatable.

</details>

**3. Add a setting `GREETING` to `.env.example` and `.env`; make `hello.py` read it**

<details>
<summary>Show answer</summary>

add `GREETING=Hello` to `.env.example` **and** `.env`, then:
```python
import os
from dotenv import load_dotenv

load_dotenv()

def greet(name: str = "world") -> str:
    greeting = os.environ.get("GREETING", "Hello")
    return f"{greeting}, {name}!"
```
With `GREETING=Namaste` in `.env`, `python hello.py Riya` prints `Namaste, Riya!`. The default keeps
the existing tests passing. `check_setup.py` will now report a `.env` that lacks `GREETING`.

</details>

**4. Scenario: your app works, but crashes on a teammate's laptop with `ModuleNotFoundError`. Explain why, and the fix.**

<details>
<summary>Show answer</summary>

the package is installed on your machine but not
on theirs. Usually you installed it without updating `requirements.txt` (or installed it globally,
outside the venv), or they didn't run `pip install -r requirements.txt` inside an **activated**
venv. Fix: `pip freeze > requirements.txt`, commit it; they activate the venv and run
`pip install -r requirements.txt`.

</details>

### Interview corner

**Interviewer:** Why do Python projects use virtual environments?

<details>
<summary>Show answer</summary>

**A good answer:** To **isolate** each project's packages and versions, so projects don't break each other, and so the setup can be **reproduced** exactly from `requirements.txt` on any machine.

**Trap to avoid:** "To make Python faster." A venv changes which packages are used, not speed.

</details>

**Interviewer:** Do you commit the `.venv` folder?

<details>
<summary>Show answer</summary>

**A good answer:** No. Commit `requirements.txt` (the recipe) and ignore `.venv` (it is big, machine-specific and rebuildable with `pip install -r requirements.txt`).

**Trap to avoid:** Committing `.venv` "so teammates don't need to install". It breaks on other operating systems and Python versions.

</details>

**Interviewer:** How do you handle API keys in a Python project?

<details>
<summary>Show answer</summary>

**A good answer:** Read them from **environment variables**, loaded from a git-ignored `.env` in development or a secrets manager in production. Commit only `.env.example` with names and placeholders. Never print or log the value; revoke a key if it leaks.

**Trap to avoid:** Hard-coding the key "just for now". It ends up in git history.

</details>

## Lesson 3: Git and GitHub: Save, Commit, Push and Share Your Work

### Module quiz

**Q1. You edited `app.py`. In which order do these commands put it on GitHub?**

- A) `git push` → `git commit` → `git add`
- B) `git commit` → `git add` → `git push`
- C) `git add` → `git commit` → `git push`
- D) `git add` → `git push` → `git commit`

<details>
<summary>Show answer</summary>

**C) `git add` → `git commit` → `git push`**

Stage the change (`add`), save it in the local history (`commit`), then send the commits to the remote (`push`).

</details>

**Q2. `.env` is listed in `.gitignore`. What does `git status` show for it?**

- A) `modified: .env`
- B) `new file: .env`
- C) Nothing: ignored files are not listed
- D) An error

<details>
<summary>Show answer</summary>

**C) Nothing: ignored files are not listed**

Ignored files don't appear in `git status`. Check why a file is ignored with `git check-ignore -v .env`.

</details>

**Q3. A teammate pushed new commits. Which command brings them into your local `main`?**

- A) `git clone`
- B) `git pull`
- C) `git push`
- D) `git init`

<details>
<summary>Show answer</summary>

**B) `git pull`**

`pull` fetches new commits from the remote and merges them. `clone` is only for getting a repository the first time.

</details>

### Practice questions

Easy to hard.

**1. Which command shows what changed in a file that you have not staged yet?**

<details>
<summary>Show answer</summary>

`git diff`. For changes already staged with `git add`:
`git diff --staged`.

</details>

**2. Make a branch `add-greeting`, change `greet()`, commit, merge into `main`**

<details>
<summary>Show answer</summary>

```bash
git switch -c add-greeting
# edit greet() in hello.py, run python -m pytest -q
git commit -am "Make the greeting friendlier"
git switch main
git merge add-greeting
```
If `main` got no new commits meanwhile, the merge is a fast-forward.

</details>

**3. You ran `git add secrets.txt` by mistake. Unstage it (hint: `git restore --staged`)**

<details>
<summary>Show answer</summary>

`git restore --staged secrets.txt`. The file stays on disk, untracked
(`?? secrets.txt`). Then add it to `.gitignore` so it can't be added again by accident. If it was
already **committed**, treat any secret in it as leaked: revoke it.

</details>

**4. Scenario: two teammates edit the same line of README. Walk through what happens on `git pull`.**

<details>
<summary>Show answer</summary>

the first to push wins. The second push is rejected
(`! [rejected] main -> main (fetch first)`). The second person runs `git pull`. With Git 2.43 and
no setting, Git stops and asks how to combine the diverged branches: use `git pull --no-rebase`
(merge) or set it once with `git config --global pull.rebase false`. Git reports
`CONFLICT (content): Merge conflict in README.md` and writes both versions into the file between
`<<<<<<< HEAD`, `=======` and `>>>>>>>`. Edit the file to the right text, delete the markers, then
`git add README.md`, `git commit`, `git push`.

</details>

### Interview corner

**Interviewer:** What is the difference between Git and GitHub?

<details>
<summary>Show answer</summary>

**A good answer:** **Git** is the version control tool that runs on your computer: commits, history, branches. **GitHub** is a website that hosts Git repositories and adds collaboration: pull requests, reviews, issues.

**Trap to avoid:** Saying they are the same thing, or that you need GitHub to use Git.

</details>

**Interviewer:** Explain `git add`, `git commit` and `git push`.

<details>
<summary>Show answer</summary>

**A good answer:** `add` moves changes into the **staging area** (choose what goes in). `commit` saves the staged snapshot in the **local** history with a message. `push` sends your commits to the **remote**, like GitHub.

**Trap to avoid:** Thinking `commit` uploads your work. Until you push, it exists only on your laptop.

</details>

**Interviewer:** You committed an API key and pushed it. What do you do?

<details>
<summary>Show answer</summary>

**A good answer:** **Revoke the key immediately** and issue a new one; then remove the file, add it to `.gitignore`, and if needed clean the history. Revoking comes first because the key must be treated as already stolen.

**Trap to avoid:** "I deleted the file in the next commit." The key is still in the history.

</details>

**Interviewer:** What is a merge conflict?

<details>
<summary>Show answer</summary>

**A good answer:** When two branches change **the same lines** differently, Git can't choose for you. It marks both versions in the file; you edit it to the right result, then `add` and `commit`.

**Trap to avoid:** Panicking, or deleting and re-cloning. A conflict is normal: read both sides, keep the right code.

</details>
