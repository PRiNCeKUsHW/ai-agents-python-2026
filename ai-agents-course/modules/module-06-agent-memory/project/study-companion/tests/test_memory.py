import pytest

from companion.errors import ToolError
from companion.memory import LongTermMemory, describe
from conftest import TODAY


def test_remember_numbers_facts_and_skips_duplicates(memory):
    a = memory.remember("The learner's name is Anuj.", "profile")
    b = memory.remember("the learner's name is anuj", "profile")
    assert a.id == b.id == 1 and a.text == "The learner's name is Anuj"
    assert describe(a) == "#1 [profile] The learner's name is Anuj (saved 2026-11-02)"
    assert len(memory.facts()) == 1


@pytest.mark.parametrize("secret", ["my password is hunter2", "API key sk-ant-abc123456",
                                    "card 4111 1111 1111 1111"])
def test_secrets_are_refused(memory, secret):
    with pytest.raises(ToolError, match="never store"):
        memory.remember(secret, "profile")
    assert memory.facts() == []


def test_recall_ranks_by_shared_words(memory):
    memory.remember("The learner finds recursion hard", "struggle")
    memory.remember("The learner is learning Python", "goal")
    memory.remember("The learner prefers short examples", "preference")
    hits = memory.recall("why is recursion so hard")
    assert [f.id for f in hits] == [1]
    assert len(memory.recall("learner's")) == 3          # possessive still matches
    assert memory.recall("zebra") == []


def test_forget_removes_only_that_fact(memory):
    memory.remember("Fact one", "progress")
    memory.remember("Fact two", "progress")
    assert memory.forget(1).text == "Fact one"
    assert [f.id for f in memory.facts()] == [2]
    with pytest.raises(ToolError, match="no fact #1"):
        memory.forget(1)


def test_users_are_isolated(db, memory):
    memory.remember("The learner's name is Anuj", "profile")
    other = LongTermMemory(db, "riya", TODAY)
    assert other.facts() == [] and other.recall("name") == []
    with pytest.raises(ToolError):
        other.forget(1)                     # can't delete someone else's fact
    assert len(memory.facts()) == 1


def test_for_prompt_puts_the_profile_first(memory):
    memory.remember("The learner finds decorators hard", "struggle")
    memory.remember("The learner's name is Anuj", "profile")
    chosen = memory.for_prompt("quiz me on decorators")
    assert [f.topic for f in chosen][:2] == ["profile", "struggle"]
