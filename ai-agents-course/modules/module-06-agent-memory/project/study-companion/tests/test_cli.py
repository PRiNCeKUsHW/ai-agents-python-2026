import io

from companion.cli import main


def run(capsys, monkeypatch, tmp_path, *args, stdin="", today="2026-11-02"):
    monkeypatch.setenv("COMP_HOME", str(tmp_path))
    monkeypatch.setenv("COMP_TODAY", today)
    monkeypatch.setattr("sys.stdin", io.StringIO(stdin))
    code = main(list(args))
    out, err = capsys.readouterr()
    return code, out, err


def test_ask_shows_memory_steps_and_footer(capsys, monkeypatch, tmp_path):
    code, out, err = run(capsys, monkeypatch, tmp_path, "ask", "My name is Anuj")
    assert code == 0
    assert "memory   remember_fact(text=\"The learner's name is Anuj\"" in out
    assert "session 2026-11-02 (new) · user me" in err
    assert "[conversation ~" in err and "offline mode" in err


def test_next_day_is_a_new_session_that_still_knows_you(capsys, monkeypatch, tmp_path):
    run(capsys, monkeypatch, tmp_path, "ask", "My name is Anuj")
    code, out, err = run(capsys, monkeypatch, tmp_path, "ask", "What's my name?",
                         today="2026-11-03")
    assert "session 2026-11-03 (new)" in err and "Your name is Anuj." in out
    out = run(capsys, monkeypatch, tmp_path, "sessions", today="2026-11-03")[1]
    assert out.splitlines()[0].startswith("2026-11-02   last used 2026-11-02 · 4 messages")


def test_chat_loop_with_piped_input(capsys, monkeypatch, tmp_path):
    code, out, _ = run(capsys, monkeypatch, tmp_path, "chat",
                       stdin="my name is Anuj\nwhat's my name?\nbye\n")
    assert code == 0 and "you> what's my name?" in out
    assert "companion> (offline demo) Your name is Anuj." in out
    assert out.rstrip().endswith("I'll remember.")


def test_users_dont_share_memory(capsys, monkeypatch, tmp_path):
    run(capsys, monkeypatch, tmp_path, "--user", "anuj", "ask", "My name is Anuj")
    out = run(capsys, monkeypatch, tmp_path, "--user", "riya", "ask", "What's my name?")[1]
    assert "don't know your name" in out
    assert run(capsys, monkeypatch, tmp_path, "--user", "riya", "memory")[1] == "no facts yet\n"


def test_memory_forget_history_purge_and_delete(capsys, monkeypatch, tmp_path):
    run(capsys, monkeypatch, tmp_path, "ask", "My name is Anuj")
    assert run(capsys, monkeypatch, tmp_path, "memory")[1].startswith("#1 [profile]")
    out = run(capsys, monkeypatch, tmp_path, "history", "2026-11-02")[1]
    assert out.startswith("     user: My name is Anuj")
    assert run(capsys, monkeypatch, tmp_path, "forget", "1")[1].startswith("forgot #1")
    code, _, err = run(capsys, monkeypatch, tmp_path, "forget", "1")
    assert code == 1 and "no fact #1" in err
    out = run(capsys, monkeypatch, tmp_path, "purge", "--days", "30", today="2026-12-15")[1]
    assert out == "deleted 1 session(s) not used in 30 days\n"
    run(capsys, monkeypatch, tmp_path, "ask", "My name is Anuj")
    code, out, err = run(capsys, monkeypatch, tmp_path, "delete-me", stdin="n\n")
    assert code == 1 and "nothing was deleted" in err
    out = run(capsys, monkeypatch, tmp_path, "delete-me", stdin="y\n")[1]
    assert "deleted 1 fact(s) and 1 session(s) of me" in out


def test_api_errors_are_one_line(capsys, monkeypatch, tmp_path):
    monkeypatch.setenv("COMP_FAKE_FAIL", "401")
    code, out, err = run(capsys, monkeypatch, tmp_path, "ask", "hello")
    assert code == 1 and "error: the API key was rejected" in err
    assert "Traceback" not in err
