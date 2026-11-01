import pytest

from companion.errors import ToolError
from companion.fake_api import plan
from companion.tools import definitions, run_tool


def test_definitions_are_strict_and_closed():
    defs = {d["name"]: d for d in definitions()}
    assert set(defs) == {"remember_fact", "recall_facts", "forget_fact"}
    schema = defs["remember_fact"]["input_schema"]
    assert defs["remember_fact"]["strict"] is True
    assert schema["additionalProperties"] is False and schema["required"] == ["text", "topic"]
    assert schema["properties"]["topic"]["enum"][0] == "profile"


def test_bad_input_is_a_tool_error(memory):
    with pytest.raises(ToolError, match="invalid input for remember_fact: topic"):
        run_tool(memory, "remember_fact", {"text": "Likes maths", "topic": "hobby"})
    with pytest.raises(ToolError, match="fact_id"):
        run_tool(memory, "forget_fact", {"fact_id": 0})
    with pytest.raises(ToolError, match="unknown tool"):
        run_tool(memory, "drop_tables", {})


def test_tools_run_against_memory(memory):
    assert run_tool(memory, "remember_fact", {"text": "Likes maths", "topic": "preference"}) \
        == "saved #1 [preference] Likes maths (saved 2026-11-02)"
    assert run_tool(memory, "recall_facts", {"query": "maths"}).startswith("#1 ")
    assert run_tool(memory, "recall_facts", {"query": "art"}) == "no matching facts"


def test_fake_plan_is_a_script_not_a_model():
    assert plan("hello there") == []
    assert [c[1]["topic"] for c in plan("My name is Anuj and I prefer short examples")] \
        == ["profile", "preference"]
    assert plan("forget that I find recursion hard") == [
        ("recall_facts", {"query": "find recursion hard"})]
