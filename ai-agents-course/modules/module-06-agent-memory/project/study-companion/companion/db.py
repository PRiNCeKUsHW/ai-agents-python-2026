"""Everything the companion remembers, in one SQLite database file.

Three tables: facts (long-term memory), sessions (one row per conversation,
with its running summary) and messages (the conversation, turn by turn).
Every row belongs to a user, and every query filters by user_id: that is
user isolation. SQL values are always passed as ? parameters, never pasted
into the SQL text, so input can't change the query (SQL injection).
"""
import json
import sqlite3
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from companion.errors import AgentError

SCHEMA_VERSION = 1
SCHEMA = """
CREATE TABLE IF NOT EXISTS facts (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    text    TEXT NOT NULL,
    topic   TEXT NOT NULL,
    saved   TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS sessions (
    user_id TEXT NOT NULL,
    id      TEXT NOT NULL,
    summary TEXT NOT NULL DEFAULT '',
    updated TEXT NOT NULL,
    PRIMARY KEY (user_id, id)
);
CREATE TABLE IF NOT EXISTS messages (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    TEXT NOT NULL,
    session_id TEXT NOT NULL,
    role       TEXT NOT NULL,
    content    TEXT NOT NULL,                 -- JSON: a string or a block list
    FOREIGN KEY (user_id, session_id) REFERENCES sessions (user_id, id)
        ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS facts_user ON facts (user_id);
CREATE INDEX IF NOT EXISTS messages_session ON messages (user_id, session_id);
"""


class Database:
    def __init__(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        version = self.conn.execute("PRAGMA user_version").fetchone()[0]
        if version > SCHEMA_VERSION:
            raise AgentError(f"{path} was made by a newer version (schema "
                             f"{version}); this program reads {SCHEMA_VERSION}")
        with self.conn:                         # one transaction
            self.conn.executescript(SCHEMA)
            self.conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")

    def close(self) -> None:
        self.conn.close()

    def query(self, sql: str, *args: Any) -> list[sqlite3.Row]:
        return self.conn.execute(sql, args).fetchall()

    def write(self, sql: str, *args: Any) -> int:
        """Run one change in its own transaction; returns the new row id."""
        with self.conn:                         # commit, or roll back on error
            return self.conn.execute(sql, args).lastrowid or 0

    # ------------------------------------------------------------ sessions
    def load_session(self, user: str, session: str
                     ) -> tuple[str, list[dict[str, Any]]]:
        """The session's summary and messages; empty if it's new."""
        row = self.query("SELECT summary FROM sessions WHERE user_id = ? "
                         "AND id = ?", user, session)
        messages = [{"role": r["role"], "content": json.loads(r["content"])}
                    for r in self.query(
                        "SELECT role, content FROM messages WHERE user_id = ? "
                        "AND session_id = ? ORDER BY id", user, session)]
        return (row[0]["summary"] if row else ""), messages

    def save_session(self, user: str, session: str, summary: str,
                     messages: list[dict[str, Any]], today: date) -> None:
        """Replace the session's summary and messages in ONE transaction."""
        with self.conn:
            self.conn.execute(
                "INSERT INTO sessions (user_id, id, summary, updated) "
                "VALUES (?, ?, ?, ?) ON CONFLICT (user_id, id) DO UPDATE SET "
                "summary = excluded.summary, updated = excluded.updated",
                (user, session, summary, today.isoformat()))
            self.conn.execute("DELETE FROM messages WHERE user_id = ? AND "
                              "session_id = ?", (user, session))
            self.conn.executemany(
                "INSERT INTO messages (user_id, session_id, role, content) "
                "VALUES (?, ?, ?, ?)",
                [(user, session, m["role"], json.dumps(m["content"]))
                 for m in messages])

    def sessions(self, user: str) -> list[sqlite3.Row]:
        return self.query(
            "SELECT s.id, s.updated, length(s.summary) > 0 AS summarized, "
            "count(m.id) AS messages FROM sessions s LEFT JOIN messages m "
            "ON m.user_id = s.user_id AND m.session_id = s.id "
            "WHERE s.user_id = ? GROUP BY s.id ORDER BY s.updated, s.id", user)

    # ------------------------------------------------------------ privacy
    def purge(self, user: str, days: int, today: date) -> int:
        """Retention: delete sessions not used for `days` days."""
        cutoff = (today - timedelta(days=days)).isoformat()
        with self.conn:
            cur = self.conn.execute("DELETE FROM sessions WHERE user_id = ? "
                                    "AND updated < ?", (user, cutoff))
        return cur.rowcount

    def delete_user(self, user: str) -> tuple[int, int]:
        """Deletion: every fact and session of one user, nobody else's."""
        with self.conn:
            facts = self.conn.execute("DELETE FROM facts WHERE user_id = ?",
                                      (user,)).rowcount
            sessions = self.conn.execute("DELETE FROM sessions WHERE "
                                         "user_id = ?", (user,)).rowcount
        return facts, sessions
