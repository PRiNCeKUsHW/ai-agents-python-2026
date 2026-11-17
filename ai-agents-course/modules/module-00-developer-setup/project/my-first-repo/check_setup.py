"""check_setup.py: is this project set up the right way?

Checks, in order:
  1. Python is new enough (3.11 or later)
  2. it runs inside a virtual environment (.venv)
  3. every package in requirements.txt is installed, at the pinned version
  4. a .env file exists and has every setting that .env.example lists
  5. .gitignore keeps .env and .venv out of git
  6. the folder is a git repository

Run it:  python check_setup.py      (exit code 0 = all good, 1 = something to fix)
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from importlib import metadata
from pathlib import Path

MIN_PYTHON = (3, 11)


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


def check_python(version: tuple[int, int] | None = None) -> Check:
    version = version or (sys.version_info[0], sys.version_info[1])
    found = f"{version[0]}.{version[1]}"
    need = f"{MIN_PYTHON[0]}.{MIN_PYTHON[1]}"
    ok = version >= MIN_PYTHON
    return Check("Python version", ok, f"{found} (need {need}+)")


def in_virtualenv() -> bool:
    # Inside a venv, sys.prefix points at .venv; outside, both are the same.
    return sys.prefix != sys.base_prefix


def check_venv() -> Check:
    name = "Virtual environment"
    if in_virtualenv():
        return Check(name, True, f"active: {Path(sys.prefix).name}")
    return Check(name, False, "not active: source .venv/bin/activate")


def read_requirements(path: Path) -> dict[str, str]:
    """'python-dotenv==1.2.4' -> {'python-dotenv': '1.2.4'}.

    Blank lines and # comments are skipped.
    """
    pins: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#")[0].strip()
        if line:
            name, _, version = line.partition("==")
            pins[name.strip()] = version.strip()
    return pins


def check_packages(path: Path) -> Check:
    if not path.exists():
        return Check("Packages", False, "requirements.txt is missing")
    problems = []
    pins = read_requirements(path)
    for name, version in pins.items():
        try:
            installed = metadata.version(name)
        except metadata.PackageNotFoundError:
            problems.append(f"{name} not installed")
            continue
        if version and installed != version:
            problems.append(f"{name} {installed} (want {version})")
    if problems:
        return Check("Packages", False, "; ".join(problems))
    return Check("Packages", True, f"{len(pins)} installed, versions match")


def read_env_names(path: Path) -> set[str]:
    """Setting names in a .env-style file: 'APP_NAME=demo' -> 'APP_NAME'."""
    names = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            names.add(line.split("=", 1)[0].removeprefix("export ").strip())
    return names


def check_env(folder: Path) -> Check:
    env, example = folder / ".env", folder / ".env.example"
    if not env.exists():
        return Check(".env file", False, "missing: copy .env.example to .env")
    have = read_env_names(env)
    want = read_env_names(example) if example.exists() else set()
    missing = sorted(want - have)
    if missing:
        return Check(".env file", False, "missing: " + ", ".join(missing))
    return Check(".env file", True, f"{len(have)} settings (values hidden)")


def check_gitignore(folder: Path) -> Check:
    path = folder / ".gitignore"
    lines = path.read_text(encoding="utf-8").split() if path.exists() else []
    missing = [p for p in (".env", ".venv/")
               if p not in lines and p.rstrip("/") not in lines]
    if missing:
        return Check(".gitignore", False, "add: " + ", ".join(missing))
    return Check(".gitignore", True, ".env and .venv/ are ignored")


def check_git(folder: Path) -> Check:
    if (folder / ".git").is_dir():
        return Check("Git repository", True, "found .git/")
    return Check("Git repository", False, "not a repo yet: git init")


def run_checks(folder: Path) -> list[Check]:
    return [
        check_python(),
        check_venv(),
        check_packages(folder / "requirements.txt"),
        check_env(folder),
        check_gitignore(folder),
        check_git(folder),
    ]


def main() -> int:
    checks = run_checks(Path.cwd())
    for c in checks:
        mark = "OK" if c.ok else "!!"
        print(f"[{mark}] {c.name:<20} {c.detail}")
    passed = sum(c.ok for c in checks)
    print(f"{passed}/{len(checks)} checks passed")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
