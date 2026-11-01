import pytest

from companion.errors import AgentError
from companion.fake_api import DEMO_MARK, SUMMARY_MARK, FakeAnthropicAPI
from conftest import make_companion


def test_parallel_remember_calls_in_one_turn(db):
    fake = FakeAnthropicAPI()
    comp = make_companion(db, fake)
    reply = comp.chat("My name is Anuj. I'm learning Python and I find recursion hard.")
    assert reply.ok and [s.tool for s in reply.steps] == ["remember_fact"] * 3
    assert [f.topic for f in comp.memory.facts()] == ["profile", "goal", "struggle"]
    results = fake.requests[1]["messages"][-1]["content"]          # one message
    assert [r["tool_use_id"] for r in results] == [
        "toolu_offline_01", "toolu_offline_02", "toolu_offline_03"]


def test_without_history_the_model_cant_know(db):
    comp = make_companion(db, FakeAnthropicAPI())
    comp.chat("Hello, my name is Anuj")
    comp.memory.forget(1)                     # only the conversation knows now
    assert "Your name is Anuj" in comp.chat("What's my name?").answer
    other_session = make_companion(db, FakeAnthropicAPI(), session="s2")
    assert "don't know your name" in other_session.chat("What's my name?").answer


def test_long_term_memory_crosses_sessions(db):
    make_companion(db, FakeAnthropicAPI(), session="mon").chat("My name is Anuj")
    fake = FakeAnthropicAPI()
    tue = make_companion(db, fake, session="tue")
    assert tue.conv.messages == []                        # a fresh conversation
    assert tue.chat("What's my name?").answer == f"{DEMO_MARK} Your name is Anuj."
    assert "- #1 [profile] The learner's name is Anuj" in fake.requests[0]["system"]


def test_sessions_resume_from_the_database(db):
    make_companion(db, FakeAnthropicAPI()).chat("I finished lesson 1")
    again = make_companion(db, FakeAnthropicAPI())
    assert len(again.conv.turns()) == 1
    assert again.conv.messages[0]["content"] == "I finished lesson 1"


def test_secret_is_refused_and_reported_to_the_model(db):
    comp = make_companion(db, FakeAnthropicAPI())
    reply = comp.chat("Remember that my password is hunter2")
    assert reply.steps[0].is_error and "never store" in reply.steps[0].output
    assert comp.memory.facts() == []


def test_forget_is_recall_then_forget(db):
    comp = make_companion(db, FakeAnthropicAPI())
    comp.chat("My name is Anuj and I find recursion hard")
    reply = comp.chat("Please forget that I find recursion hard")
    assert [s.tool for s in reply.steps] == ["recall_facts", "forget_fact"]
    assert [f.topic for f in comp.memory.facts()] == ["profile"]


def test_summary_kicks_in_and_keeps_recent_turns(db):
    fake = FakeAnthropicAPI()
    comp = make_companion(db, fake, keep_turns=2, summarize_at=150)
    for text in ("I finished lesson 1", "Explain loops", "Explain dicts", "Explain classes"):
        reply = comp.chat(text)
    assert comp.conv.summary.startswith(SUMMARY_MARK)
    assert "Explain loops" in comp.conv.summary
    assert len(comp.conv.turns()) <= 2 and reply.ok
    saved_summary, saved = db.load_session("anuj", "s1")
    assert saved_summary == comp.conv.summary and saved == comp.conv.messages
    assert "Summary of earlier conversation" in comp.system_prompt("x")


def test_api_error_saves_nothing(db):
    comp = make_companion(db, FakeAnthropicAPI(failures=["401"]))
    with pytest.raises(AgentError, match="API key was rejected"):
        comp.chat("hello")
    assert comp.conv.messages == [] and db.load_session("anuj", "s1") == ("", [])


def test_budget_stops_before_a_call(db):
    comp = make_companion(db, FakeAnthropicAPI(), budget_usd=0.0)
    with pytest.raises(AgentError, match="budget"):
        comp.chat("hello")


def test_refusal_is_not_saved(db, monkeypatch):
    fake = FakeAnthropicAPI()
    comp = make_companion(db, fake)
    monkeypatch.setattr(fake, "_turn", lambda body, system: ([], "refusal"))
    assert comp.chat("hello").stop == "refused"
    assert comp.conv.messages == []
