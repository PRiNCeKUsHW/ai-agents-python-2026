# Glossary

Every technical term used in the course, in plain words. The module where a term first appears is
in brackets. New terms are added with each module.

## Python and tools

| Term | Meaning |
|---|---|
| **async / await** [1] | A way to start several slow tasks (like web requests) and wait for them together instead of one after another. |
| **CLI** (command-line interface) [1] | A program you run by typing a command in the terminal, such as `python -m resume analyze ...`. |
| **dataclass** [1] | A Python class that mainly holds data; `@dataclass` writes the boring `__init__` code for you. |
| **dict** (dictionary) [1] | Python's key-to-value container: `{"name": "Sam", "years": 4}`. |
| **environment variable** [1] | A setting stored outside your code, read with `os.environ`. Used for API keys so they never appear in code. |
| **exception** [1] | Python's way of reporting an error. You `raise` one and `except` (catch) it. |
| **exit code** [1] | The number a program returns when it finishes: 0 means success, anything else means an error. |
| **f-string** [1] | A string with values inside: `f"Hello {name}"`. |
| **JSON** [1] | A text format for data that every language understands: `{"skills": ["Python"]}`. |
| **mypy** [1] | A tool that checks your type hints and finds type mistakes before you run the code. |
| **package / module** [1] | A module is one `.py` file; a package is a folder of modules with an `__init__.py`. |
| **pip** [1] | Python's package installer: `pip install -r requirements.txt`. |
| **pytest** [1] | The testing tool used in every project. A test is a function that `assert`s something is true. |
| **stdout / stderr** [1] | A program's two output streams: normal output, and messages or errors. |
| **terminal** [1] | The text window where you type commands (Terminal on macOS, PowerShell or Git Bash on Windows). |
| **type hint** [1] | A note about what type a value should be: `def add(a: int, b: int) -> int`. |
| **virtual environment (venv)** [1] | A private folder of packages for one project, so projects don't break each other. |

## Language models and the API

| Term | Meaning |
|---|---|
| **API** [2] | A way for programs to talk to a service. Your code sends a request to the Claude API and gets a response. |
| **API key** [2] | A secret password that identifies you to the API. Keep it in an environment variable; never commit it. |
| **context window** [2] | The most text (in tokens) a model can consider in one request, input and output together. |
| **cost per million tokens** [2] | How API usage is priced: separate prices for input and output tokens. |
| **effort** [2] | A setting (`low` to `max`) that controls how much the model reasons before answering. More effort, more tokens. |
| **fake API / offline mode** [2] | A local stand-in that speaks the same protocol as the real API, so code runs and tests pass without a key. Its replies are not real model output. |
| **hallucination** [2] | When a model states something false with confidence. Models produce plausible text, not looked-up facts. |
| **LLM** (large language model) [2] | A model trained on huge amounts of text that predicts the next token, over and over. |
| **max_tokens** [2] | The most tokens a reply may use. If it's reached, the reply is cut off. |
| **message history** [2] | The list of earlier messages your app sends with every request. The API itself remembers nothing. |
| **rate limit / 429** [2] | A cap on how many requests or tokens you may use per minute. Exceeding it returns error 429. |
| **refusal** [2] | When the model declines a request; the reply's `stop_reason` is `refusal`. |
| **retry with backoff** [2] | Trying a failed request again after a short wait that grows each time. The SDK does this for you. |
| **SDK** (software development kit) [2] | A library that makes an API easy to use from a language. Here: the `anthropic` Python package. |
| **stop_reason** [2] | Why the model stopped: finished (`end_turn`), hit the limit (`max_tokens`), declined (`refusal`), and others. |
| **streaming** [2] | Receiving the reply piece by piece as it's generated, instead of waiting for all of it. |
| **system prompt** [2] | Instructions that set the model's role, rules and style for the whole conversation. |
| **token** [2] | A chunk of text a model reads and writes: often a short word or part of a word. About 4 characters in English. |

## Prompts and structured output

| Term | Meaning |
|---|---|
| **eval** (evaluation) [3] | A set of labelled examples plus a grader that scores a prompt version, so changes can be compared with numbers. |
| **example (few-shot)** [3] | A sample input and output in the prompt that shows the model what you mean. Use a few varied ones. |
| **fingerprint** [3] | A short hash of a prompt's exact text. If one character changes, the fingerprint changes. |
| **grader** [3] | The code (or model) that decides whether an output is right. Prefer exact checks in code. |
| **grounding check** [3] | Verifying in code that the model's output is supported by the input, e.g. a skill really appears in the resume. |
| **prefill** [3] | Starting the assistant's reply for it. Current Claude models reject it; use structured outputs instead. |
| **prompt** [3] | Everything you send the model: context, task, data, constraints and examples. |
| **prompt injection** [3] | Text inside your data that tries to act as instructions ("ignore your rules..."). |
| **prompt versioning** [3] | Giving every prompt a version and never editing a released one, so results stay traceable. |
| **Pydantic** [3] | A Python library that defines data shapes (schemas) as classes and validates data against them. |
| **schema** [3] | A description of the shape data must have: which fields, which types, which limits. |
| **structured output** [3] | Asking the API to return JSON that matches your schema, e.g. `messages.parse(output_format=Model)`. |
| **task decomposition** [3] | Splitting a big task into steps: the model for judgment, plain code for everything deterministic. |
| **validation / ValidationError** [3] | Checking data against a schema; Pydantic raises `ValidationError` when it doesn't fit. |
| **XML tags** [3] | Markers like `<resume>...</resume>` that show the model exactly where data starts and ends. |

## Agents

