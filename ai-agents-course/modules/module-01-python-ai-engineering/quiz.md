# Module 1 quiz with answers

Hinglish remake (2026-11-18): every lesson ends with practice questions and one or two quick checks;
the five module questions close lesson 7. Practice answers below were checked by running them.

## Lesson quick checks

**L1 Q1.** In an AI agent, who actually runs the tool? **Answer: your Python code.** The model only decides.

**L1 Q2.** Which command records the exact package versions of your venv?
**Answer:** `pip freeze > requirements.txt`. `pip install -r requirements.txt` rebuilds from the file.

**L2.** What does this print?
```python
message = {"role": "user", "content": "Hi"}
print(message.get("model", "unknown"))
```
A) `None` B) `unknown` C) a `KeyError` D) `model`
**Answer: B.** `.get()` returns the default when the key is missing; only `message["model"]` raises `KeyError`.

**L2 Q2.** `messages = ["a", "b", "c", "d"]`; what is `messages[1:3]`? **Answer:** `["b", "c"]`.

**L3.** Why is `def add(msg, history=[])` dangerous?
**Answer:** the default list is created once and shared by every call that uses it (one user's
messages leak into another's). Use `history=None` and create a new list inside.

**L3 Q2.** Which block of `try / except / else / finally` runs every time? **Answer:** `finally`.

**L4.** Which call turns the JSON text `'{"ok": true}'` into a Python dict?
A) `json.dumps(text)` B) `json.loads(text)` C) `dict(text)` D) `json.load(text)`
**Answer: B.** `loads` loads from a string; `dumps` goes the other way; `json.load` reads from an open file object.

**L4 Q2.** Where should a real API key live? **Answer:** an environment variable or a git-ignored `.env`.

**L5.** An API replies `429`. What does it mean, and what should your code do?
**Answer:** too many requests (rate limit). Wait, often for as long as the response says, then retry with backoff (Module 2).

**L5 Q2.** Three independent 2-second calls with `asyncio.gather`: about **2 s** (one by one: 6 s).

**L6 Q1.** `load_records` finds 1 valid and 4 invalid records. **Answer:** it returns the valid record and
a list of 4 problems; good records keep working.

**L6 Q2.** `frozen=True` on a dataclass: fields can't be changed after creation (it does not validate types).

## Practice answers

**Lesson 1**
1. Decide → act → observe → repeat (until done or a limit stops it).
2. With `max_steps=2` the loop runs two calculator steps (437, then 444) and never reaches "finish":
   `run_agent` returns `stopped: step limit reached`.
3. Example, booking a cab: goal "a cab to the station by 9:00"; decisions: which app, which car type,
   accept the price?; tools: maps (distance), the cab app's API (prices, booking), payments.
4. Fixes for an agent stuck calling the same search: a step limit (`max_steps`), and give the model the
   earlier results (the "observe" step) so it can see it already searched; also detect repeated
   identical tool calls and stop or change strategy.

**Lesson 2**
1. `print(f"Model: {model} | Tokens: {tokens:,}")` → `Model: model-small | Tokens: 1,500`.
2. Append a dict, then `for turn in conversation: if turn["role"] == "user": print(turn["content"])`
   (or a comprehension: `[t["content"] for t in conversation if t["role"] == "user"]`).
3. `{r["status"] for r in records}` → `{'ok', 'error'}` (a set comprehension).
4. Duplicates: `len(tools) - len(set(tools))`; unknown tools: `set(tools) - allowed`.
   For `["search", "calc", "search", "delete_files"]`: 1 duplicate, `{'delete_files'}`.

**Lesson 3**
1. `def word_count(text): return len(text.split())`.
2. `def clear(self): self.messages = self.messages[:1]` (keeps the system message).
3. ```python
   @dataclass
   class ToolCall:
       name: str
       args: dict[str, object] = field(default_factory=dict)
   ```
   `args={}` as a default is refused by dataclasses (mutable default).
4. Around each **tool call** inside the loop: catch the specific errors a tool can raise (for example
   `TimeoutError`, `httpx.HTTPError`, your own `ToolkitError`), turn them into a result message the model
   can see ("tool failed: ..."), and continue. Let unexpected errors (bugs) surface.

**Lesson 4**
1. Add `def char_count(text): return len(text)` to `cleaning.py`; import it in `__init__.py` and add it
   to `__all__`.
2. `Path("chat.json").write_text(json.dumps(messages, indent=2), encoding="utf-8")`, then
   `json.loads(Path("chat.json").read_text(encoding="utf-8"))`.
3. `int(os.environ.get("DEMO_MAX_TOKENS", "500"))`. Environment values are always strings; wrap it in
   `try/except ValueError` to report a bad value clearly.
4. Catch `json.JSONDecodeError`, log the message (line and column), and either ask the model again or
   return a clear error. Never let the exception crash the app.

**Lesson 5**
1. `def shorten(text: str, max_words: int = 8) -> str:`; `mypy` then reports wrong argument types.
2. `print(response.headers["content-length"])` (header names are case-insensitive in httpx).
3. Five 2-second tasks: one by one about 10 s; with `gather` about 2 s.
4. On 429: wait (use the `Retry-After` header if present), then retry with exponential backoff and a
   little random jitter, with a maximum number of attempts; never retry in a tight loop.

**Lesson 6**
1. `ValidationError: status: must be one of ['error', 'ok'], got 'done'`.
2. Add it to `ALLOWED_STATUS` in `toolkit/models.py`. The expected message in
   `tests/test_cli.py` (line 16) changes to include `'cancelled'`; `("status", "done")` in
   `tests/test_models.py` still fails as intended. Add a test that a `cancelled` record is accepted.
3. ```python
   @property
   def cost_per_request(self) -> float:
       return self.cost / self.requests if self.requests else 0.0
   ```
4. The 9,997 good records are summarised as usual, and the user sees 3 precise problem lines
   (record number, id, field and value). `--strict` turns any problem into a failure (exit code 1).

## Module quiz

1. An agent may only use `search` and `calculator`. Fastest "is this tool allowed?" check?
   A) list B) **set** C) string D) tuple
   *Set membership stays fast however many items it holds, and duplicates are impossible.*
2. What does `@dataclass(frozen=True)` add to `UsageRecord`?
   A) faster JSON parsing B) automatic type validation C) **fields can't change after creation** D) can't be printed
   *Dataclasses do not validate types. That is why `from_dict` checks every field.*
3. A command prints an error. How does a CI pipeline know it failed?
   A) it reads the text B) **a non-zero exit code** C) the file size D) it can't
   *Our `validate` returns 1 when any record is invalid.*
4. Why does `fetch_all` use `asyncio.gather`?
   **To download all URLs concurrently, so the total time is roughly the slowest download instead of the sum.**
   It saves waiting time; it does not add CPU power, and it does not retry.
5. Where should the real API key live?
   **In an environment variable or a git-ignored `.env` file.** `.env.example` holds only fake placeholders.

## Extension challenge (code + a test for each)

- `--top N` option for `report`.
- p95 latency (sort latencies, take the 95th-percentile value). Compare it with the 4,200 ms average.
- Per-day breakdown using `record.created_at.date()`.
- `--format csv` using the standard `csv` module.
