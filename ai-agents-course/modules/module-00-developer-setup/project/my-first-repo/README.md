# My First Repo

My first project for **AI Agents with Python: Beginner to Production (2026)**, Module 0.

It has a tiny program, `hello.py`, and a **setup checker**, `check_setup.py`, that confirms
this project is set up the way every project in the course is:

1. Python 3.11 or later
2. a virtual environment (`.venv`) is active
3. the packages in `requirements.txt` are installed at the pinned versions
4. a `.env` file has every setting listed in `.env.example`
5. `.gitignore` keeps `.env` and `.venv/` out of git
6. the folder is a git repository

## Set up

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env               # then put your own values in .env
```

## Run

```bash
python hello.py Riya               # Hello, Riya!
python show_config.py              # reads .env; never prints the secret itself
python check_setup.py              # 6/6 checks passed (exit code 0)
```

## Test

```bash
pip install pytest
python -m pytest -q                # 26 passed
```

## What is not in git (on purpose)

| File | Why it stays out |
|---|---|
| `.env` | your settings and secrets; only `.env.example` (no real values) is committed |
| `.venv/` | big and machine-specific; rebuild it from `requirements.txt` |
| `__pycache__/` | files Python makes on its own |
