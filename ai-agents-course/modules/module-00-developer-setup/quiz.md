# Module 0 quiz with answers

## Lesson quick checks

**L1 Q1.** You are in `/home/student/projects/my-first-repo`. What does `cd ..` then `pwd` print?
**Answer:** `/home/student/projects`. `..` is the parent folder.

**L1 Q2.** Which command adds a line to the END of `notes.txt` without deleting what is there?
**Answer:** `echo "hi" >> notes.txt`. A single `>` overwrites the file.

**L2 Q1.** Which file do you commit so a teammate can rebuild your environment?
**Answer:** `requirements.txt` (the recipe). `.venv` is rebuilt from it; `.env` is private.

**L2 Q2.** `os.environ.get("DEBUG")` returns `"False"`. What is `bool("False")`?
**Answer:** `True`. Any non-empty string is truthy, so compare text: `value.lower() == "true"`.

**L3 Q1.** In which order do commands put an edit on GitHub?
**Answer:** `git add` → `git commit` → `git push`.

**L3 Q2.** `.env` is in `.gitignore`. What does `git status` show for it?
**Answer:** nothing. Ignored files are not listed (`git check-ignore -v .env` says why).

**L3 Q3.** A teammate pushed new commits. Which command brings them into your local `main`?
**Answer:** `git pull`. `git clone` is only for getting a repository the first time.

## Practice questions (lesson 1)

1. **Nested folders in one command:** `mkdir -p ~/projects/practice/notes`. `-p` creates every missing
   parent folder and doesn't complain if a folder already exists.
2. **Two lines, then count them:**
   ```bash
   echo "buy milk" > todo.txt
   echo "learn git" >> todo.txt
   wc -l todo.txt        # 2 todo.txt
   wc -l < todo.txt      # 2   (only the number)
   ```
   The second line must use `>>`, or it replaces the first.
3. **Run `hello.py` from the parent folder:** `python3 my-first-repo/hello.py` (a relative path from
   `projects`), or the absolute path `python3 ~/projects/my-first-repo/hello.py`. Python runs the file
   either way, but anything the program opens with a relative path is looked up from where you ran it.
4. **Works for me, fails for a teammate. Three causes:** (a) a relative path such as `open("data.csv")`
   and the script is run from a different folder; (b) a different Python, or a package missing because
   their venv isn't active or they skipped `pip install -r requirements.txt`; (c) a setting that only
   exists on your machine: an environment variable or a `.env` they don't have. Also common: `python`
   vs `python3` on Windows, and file names that differ only in capital letters (Linux and macOS
   treat `Data.csv` and `data.csv` differently).

## Practice questions (lesson 2)

1. **A new terminal:** the venv is **not** active. Every window starts fresh. Check with the prompt (no
   `(.venv)`), with `which python` (not inside `.venv`), or with
   `python -c "import sys; print(sys.prefix != sys.base_prefix)"` → `False`. Run
   `source .venv/bin/activate` again.
2. **Install `requests` at an exact version:** with the venv active,
   `pip install requests==<version>` (pick one from `pip index versions requests` or pypi.org), then
   `pip freeze > requirements.txt`. The file now also lists requests' own dependencies (`certifi`,
   `charset-normalizer`, `idna`, `urllib3`) at exact versions: that is what makes the install
   repeatable.
3. **A `GREETING` setting:** add `GREETING=Hello` to `.env.example` **and** `.env`, then:
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
4. **`ModuleNotFoundError` on a teammate's laptop:** the package is installed on your machine but not
   on theirs. Usually you installed it without updating `requirements.txt` (or installed it globally,
   outside the venv), or they didn't run `pip install -r requirements.txt` inside an **activated**
   venv. Fix: `pip freeze > requirements.txt`, commit it; they activate the venv and run
   `pip install -r requirements.txt`.

## Practice questions (lesson 3)

1. **See unstaged changes:** `git diff`. For changes already staged with `git add`:
   `git diff --staged`.
2. **Branch, change, merge:**
   ```bash
   git switch -c add-greeting
   # edit greet() in hello.py, run python -m pytest -q
   git commit -am "Make the greeting friendlier"
   git switch main
   git merge add-greeting
   ```
   If `main` got no new commits meanwhile, the merge is a fast-forward.
3. **Unstage a file:** `git restore --staged secrets.txt`. The file stays on disk, untracked
   (`?? secrets.txt`). Then add it to `.gitignore` so it can't be added again by accident. If it was
   already **committed**, treat any secret in it as leaked: revoke it.
4. **Two teammates edit the same README line:** the first to push wins. The second push is rejected
   (`! [rejected] main -> main (fetch first)`). The second person runs `git pull`. With Git 2.43 and
   no setting, Git stops and asks how to combine the diverged branches: use `git pull --no-rebase`
   (merge) or set it once with `git config --global pull.rebase false`. Git reports
   `CONFLICT (content): Merge conflict in README.md` and writes both versions into the file between
   `<<<<<<< HEAD`, `=======` and `>>>>>>>`. Edit the file to the right text, delete the markers, then
   `git add README.md`, `git commit`, `git push`.

## Extension challenge

Pick one or more and push each to your real GitHub repository:

- **A 7th check:** warn about uncommitted changes. `git status --porcelain` prints nothing when the
  working tree is clean; run it with `subprocess.run(..., capture_output=True, text=True)` and add a
  test for both cases.
- **`--quiet`:** print only failed checks (and the summary line). Test it with `capsys`.
- **A profile README:** a public repository named exactly like your GitHub username, with a
  `README.md`. GitHub shows it on your profile page.
- **SSH:** create a key with `ssh-keygen -t ed25519`, add the **public** key (`.pub`) in GitHub
  settings, check with `ssh -T git@github.com`, then
  `git remote set-url origin git@github.com:your-name/my-first-repo.git`. Never share the private key.
