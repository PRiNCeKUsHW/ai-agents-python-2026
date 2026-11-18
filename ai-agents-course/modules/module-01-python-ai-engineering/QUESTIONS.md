# Module 1 question bank: Python for AI Engineering

Every question asked in the Module 1 videos, with answers. **62 questions.**

How to use it: read the question, answer it out loud or on paper, *then* click **Show answer**. Getting one wrong is useful: rewatch that lesson's chapter.

The videos are narrated in Hinglish; the questions here are the English text shown on screen.

Short answer key, practice answers and the extension challenge: [quiz.md](quiz.md) · Module guide: [README.md](README.md)

## Lesson 1: Welcome, the Agent Loop, and Your Python Setup

### Module quiz

**Q1. In an AI agent, who actually runs the tool (for example, the calculator)?**

- A) The language model
- B) Your Python code
- C) The user
- D) The operating system, automatically

<details>
<summary>Show answer</summary>

**B) Your Python code**

The model only decides. Your code calls the tool and sends the result back.

</details>

**Q2. Which command records the exact package versions of your venv?**

- A) `pip list`
- B) `pip freeze > requirements.txt`
- C) `python -m venv .venv`
- D) `pip install -r requirements.txt`

<details>
<summary>Show answer</summary>

**B) `pip freeze > requirements.txt`**

`pip freeze` prints `name==version` lines; redirecting them makes `requirements.txt`. `install -r` is the other direction: it rebuilds from the file.

</details>

### Try these before the next lesson

Easy to hard.

**1. Name the four steps of the agent loop, in order**

**2. Set `max_steps=2` in `agent_loop.py`. What is printed, and why?**

**3. Pick a daily task (e.g. booking a cab) and list the goal, the decisions and the tools an agent would need**

**4. Scenario: an agent keeps calling the same search tool forever. Give two fixes.**

_Answers: see [quiz.md](quiz.md)._

### Interview corner

**Interviewer:** What is the difference between a chatbot and an AI agent?

<details>
<summary>Show answer</summary>

**A good answer:** A chatbot answers a message with text. An **agent** works towards a goal in a **loop**: the model decides the next step, the program runs a tool, and the result goes back to the model, until the goal is met or a limit stops it.

**Trap to avoid:** Saying "an agent is a smarter model". The model can be the same; the loop and the tools make it an agent.

</details>

**Interviewer:** Does the language model run the tools itself?

<details>
<summary>Show answer</summary>

**A good answer:** No. The model only returns a **decision** (text or a structured tool request). **Your code** validates it and runs the tool, then sends the result back.

**Trap to avoid:** Trusting the model's request blindly. Your code is where permissions and checks live.

</details>

**Interviewer:** Why does every agent loop need a step limit?

<details>
<summary>Show answer</summary>

**A good answer:** A model can repeat itself or never say "finish". A **max-steps** limit (and often a time or cost limit) stops runaway loops and runaway API bills.

**Trap to avoid:** Writing `while True:` around model calls.

</details>

## Lesson 2: Python Core Data: Variables, Lists, Dictionaries and Sets

### Module quiz

**Q1. What does this code print?**

```python
message = {"role": "user", "content": "Hi"}
print(message.get("model", "unknown"))
```

- A) `None`
- B) `unknown`
- C) A `KeyError`
- D) `model`

<details>
<summary>Show answer</summary>

**B) `unknown`**

`.get()` returns the default, `"unknown"`, when the key is missing. Only `message["model"]` would raise a `KeyError`.

</details>

**Q2. `messages = ["a", "b", "c", "d"]`. What is `messages[1:3]`?**

- A) `["a", "b", "c"]`
- B) `["b", "c"]`
- C) `["b", "c", "d"]`
- D) `["c", "d"]`

<details>
<summary>Show answer</summary>

**B) `["b", "c"]`**

A slice starts at index 1 (`"b"`) and **stops before** index 3, so it's `["b", "c"]`.

</details>

### Try these before the next lesson

Easy to hard.

**1. Print `Model: model-small | Tokens: 1,500` with one f-string**

**2. Add a 4th message to `conversation` in `dicts.py` and print only the `user` messages**

**3. From the `records` list, build a set of all statuses**

**4. Scenario: a tool list has duplicates and an unknown tool. Find both with sets.**

_Answers: see [quiz.md](quiz.md)._

### Interview corner

**Interviewer:** What is the difference between a list and a tuple?

<details>
<summary>Show answer</summary>

**A good answer:** A **list** is mutable: you can append, remove and change items. A **tuple** is immutable: once made, it can't change. Tuples can be dictionary keys and set items; lists can't.

