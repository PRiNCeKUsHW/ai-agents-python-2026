import sys
from dataclasses import replace
from datetime import date
from pathlib import Path

import pytest

PROJECT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT))

from companion.agent import StudyCompanion  # noqa: E402
from companion.client import make_client  # noqa: E402
from companion.config import Settings  # noqa: E402
from companion.db import Database  # noqa: E402
from companion.fake_api import FakeAnthropicAPI  # noqa: E402
from companion.memory import LongTermMemory  # noqa: E402
from companion.pricing import CostTracker  # noqa: E402

TODAY = date(2026, 11, 2)


@pytest.fixture(autouse=True)
def no_real_api(monkeypatch):
    """Tests never touch the network, a real key, or the user's data."""
    for name in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL",
                 "COMP_MODEL", "COMP_BUDGET_USD", "COMP_MAX_RETRIES", "COMP_MAX_STEPS",
                 "COMP_HOME", "COMP_KEEP_TURNS", "COMP_SUMMARIZE_AT", "COMP_TODAY",
                 "COMP_USER", "COMP_FAKE_FAIL"):
        monkeypatch.delenv(name, raising=False)


@pytest.fixture
def db(tmp_path):
    database = Database(tmp_path / "companion.db")
    yield database
    database.close()


@pytest.fixture
def memory(db):
    return LongTermMemory(db, "anuj", TODAY)


def settings(tmp_path: Path, **changes) -> Settings:
    base = Settings(model="claude-opus-5-5", offline=True, budget_usd=1.0,
                    max_retries=0, max_steps=6, home=tmp_path, keep_turns=2,
                    summarize_at=100_000, today=TODAY)
    return replace(base, **changes)


def make_companion(db: Database, fake: FakeAnthropicAPI, user: str = "anuj",
                   session: str = "s1", **changes) -> StudyCompanion:
    s = settings(db.path.parent, **changes)
    return StudyCompanion(make_client(s, fake), s, CostTracker(s.budget_usd),
                          db, user, session)
