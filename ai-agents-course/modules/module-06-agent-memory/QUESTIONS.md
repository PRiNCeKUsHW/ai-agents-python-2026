# Module 6 question bank: Agent Memory and Conversation State

Every question asked in the Module 6 videos, with answers. **35 questions.**

How to use it: read the question, answer it out loud or on paper, *then* click **Show answer**. Getting one wrong is useful: rewatch that lesson's chapter.

Short answer key, practice answers and the extension challenge: [quiz.md](quiz.md) · Module guide: [README.md](README.md)

## Lesson 1: Why Agents Forget: Stateless APIs and Conversation History

### Quick check

**Your chatbot forgets what the user said two messages ago. What's the most likely bug?**

- A) The model's memory is full
- B) The code doesn't append replies and messages to the history it sends
- C) The API key expired
- D) max_tokens is too small

<details>
<summary>Show answer</summary>

**B) The code doesn't append replies and messages to the history it sends**

The API is stateless. If a message isn't in the list you send, the model never sees it.

</details>

### Pause and try: predict the reply

The history is `[user: "I love chess", assistant: "Nice!"]`. Your code then sends **only** `[user: "What do I love?"]`.

1. What can the model answer? Why? What would you change?

<details>
<summary>Show answer</summary>

It can't know. The request doesn't mention chess, and the API keeps nothing between calls. The fix: append every message to the history list, and send the whole list each time.

</details>

### Interview corner

**Interviewer:** Does the Claude API remember earlier messages?

<details>
<summary>Show answer</summary>

**A good answer:** No. The Messages API is **stateless**: each request stands alone. A conversation works because **your code** resends the history (user and assistant messages, in order) with every request.

**Trap to avoid:** Saying "the model remembers our chat". Any memory is data your code stores and sends.

</details>

**Interviewer:** Why can't you just keep the whole history forever?

<details>
<summary>Show answer</summary>

**A good answer:** Cost and limits. Every turn resends everything, so input tokens and **latency** grow with the conversation, and eventually it won't fit the **context window**. You need a strategy: windows, summaries, long-term facts.

**Trap to avoid:** Thinking that's only about money. Very long contexts also make replies slower.

</details>

## Lesson 2: Short-Term Memory: Context Windows and Sliding Windows

### Quick check

**A sliding window keeps the last 3 turns. What is the main risk?**

- A) The request becomes invalid
- B) Facts from early turns, like the user's name, are lost
- C) Costs grow every turn
- D) The model can't call tools any more

<details>
<summary>Show answer</summary>

**B) Facts from early turns, like the user's name, are lost**

A window bounds cost, but anything older than the window is gone. Lessons 3 and 4 fix that with summaries and long-term facts.

</details>

### Pause and try: pick the window

Messages: `0 user` · `1 assistant` · `2 user` · `3 assistant tool_use` · `4 user tool_result` · `5 assistant` · `6 user` · `7 assistant`.

1. Which messages does window(keep_turns=2) keep?

<details>
<summary>Show answer</summary>

Turns start at messages zero, two and six. Keeping two turns means starting at message two, so it keeps messages two to seven, and the tool use stays with its result.

</details>

### Interview corner

**Interviewer:** What is a context window, and how do you manage it in a long chat?

<details>
<summary>Show answer</summary>

**A good answer:** The most tokens a model can read in one request (system prompt, tools, messages, reply). Manage it with a **sliding window** of recent turns, **summaries** of older ones, and **long-term facts** fetched when needed.

**Trap to avoid:** Saying a big window means you never need to manage it: cost and latency grow long before the limit.

</details>

**Interviewer:** Why can't you just drop the oldest message?

<details>
<summary>Show answer</summary>

**A good answer:** Because messages come in linked groups. Dropping a `tool_use` but keeping its `tool_result` (or the reverse) makes the request **invalid**. Cut at **turn boundaries** instead.

**Trap to avoid:** Forgetting that tool results are sent with the user role.

</details>

## Lesson 3: Summary Memory: Compressing a Long Conversation

### Quick check

**Why does compact() drop the old messages only after the summary call returns?**

- A) It's faster
- B) If the call fails, no conversation is lost
- C) The API requires it
- D) So the summary includes the newest turn

<details>
<summary>Show answer</summary>

**B) If the call fails, no conversation is lost**

Summarize first, then drop. A failed or slow summary call must never lose the conversation.

</details>

### Pause and try: write the minutes

Old turns: *"I'm Riya. I'm preparing for a Python interview on Friday. Lists are fine, decorators confuse me. Can you quiz me tomorrow?"*

1. Write a summary of at most 25 words. What must it keep?

<details>
<summary>Show answer</summary>

One good summary: Riya, Python interview on Friday. Comfortable with lists, struggles with decorators. Promised: a quiz tomorrow. It keeps the fact, the goal, the struggle, and the promise.

</details>

### Interview corner

**Interviewer:** How would you keep a long-running chat within budget?

<details>
<summary>Show answer</summary>

**A good answer:** Keep the last few turns verbatim, fold older turns into a **running summary** with a dedicated prompt, and move durable facts to **long-term memory**. Summarize only when over a token threshold, and drop old turns only after the summary succeeds.