**Trap to avoid:** Saying tuples are "faster lists". The real difference is mutability, and what that allows.

</details>

**Interviewer:** `d["k"]` or `d.get("k")`: which one, and when?

<details>
<summary>Show answer</summary>

**A good answer:** Use `d["k"]` when the key **must** exist: a missing key is a bug, and the `KeyError` says so. Use `d.get("k", default)` when the key is **optional**.

**Trap to avoid:** Using `.get()` everywhere, which hides real bugs behind `None`.

</details>

**Interviewer:** Why is checking `x in my_set` faster than `x in my_list`?

<details>
<summary>Show answer</summary>

**A good answer:** A set uses hashing, so a membership check takes about the same time however big it is. A list is checked **item by item**, so it gets slower as it grows.

**Trap to avoid:** Converting a list to a set inside a loop, every time: the conversion itself is the slow part.

</details>

## Lesson 3: Functions, Classes and Exceptions

### Module quiz

**Q1. Why is `def add(msg, history=[])` dangerous?**

- A) Lists can't be parameters
- B) The same list is shared by every call that uses the default
- C) It makes the function slow
- D) `history` becomes read-only

<details>
<summary>Show answer</summary>

**B) The same list is shared by every call that uses the default**

Default values are created **once**, when the function is defined. Use `history=None` and create a new list inside.

</details>

**Q2. In `try / except / else / finally`, which block runs **every** time?**

- A) `try`
- B) `except`
- C) `else`
- D) `finally`

<details>
<summary>Show answer</summary>

**D) `finally`**

`finally` runs whether the `try` succeeded or failed. `else` runs only on success; `except` only on a matching error.

</details>

### Try these before the next lesson

Easy to hard.

**1. Write `word_count(text)` that returns the number of words**

**2. Add a `clear()` method to `Conversation` that keeps only the system message**

**3. Make a `@dataclass` called `ToolCall` with `name: str` and `args: dict`**

**4. Scenario: an agent crashes on one bad tool result and loses the whole run. Where would you add `try`/`except`, and what would you catch?**

_Answers: see [quiz.md](quiz.md)._

### Interview corner

**Interviewer:** What is `self` in a Python method?

<details>
<summary>Show answer</summary>

**A good answer:** The object the method was called on. `chat.add(...)` runs `Conversation.add(chat, ...)`, so `self` is `chat`. It lets each object keep its **own** data.

**Trap to avoid:** Thinking `self` is a keyword. It's just the conventional name of the first parameter.

</details>

**Interviewer:** What's wrong with `def f(items=[])`?

<details>
<summary>Show answer</summary>

**A good answer:** The default list is created **once** and shared by every call that uses it, so data leaks between calls. Use `items=None` and create a new list inside (or `field(default_factory=list)` in a dataclass).

**Trap to avoid:** Fixing it with `items=list()`. That's still evaluated once.

</details>

**Interviewer:** When should you write a bare `except:`?

<details>
<summary>Show answer</summary>

**A good answer:** Almost never. Catch the **specific** exceptions you can handle. If you must catch broadly (for example at the top of a server), catch `Exception`, **log** it, and don't hide it.

**Trap to avoid:** `except: pass`: it also swallows `KeyboardInterrupt` and your own bugs.

</details>

## Lesson 4: Modules, Packages, Files, JSON and Environment Variables

### Module quiz

**Q1. Which call turns the JSON text `'{"ok": true}'` into a Python dictionary?**

- A) `json.dumps(text)`
- B) `json.loads(text)`
- C) `dict(text)`
- D) `json.load(text)`

<details>
<summary>Show answer</summary>

**B) `json.loads(text)`**

`loads` = load from a **string**. `dumps` goes the other way. `json.load` (no s) reads from an open **file** object, not a string.

</details>

**Q2. Where should a real API key live?**

- A) In `config.py`, committed to git
- B) In `.env.example`
- C) In an environment variable (or a git-ignored `.env`)
- D) In a code comment, so teammates can find it

<details>
<summary>Show answer</summary>

**C) In an environment variable (or a git-ignored `.env`)**

Real keys go in the environment or a git-ignored `.env`. `.env.example` is committed, so it holds only fake placeholders.

</details>

### Try these before the next lesson

Easy to hard.

**1. Add `char_count(text)` to `textkit` and export it in `__init__.py`**

**2. Save a list of 3 messages to `chat.json` and load it back**

**3. Read `DEMO_MAX_TOKENS` as an **int**, default 500**

**4. Scenario: a model returns JSON with a trailing comma. What does your code do so the app doesn't crash?**

_Answers: see [quiz.md](quiz.md)._

### Interview corner

**Interviewer:** What is the difference between a module and a package?

