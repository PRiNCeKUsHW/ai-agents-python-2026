# Module 6 quiz with answers

## Lesson quick checks

**L1.** Your chatbot forgets what the user said two messages ago. Most likely bug?
**Answer:** the code doesn't append every message (and reply) to the history it sends. The API is
stateless.

**L2.** A sliding window keeps the last 3 turns. Main risk?
**Answer:** facts from early turns, like the user's name, are lost.

**L3.** Why does `compact()` drop old messages only after the summary call returns?
**Answer:** if the call fails, no conversation is lost.

**L4.** Where does the companion put long-term facts so the model can use them?
**Answer:** in the system prompt of each request. The model learns nothing between calls.

**L5.** A transaction deletes messages, then the program crashes before the block ends. What's stored?
**Answer:** everything as before the transaction (all or nothing).

**L6.** Which part decides that "I find recursion hard" is worth remembering?
**Answer:** the model, by calling `remember_fact`; your code validates and stores it, or refuses it.

## Pause-and-try answers

- **L1, predict the reply:** it can't know: the request doesn't mention chess. Append every message to
  the history and send the whole list.
- **L2, pick the window:** turns start at messages 0, 2 and 6; two turns start at message 2, so it keeps
  messages 2-7 and the tool_use (3) stays with its tool_result (4).
- **L3, write the minutes:** "Riya, Python interview Friday. Fine with lists, struggles with decorators.
  Promised: a quiz tomorrow." (fact, goal, struggle, promise).
- **L4, what should be saved:** `remember_fact("The learner finished the decorators lesson", "progress")`
  and `remember_fact("The learner prefers shorter examples", "preference")`. Not the traffic; never the
  PIN.
- **L5, write the query:**
  `conn.execute("SELECT id FROM sessions WHERE user_id = ? AND updated < ?", ("riya", "2026-10-01"))`.
  ISO dates compare correctly as text.
- **L6, trace the request:** the session is tomorrow's date (new, empty), but the system prompt still
  carries the fact "The learner's name is Anuj", so it answers Anuj.

## Module quiz

1. Why does a chatbot remember earlier messages? **Your code resends the history with each request.**
2. Where must a sliding window cut? **Where a turn starts: a user message with plain text** (tool
   results are user messages but don't start a turn).
3. Main trade-off of summary memory? **Details can be lost, and it costs an extra call.**
4. The model calls `remember_fact` with a password. **Your code refuses it and returns a tool error.**
5. Which query is safe from SQL injection? **b**, the parameterised one (`?` with a tuple).

## Practice questions (lesson 7)

1. **`window_by_tokens`:**
   ```python
   def window_by_tokens(messages, budget):
       starts = [i for i, m in enumerate(messages) if is_turn_start(m)]
       for start in starts:                       # oldest first
           if estimate_tokens(messages[start:]) <= budget:
               return messages[start:]
       return messages[starts[-1]:] if starts else []   # at least the last turn
   ```
   It still cuts only at turn starts, so tool pairs stay together.
2. **Sam:** save "The learner's name is Sam" (profile) and "The learner passed the Python exam"
   (progress). "Tired today" won't be true tomorrow: don't save it.
3. **Count each user's messages:**
   `SELECT user_id, count(*) FROM messages GROUP BY user_id ORDER BY user_id;`
4. **Scenario, support bot memory:** per-customer rows keyed by the authenticated customer id (never a
   model argument); a window + running summary per ticket; long-term facts limited to useful,
   expected ones (product owned, preferred language, open issues); refuse card numbers and passwords in
   code; show customers what's stored; retention (e.g. close-ticket + 90 days); delete-my-data that
   covers facts, tickets, messages and backups; isolation tests; audit who read what.

## Extension challenge (code + a test using the fake API)

- Add `export` and `import` commands: your facts and sessions as a JSON file.
- Make facts expire: for example "struggle" facts older than 60 days.
- Size the window by tokens instead of turns (practice 1), and use it in `compact()`.
- Swap SQLite for PostgreSQL with psycopg (`%s` placeholders), keeping the same tests.