**Trap to avoid:** Summarizing on every turn: it adds a call each time and the summary drifts.

</details>

**Interviewer:** What can go wrong with summaries?

<details>
<summary>Show answer</summary>

**A good answer:** **Lost details** (exact numbers, code), **drift** as summaries of summaries pile up, and the extra **cost** and latency of the summary call. Mitigate with a clear keep-list, a length limit and long-term facts for what must be exact.

**Trap to avoid:** Treating a summary as a perfect record.

</details>

## Lesson 4: Long-Term Memory: Facts That Outlive a Conversation

### Quick check

**Where does the companion put long-term facts so the model can use them?**

- A) In the model's weights
- B) In the system prompt of each request
- C) In a hidden API setting
- D) In the user's last message

<details>
<summary>Show answer</summary>

**B) In the system prompt of each request**

The model learns nothing between calls. Relevant facts are read from the database and sent in the system prompt every time.

</details>

### Pause and try: what should be saved?

The learner says: *"Morning! Ugh, traffic was awful. I finished the decorators lesson, and I'd like shorter examples. My bank PIN is 4321, by the way."*

1. Which remember_fact calls should happen? With which topic?

<details>
<summary>Show answer</summary>

Two calls. The learner finished the decorators lesson, with topic progress. And the learner prefers shorter examples, topic preference. Not the traffic: it won't matter later. And never the PIN.

</details>

### Interview corner

**Interviewer:** How would you give an agent memory across sessions?

<details>
<summary>Show answer</summary>

**A good answer:** Store **durable facts** per user in a database. Let the model **save, recall and forget** them via tools, validate inputs and block secrets in code, and inject the **relevant** facts into the system prompt of each new conversation.

**Trap to avoid:** Saving every message forever and sending it all back: costly, slow and a privacy risk.

</details>

**Interviewer:** Who should decide what gets remembered: the model or your code?

<details>
<summary>Show answer</summary>

**A good answer:** Both. The **model** judges what's worth saving (via tool calls); **your code** enforces the rules: allowed topics, length, no secrets, per-user isolation, and deletion.

**Trap to avoid:** Trusting a prompt instruction alone to keep secrets out.

</details>

## Lesson 5: Saving Memory in SQLite: Sessions, Users, Retention and Deletion

### Quick check

**A transaction deletes a session's messages, then the program crashes before the block ends. What's in the database?**

- A) The messages are gone
- B) Half of the messages are gone
- C) Everything as before the transaction
- D) An empty database

<details>
<summary>Show answer</summary>

**C) Everything as before the transaction**

A transaction is all or nothing. If it doesn't finish, every change in it is rolled back.

</details>

### Pause and try: write the query

Table `sessions(user_id, id, updated)`. Find **riya's** sessions last used **before 2026-10-01**.

1. Write the SQL and the Python call. Where do the values go?

<details>
<summary>Show answer</summary>

conn dot execute, with: select id from sessions where user ID equals question mark and updated is less than question mark. Then a tuple: riya, and the date. The values go in the tuple, never in the SQL text. ISO dates compare correctly as text.

</details>

### Interview corner

**Interviewer:** What is SQL injection, and how do you prevent it?

<details>
<summary>Show answer</summary>

**A good answer:** Input that becomes part of the SQL text and changes the query. Prevent it with **parameterised queries** (`?` or `%s`): the driver sends values separately, so they're always data. Never format SQL with f-strings.

**Trap to avoid:** Escaping quotes by hand. Parameters are the fix.

</details>

**Interviewer:** How do you keep one user's memory away from another's?

<details>
<summary>Show answer</summary>

**A good answer:** Every table has a **user_id**, every query filters by it, and the user id comes from **authentication**, never from the model. Test it: user B can't read or delete user A's rows.

**Trap to avoid:** Letting the model pass the user id as a tool argument.

</details>

## Lesson 6: Project, Part 1: The Persistent AI Study Companion

### Quick check

**In the companion, which part decides that "I find recursion hard" is worth remembering?**

- A) db.py, when saving the session
- B) The model, by calling remember_fact
- C) The CLI, by parsing the message
- D) conversation.py, when summarizing

<details>
<summary>Show answer</summary>

**B) The model, by calling remember_fact**

The model judges what's worth saving and calls the tool. Your code then validates and stores it, or refuses it.

</details>

### Pause and try: trace the request

Tomorrow you run `python -m companion ask "What's my name?"` with **no** `--session`.

1. Which session is used? What's in the request? Can it answer?

<details>
<summary>Show answer</summary>

The session is tomorrow's date, so it's new and empty. But the system prompt still carries the long-term facts, including: the learner's name is Anuj. So yes, it answers Anuj. That's the difference between conversation memory and long-term memory.

</details>

### Interview corner

**Interviewer:** What's the difference between a session and long-term memory?

<details>
<summary>Show answer</summary>

**A good answer:** A **session** is one conversation: its turns and summary, resumable by id. **Long-term memory** is facts about the user shared by **all** sessions. New session: empty history, same facts.