<details>
<summary>Show answer</summary>

**A good answer:** A **module** is one `.py` file. A **package** is a folder of modules, usually with an `__init__.py`, imported by its folder name.

**Trap to avoid:** Running a package's file directly (`python textkit/cleaning.py`) and wondering why its imports break. Use `python -m`.

</details>

**Interviewer:** `json.load` vs `json.loads`?

<details>
<summary>Show answer</summary>

**A good answer:** `loads` parses a **string**; `load` reads from an open **file** object. Same pair for writing: `dumps` returns a string, `dump` writes to a file.

**Trap to avoid:** Passing a file path string to `json.load`. It needs an open file, not a path.

</details>

**Interviewer:** An API key was committed to git. Is deleting the line enough?

<details>
<summary>Show answer</summary>

**A good answer:** No. It stays in the git **history**, and may already be copied. **Revoke** the key, create a new one, and keep it in an environment variable or `.env` that is git-ignored.

**Trap to avoid:** Only rewriting history. The key must be treated as leaked.

</details>

## Lesson 5: Type Hints, HTTP Requests and Async

### Module quiz

**Q1. An API replies with status `429`. What does it mean, and what should your code do?**

- A) The URL is wrong: fix it
- B) Too many requests: wait, then retry
- C) Success: read the body
- D) The server crashed: give up

<details>
<summary>Show answer</summary>

**B) Too many requests: wait, then retry**

429 means you hit a **rate limit**. Wait (often the response says how long), then retry. Module 2 implements this with backoff.

</details>

**Q2. Three independent calls each take 2 seconds. About how long does `asyncio.gather` take?**

- A) 6 seconds
- B) About 2 seconds
- C) 0 seconds
- D) It depends on the CPU speed

<details>
<summary>Show answer</summary>

**B) About 2 seconds**

They wait **together**, so the total is about the slowest one: ~2 s. One by one would be 6 s.

</details>

### Try these before the next lesson

Easy to hard.

**1. Add type hints to `shorten(text, max_words=8)` from lesson 3 and run mypy**

**2. In `http_demo.py`, print the response's `content-length` header**

**3. Change `async_demo.py` to 5 tasks of 2 s each. Predict both times first.**

**4. Scenario: an agent calls a model API and sometimes gets 429. Describe a safe retry plan.**

_Answers: see [quiz.md](quiz.md)._

### Interview corner

**Interviewer:** Does Python enforce type hints at runtime?

<details>
<summary>Show answer</summary>

**A good answer:** No. Hints are for **tools** (mypy, your editor) and for readers. Libraries like **Pydantic** read them to validate data at runtime, but plain Python ignores them.

**Trap to avoid:** Saying hints make code faster or safer by themselves.

</details>

**Interviewer:** Which HTTP errors should you retry?

<details>
<summary>Show answer</summary>

**A good answer:** **429** (after waiting) and **5xx** (temporary server problems), plus timeouts, with backoff and a limit. **4xx** like 400/401/404 mean your request is wrong: retrying won't help.

**Trap to avoid:** Retrying everything in a tight loop, which makes rate limits worse.

</details>

**Interviewer:** Async vs threads vs processes: when is async the right choice?

<details>
<summary>Show answer</summary>

**A good answer:** For **I/O-bound** work: many network or disk waits at once (model calls, API requests). For **CPU-heavy** work, async doesn't help; use processes.

**Trap to avoid:** Calling a blocking function (like `time.sleep` or `httpx.get`) inside `async def`: it blocks every other task.

</details>

## Lesson 6: Project, Part 1: Plan, Data Model and Validation

### Module quiz

**Q1. `load_records` finds 1 valid and 4 invalid records. What does it do?**

- A) Raises an error at the first invalid record
- B) Returns the valid record and a list of 4 problems
- C) Skips the bad records silently
- D) Fixes the bad records automatically

<details>
<summary>Show answer</summary>

**B) Returns the valid record and a list of 4 problems**

It returns `(records, problems)`: good records keep working, and every problem is reported with its record number.

</details>

**Q2. What does `frozen=True` on a dataclass do?**

- A) Makes the class faster
- B) Stops anyone from changing an object's fields after it's created
- C) Saves the object to disk
- D) Validates the field types

<details>
<summary>Show answer</summary>

**B) Stops anyone from changing an object's fields after it's created**

Assigning to a field of a frozen dataclass raises `FrozenInstanceError`. It doesn't validate types: that's `from_dict`'s job.

</details>

### Try these before the next lesson

Easy to hard.

**1. In the REPL, make a record with `status: "done"`. Read the message.**

**2. Add `"cancelled"` to the allowed statuses. Which tests should change?**

