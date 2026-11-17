import hello


def test_greet_default():
    assert hello.greet() == "Hello, world!"


def test_greet_name():
    assert hello.greet("Riya") == "Hello, Riya!"


def test_main_uses_words_after_file_name(capsys):
    assert hello.main(["hello.py", "Riya", "Sharma"]) == 0
    assert capsys.readouterr().out == "Hello, Riya Sharma!\n"


def test_main_without_name(capsys):
    assert hello.main(["hello.py"]) == 0
    assert capsys.readouterr().out == "Hello, world!\n"