| Term | Meaning |
|---|---|
| **agent** [4] | A program where the model decides the next step itself, in a loop, using tools, until the job is done. |
| **agent loop** [4] | Decide (the model picks an action), act (your code runs a tool), observe (the result goes back), repeat. |
| **allow-list** [4] | Listing exactly what is permitted and refusing everything else. Safer than listing what is forbidden. |
| **AST** (abstract syntax tree) [4] | Python's tree form of code. The calculator parses an expression into an AST and allows only arithmetic nodes. |
| **chatbot** [4] | One question, one answer. The human decides what happens next. |
| **dispatch** [4] | Choosing which function to run from a name, e.g. the model's tool name picks `calculate` or `convert`. |
| **eval()** [4] | Python's built-in that runs any text as code. Never use it on tool or user input. |
| **is_error** [4] | A flag on a `tool_result` saying the tool failed; the error message is the content. |
| **observation** [4] | What the agent learns from an action: a tool's result or error, sent back to the model. |
| **step limit (max steps)** [4] | The most turns an agent loop may take, so it always stops. |
| **tool** [4] | A function in your program that the model can ask you to run. The model only asks; your code runs it. |
| **tool definition** [4] | The description of a tool sent to the model: name, description and input schema. |
| **tool_result** [4] | The block your program sends back with a tool's output, matched to the request by `tool_use_id`. |
| **tool runner** [4] | An SDK helper that runs the agent loop for you. The course builds the loop by hand first. |
| **tool_use** [4] | A block in the model's reply that requests a tool call: a name, an input and an id. |
| **trace** [4] | A printout of every action an agent took and what it observed, used to understand and debug it. |
| **workflow** [4] | A program whose code runs fixed steps in a fixed order, some of them model calls. |

## Tools and safety

| Term | Meaning |
|---|---|
| **atomic save** [5] | Writing a temporary file, then replacing the real one in one step, so a crash never leaves half a file. |
| **business rule** [5] | A rule about your data that a schema can't express, e.g. "the due date isn't in the past" or "task 7 exists". |
| **daemon thread** [5] | A background thread that never stops the program from exiting. |
| **danger tool** [5] | A tool whose action can't be undone (delete, send, pay). A human must approve every call. |
| **decorator** [5] | A function that wraps another function; `@tool(...)` registers a function as a tool. |
| **human in the loop** [5] | A person approves (or declines) an agent's action before it runs. |
| **JSON Schema** [5] | A standard way to describe the shape of JSON data: fields, types, allowed values. |
| **least privilege** [5] | Give a program only the powers it needs for its job, and nothing more. |
| **parallel tool calls** [5] | One model reply that requests several tools; all results go back in one user message. |
| **permission level** [5] | How risky a tool is: read (always allowed), write (not in read-only mode), danger (needs approval). |
| **read-only mode** [5] | A mode where the agent may only use tools that look, never tools that change data. |
| **registry** [5] | One place that lists every tool once, so definitions and functions can't drift apart. |
| **strict tool use** [5] | `strict: true` on a tool: the model's input always matches the schema (shape and types). |
| **thread** [5] | A second worker inside the same program; used to run a tool while the main code watches the clock. |
| **timeout** [5] | The longest you'll wait for something before giving up with a clear error. |
| **validation** [5] | Checking input before using it; here with Pydantic's `model_validate`. |

## Memory and data

| Term | Meaning |
|---|---|
| **cascade (ON DELETE CASCADE)** [6] | A database rule: deleting a parent row (a session) also deletes its children (its messages). |
| **conversation history** [6] | The list of user and assistant messages your code resends with every request; the model keeps nothing itself. |
| **database / table / row / column** [6] | A database stores tables; a table is a set of rows; every row has the same columns (fields). |
| **foreign key** [6] | A column that must match a row in another table, e.g. each message belongs to a session. |
| **index (database)** [6] | A lookup structure that makes finding rows by a column (like `user_id`) fast. |
| **long-term memory** [6] | Facts saved outside the conversation (in a database) that survive restarts and new sessions. |
| **parameterised query** [6] | SQL with `?` (or `%s`) placeholders; values are sent separately, so they can never change the query. |
| **PostgreSQL** [6] | A database server many programs can share at once; the usual next step after SQLite. |
| **retention** [6] | A rule for how long data is kept before it's deleted, e.g. sessions unused for 30 days. |
| **running summary** [6] | A short summary of older turns, updated (not rewritten) each time more turns are folded in. |
| **schema version** [6] | A number stored with your data (`PRAGMA user_version`) that says which table layout it uses. |
| **session** [6] | One conversation (its turns and summary), saved and resumed by its id. |
| **short-term memory** [6] | What the model sees of the current conversation: recent turns, and maybe a summary. |
| **sliding window** [6] | Sending only the last N turns (or the newest turns that fit a token budget). |
| **SQL** [6] | The language for asking a database for data: `SELECT`, `INSERT`, `UPDATE`, `DELETE`. |
| **SQL injection** [6] | An attack where input pasted into SQL text changes the query; prevented by parameterised queries. |
| **SQLite** [6] | A full SQL database stored in one file, built into Python as `sqlite3`. |
| **stateless** [6] | Keeps nothing between requests. The Messages API is stateless: each request stands alone. |
| **summary memory** [6] | Folding older turns into a running summary so the conversation stays small. |
| **transaction** [6] | A group of database changes that happen all together or not at all. |
| **turn** [6] | One exchange that starts with the user's own words; it may include tool calls and results. |
| **upsert** [6] | Insert a row, or update it if it already exists (`INSERT ... ON CONFLICT DO UPDATE`). |
| **user isolation** [6] | Every row has a user id and every query filters by it, so users never see each other's data. |
