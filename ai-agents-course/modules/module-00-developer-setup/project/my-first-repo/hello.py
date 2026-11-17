"""hello.py: the first program in your first repository.

Run it from the terminal:
    python hello.py            -> Hello, world!
    python hello.py Riya       -> Hello, Riya!
"""

import sys


def greet(name: str = "world") -> str:
    """Return a friendly greeting for `name`."""
    return f"Hello, {name}!"


def main(argv: list[str]) -> int:
    name = " ".join(argv[1:]) or "world"  # words after the file name
    print(greet(name))
    return 0  # 0 = success; the terminal shows it in $?


if __name__ == "__main__":
    sys.exit(main(sys.argv))
