from companion.conversation import Conversation, estimate_tokens, transcript


def turn(i: int, with_tool: bool = False) -> list[dict]:
    msgs = [{"role": "user", "content": f"question {i}"}]
    if with_tool:
        msgs += [{"role": "assistant", "content": [
                     {"type": "tool_use", "id": f"t{i}", "name": "recall_facts",
                      "input": {"query": "x"}}]},
                 {"role": "user", "content": [
                     {"type": "tool_result", "tool_use_id": f"t{i}", "content": "ok"}]}]
    return msgs + [{"role": "assistant", "content": [{"type": "text", "text": f"answer {i}"}]}]


def test_estimate_tokens_is_about_four_characters():
    assert estimate_tokens("a" * 40) == 10 and estimate_tokens("") == 1


def test_turns_start_only_at_the_users_own_words():
    conv = Conversation(messages=turn(1, with_tool=True) + turn(2))
    assert conv.turns() == [0, 4]            # tool results don't start a turn


def test_window_keeps_whole_recent_turns():
    conv = Conversation(messages=turn(1, True) + turn(2, True) + turn(3))
    kept = conv.window(2)
    assert kept[0] == {"role": "user", "content": "question 2"}
    assert len(kept) == 6                    # tool_use + tool_result kept together


def test_compact_folds_old_turns_into_the_summary():
    conv = Conversation(messages=turn(1) + turn(2) + turn(3))
    seen = {}

    def summarize(previous, old):
        seen["old"] = old
        return f"{previous}+{len(old)}"

    assert conv.compact(summarize, keep_turns=1, limit=0) == 4
    assert conv.summary == "+4" and conv.messages == turn(3)
    assert transcript(seen["old"]).splitlines()[0] == "User: question 1"


def test_compact_does_nothing_under_the_limit_or_with_few_turns():
    conv = Conversation(messages=turn(1) + turn(2))
    assert conv.compact(lambda p, o: "x", keep_turns=1, limit=10_000) == 0
    assert conv.compact(lambda p, o: "x", keep_turns=2, limit=0) == 0
    assert conv.summary == ""


def test_failed_summary_keeps_every_message():
    conv = Conversation(messages=turn(1) + turn(2))

    def broken(previous, old):
        raise RuntimeError("API down")

    try:
        conv.compact(broken, keep_turns=1, limit=0)
    except RuntimeError:
        pass
    assert len(conv.messages) == 4