**Trap to avoid:** Storing everything in one ever-growing conversation instead.

</details>

**Interviewer:** How do you test an agent's memory without paying for API calls?

<details>
<summary>Show answer</summary>

**A good answer:** Run the **real** agent, tools and database against a **fake API** with the same protocol, and a temporary database per test. Check the facts saved, the requests sent and the reloaded sessions.

**Trap to avoid:** Mocking the agent's own methods, so the real loop is never tested.

</details>

## Lesson 7: Project, Part 2: One Turn, a Two-Day Demo, Privacy, Tests and Wrap-up

### Module quiz

**Q1. Why does a chatbot "remember" earlier messages in a conversation?**

- A) The API stores the conversation
- B) The model learns during the chat
- C) Your code resends the history with each request
- D) The API key keeps a session

<details>
<summary>Show answer</summary>

**C) Your code resends the history with each request**

The Messages API is stateless. Memory within a chat is the history your code sends every time.

</details>

**Q2. Where must a sliding window cut the conversation?**

- A) Exactly N messages from the end
- B) Where a turn starts: a user message with plain text
- C) Before every assistant message
- D) Anywhere, the API fixes it

<details>
<summary>Show answer</summary>

**B) Where a turn starts: a user message with plain text**

Cutting at a turn start keeps each tool_use with its tool_result. Tool results are user messages, but don't start a turn.

</details>

**Q3. What is the main trade-off of summary memory?**

- A) It makes requests bigger
- B) Details can be lost, and it costs an extra call
- C) It can't be saved to disk
- D) It breaks tool calls

<details>
<summary>Show answer</summary>

**B) Details can be lost, and it costs an extra call**

A summary keeps the gist small, but exact details may be dropped, and summarizing is one more model call.

</details>

**Q4. The model calls remember_fact with a user's password. What should happen?**

- A) Save it encrypted
- B) Save it, the model decided
- C) Your code refuses it and returns a tool error
- D) Crash the agent

<details>
<summary>Show answer</summary>

**C) Your code refuses it and returns a tool error**

Prompts guide; code enforces. The memory layer refuses secrets and the model receives an error observation.

</details>

**Q5. Which query is safe from SQL injection?**

```python
a) conn.execute(f"SELECT * FROM facts WHERE user_id = '{u}'")
b) conn.execute("SELECT * FROM facts WHERE user_id = ?", (u,))
c) conn.execute("SELECT * FROM facts WHERE user_id = '" + u + "'")
d) conn.execute("SELECT * FROM facts WHERE user_id = '%s'" % u)
```

- A) a
- B) b
- C) c
- D) d

<details>
<summary>Show answer</summary>

**B) b**

Only b passes the value as a parameter. The others paste the value into the SQL text, so input can change the query.

</details>

### Practice questions

Easy to hard.

**1. Write window_by_tokens(messages, budget): recent turns up to a token budget**

<details>
<summary>Show answer</summary>

```python
def window_by_tokens(messages, budget):
    starts = [i for i, m in enumerate(messages) if is_turn_start(m)]
    for start in starts:                       # oldest first
        if estimate_tokens(messages[start:]) <= budget:
            return messages[start:]
    return messages[starts[-1]:] if starts else []   # at least the last turn
```
It still cuts only at turn starts, so tool pairs stay together.

</details>

**2. Which facts from "I'm Sam, I'm tired today, I passed my Python exam" should be saved?**

<details>
<summary>Show answer</summary>

save "The learner's name is Sam" (profile) and "The learner passed the Python exam"
(progress). "Tired today" won't be true tomorrow: don't save it.

</details>

**3. Write the SQL to count each user's messages**

<details>
<summary>Show answer</summary>

`SELECT user_id, count(*) FROM messages GROUP BY user_id ORDER BY user_id;`

</details>

**4. Scenario: a support bot remembers customers. Design its memory and privacy rules.**

<details>
<summary>Show answer</summary>

per-customer rows keyed by the authenticated customer id (never a
model argument); a window + running summary per ticket; long-term facts limited to useful,
expected ones (product owned, preferred language, open issues); refuse card numbers and passwords in
code; show customers what's stored; retention (e.g. close-ticket + 90 days); delete-my-data that
covers facts, tickets, messages and backups; isolation tests; audit who read what.

</details>

### Interview corner

**Interviewer:** Design memory for a tutoring agent used by thousands of students.

<details>
<summary>Show answer</summary>

**A good answer:** Per-student rows in **PostgreSQL**; a **window + running summary** per session; **long-term facts** saved via tools and injected by relevance; secrets refused in code; **retention** and **delete-my-data**; isolation tests; embeddings for recall at scale.

**Trap to avoid:** One giant shared history, or letting the model choose the user id.

</details>

**Interviewer:** A user asks you to delete their data. What must happen?

<details>
<summary>Show answer</summary>

**A good answer:** Delete their **facts, sessions and messages** (and backups and logs, per policy), confirm it, and make sure nothing reloads it. In code: one transaction filtered by user, cascades for children, and a test.

**Trap to avoid:** Deleting only the facts and forgetting stored conversations.

</details>