**3. Add `cost_per_request` (cost ÷ requests) to `Summary` as a property, safe for zero requests**

**4. Scenario: a log has 10,000 records and 3 are broken. What should the user see?**

_Answers: see [quiz.md](quiz.md)._

### Interview corner

**Interviewer:** Why validate data at the edge instead of everywhere?

<details>
<summary>Show answer</summary>

**A good answer:** One place checks raw input and turns it into a **trusted type** (`UsageRecord`). The rest of the code can rely on it, so checks aren't duplicated and bugs show up **where the bad data enters**.

**Trap to avoid:** Sprinkling `if x is None` checks all over the code instead.

</details>

**Interviewer:** What is `@classmethod` used for here?

<details>
<summary>Show answer</summary>

**A good answer:** An **alternative constructor**: `UsageRecord.from_dict(raw)` builds and validates a record from a dictionary. It gets the class as `cls`, so it also works for subclasses.

**Trap to avoid:** Putting all validation in `__init__` of a frozen dataclass, which makes simple construction in tests awkward.

</details>

**Interviewer:** Why is `isinstance(True, int)` a problem in validation?

<details>
<summary>Show answer</summary>

**A good answer:** `bool` is a subclass of `int`, so `True` passes an `int` check. A field like `prompt_tokens: true` would be accepted as **1** unless you reject `bool` explicitly.

**Trap to avoid:** Assuming JSON `true` can never reach a number field.

</details>

## Lesson 7: Project, Part 2: Reports, CLI, Tests and Wrap-up

### Module quiz

**Q1. An agent may only use the tools `search` and `calculator`. Which structure gives the fastest "is this tool allowed?" check?**

- A) A list
- B) A set
- C) A string
- D) A tuple

<details>
<summary>Show answer</summary>

**B) A set**

Membership checks on a **set** are fast however many items it holds, and duplicates are impossible.

</details>

**Q2. What does `@dataclass(frozen=True)` add to `UsageRecord`?**

- A) Faster JSON parsing
- B) Automatic validation of types
- C) Fields can't be changed after creation
- D) It can't be printed

<details>
<summary>Show answer</summary>

**C) Fields can't be changed after creation**

Frozen dataclasses raise an error if you assign to a field after creation. Note: a dataclass does **not** validate types; that's why `from_dict` checks them.

</details>

**Q3. A command prints an error. How does a CI pipeline know it failed?**

- A) It reads the printed text
- B) From a non-zero exit code
- C) From the file size
- D) It can't know

<details>
<summary>Show answer</summary>

**B) From a non-zero exit code**

Programs signal failure with a non-zero exit code. Our `validate` returns 1 when any record is invalid.

</details>

**Q4. Why does `fetch_all` use `asyncio.gather`?**

- A) To retry failed downloads
- B) To download all URLs concurrently, so total time ≈ the slowest one
- C) To use more CPU cores
- D) Because `httpx` requires it

<details>
<summary>Show answer</summary>

**B) To download all URLs concurrently, so total time ≈ the slowest one**

`gather` waits for all downloads at once. It saves waiting time; it doesn't add CPU power.

</details>

**Q5. Where should the real API key for your project live?**

- A) In `config.py`
- B) In `.env.example`
- C) In an environment variable or a git-ignored `.env`
- D) In the README

<details>
<summary>Show answer</summary>

**C) In an environment variable or a git-ignored `.env`**

Secrets live in environment variables (or a `.env` that is in `.gitignore`). `.env.example` holds only fake placeholder values.

</details>

### Interview corner

**Interviewer:** Why should a CLI return exit codes instead of only printing errors?

<details>
<summary>Show answer</summary>

**A good answer:** Scripts, CI and other programs can't read your sentences, but they can read the exit code: **0** success, non-zero failure. `&&` and CI steps stop on failure because of it.

**Trap to avoid:** Printing "Error!" and still exiting with 0, so the pipeline happily continues.

</details>

**Interviewer:** How do you test code that makes HTTP requests?

<details>
<summary>Show answer</summary>

**A good answer:** Replace the network with a fake: `httpx.MockTransport` (or a fake client) returns prepared responses, including errors like 404. Tests become **fast and repeatable**, with no real server.

**Trap to avoid:** Tests that call a real API: slow, flaky, and they can spend money or leak keys.

</details>

**Interviewer:** Why separate calculating (`stats`) from formatting (`report`)?

<details>
<summary>Show answer</summary>

**A good answer:** Each part can be tested alone, and you can add a new output (JSON, CSV, a web page) without touching the maths. It's the **single responsibility** idea.

**Trap to avoid:** One giant function that loads, calculates and prints: impossible to test or reuse.

</details>
