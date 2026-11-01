import sqlite3
from datetime import date

import pytest

from companion.db import SCHEMA_VERSION, Database
from companion.errors import AgentError
from companion.memory import LongTermMemory

MESSAGES = [{"role": "user", "content": "hi"},
            {"role": "assistant", "content": [{"type": "text", "text": "hello"}]}]


def test_sessions_round_trip_and_replace(db):
    db.save_session("anuj", "mon", "", MESSAGES, date(2026, 11, 2))
    assert db.load_session("anuj", "mon") == ("", MESSAGES)
    db.save_session("anuj", "mon", "a summary", MESSAGES[1:], date(2026, 11, 3))
    assert db.load_session("anuj", "mon") == ("a summary", MESSAGES[1:])
    rows = db.sessions("anuj")
    assert [(r["id"], r["updated"], r["messages"], r["summarized"]) for r in rows] \
        == [("mon", "2026-11-03", 1, 1)]


def test_new_session_is_empty_and_users_are_isolated(db):
    db.save_session("anuj", "mon", "s", MESSAGES, date(2026, 11, 2))
    assert db.load_session("riya", "mon") == ("", [])
    assert db.sessions("riya") == []


def test_data_survives_a_new_connection(tmp_path):
    first = Database(tmp_path / "c.db")
    LongTermMemory(first, "anuj", date(2026, 11, 2)).remember("Name is Anuj", "profile")
    first.save_session("anuj", "mon", "", MESSAGES, date(2026, 11, 2))
    first.close()
    second = Database(tmp_path / "c.db")                 # like the next day
    assert LongTermMemory(second, "anuj", date(2026, 11, 3)).facts()[0].text == "Name is Anuj"
    assert second.load_session("anuj", "mon")[1] == MESSAGES
    second.close()


def test_sql_input_is_data_not_code(db, memory):
    memory.remember("x'); DROP TABLE facts; --", "profile")
    assert memory.facts()[0].text.startswith("x');")       # stored as text
    assert db.query("SELECT count(*) FROM facts")[0][0] == 1


def test_purge_deletes_old_sessions_and_their_messages(db):
    db.save_session("anuj", "old", "", MESSAGES, date(2026, 9, 1))
    db.save_session("anuj", "new", "", MESSAGES, date(2026, 11, 1))
    db.save_session("riya", "old", "", MESSAGES, date(2026, 9, 1))
    assert db.purge("anuj", 30, date(2026, 11, 2)) == 1
    assert [r["id"] for r in db.sessions("anuj")] == ["new"]
    assert db.load_session("anuj", "old") == ("", [])        # messages gone too
    assert len(db.sessions("riya")) == 1                       # other users untouched


def test_delete_user_removes_everything_of_one_user(db, memory):
    memory.remember("Fact", "profile")
    db.save_session("anuj", "mon", "", MESSAGES, date(2026, 11, 2))
    db.save_session("riya", "mon", "", MESSAGES, date(2026, 11, 2))
    assert db.delete_user("anuj") == (1, 1)
    assert db.query("SELECT count(*) FROM messages WHERE user_id = 'anuj'")[0][0] == 0
    assert len(db.sessions("riya")) == 1


def test_newer_schema_is_rejected(tmp_path):
    path = tmp_path / "c.db"
    conn = sqlite3.connect(path)
    conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION + 1}")
    conn.close()
    with pytest.raises(AgentError, match="newer version"):
        Database(path)
