"""SQLite basics for memory: tables, ? parameters, users, transactions."""
import sqlite3

conn = sqlite3.connect(":memory:")           # a file path in real code
conn.execute("CREATE TABLE facts (id INTEGER PRIMARY KEY, "
             "user_id TEXT NOT NULL, text TEXT NOT NULL)")
with conn:                                   # one transaction
    conn.execute("INSERT INTO facts (user_id, text) VALUES (?, ?)",
                 ("anuj", "Name is Anuj"))
    conn.execute("INSERT INTO facts (user_id, text) VALUES (?, ?)",
                 ("riya", "Name is Riya"))

rows = conn.execute("SELECT id, text FROM facts WHERE user_id = ?",
                    ("anuj",)).fetchall()
print("anuj sees:", rows)

evil = "x' OR '1'='1"                        # an injection attempt
found = conn.execute("SELECT text FROM facts WHERE user_id = ?",
                     (evil,)).fetchall()
print("injection attempt finds:", found)

try:
    with conn:                               # all or nothing
        conn.execute("DELETE FROM facts WHERE user_id = ?", ("anuj",))
        raise RuntimeError("crash halfway")
except RuntimeError as exc:
    print("error:", exc)
count = conn.execute("SELECT count(*) FROM facts").fetchone()[0]
print("facts after the failed transaction:", count)

conn.execute("PRAGMA user_version = 1")      # your schema's version number
print("schema version:", conn.execute("PRAGMA user_version").fetchone()[0])
