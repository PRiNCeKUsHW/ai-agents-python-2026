import sys
from pathlib import Path

import pytest

import check_setup as cs


def make_project(folder: Path, env: str = "APP_NAME=x\nAPI_KEY=y\n") -> Path:
    (folder / "requirements.txt").write_text("pytest\n")
    (folder / ".env.example").write_text("# comment\nAPP_NAME=\nAPI_KEY=\n")
    (folder / ".env").write_text(env)
    (folder / ".gitignore").write_text(".env\n.venv/\n__pycache__/\n")
    (folder / ".git").mkdir()
    return folder


# 1. Python version
def test_python_new_enough():
    assert cs.check_python((3, 13)).ok


def test_python_too_old():
    c = cs.check_python((3, 9))
    assert not c.ok and c.detail == "3.9 (need 3.11+)"


def test_python_defaults_to_running_version():
    assert cs.check_python().detail.startswith(f"{sys.version_info[0]}.")


# 2. virtual environment
def test_venv_detected(monkeypatch):
    monkeypatch.setattr(sys, "prefix", "/work/.venv")
    monkeypatch.setattr(sys, "base_prefix", "/usr")
    c = cs.check_venv()
    assert c.ok and c.detail == "active: .venv"


def test_no_venv(monkeypatch):
    monkeypatch.setattr(sys, "prefix", "/usr")
    monkeypatch.setattr(sys, "base_prefix", "/usr")
    assert not cs.check_venv().ok


# 3. packages
def test_read_requirements_skips_comments(tmp_path):
    req = tmp_path / "requirements.txt"
    req.write_text("# tools\npython-dotenv==1.2.4\n\npytest  # any version\n")
    assert cs.read_requirements(req) == {"python-dotenv": "1.2.4", "pytest": ""}


def test_packages_ok(tmp_path):
    req = tmp_path / "requirements.txt"
    req.write_text(f"pytest=={pytest.__version__}\n")
    c = cs.check_packages(req)
    assert c.ok and c.detail == "1 installed, versions match"


def test_package_missing(tmp_path):
    req = tmp_path / "requirements.txt"
    req.write_text("surely-not-installed-pkg==1.0\n")
    c = cs.check_packages(req)
    assert not c.ok and "surely-not-installed-pkg not installed" in c.detail


def test_package_wrong_version(tmp_path):
    req = tmp_path / "requirements.txt"
    req.write_text("pytest==0.0.1\n")
    c = cs.check_packages(req)
    assert not c.ok and "(want 0.0.1)" in c.detail


def test_requirements_missing(tmp_path):
    assert cs.check_packages(tmp_path / "requirements.txt").detail == (
        "requirements.txt is missing")


# 4. .env
def test_env_names_ignore_comments_and_export(tmp_path):
    f = tmp_path / ".env"
    f.write_text("# hi\nexport APP_NAME=a\nDEBUG = true\nnot a setting\n")
    assert cs.read_env_names(f) == {"APP_NAME", "DEBUG"}


def test_env_ok_never_shows_values(tmp_path):
    make_project(tmp_path, env="APP_NAME=x\nAPI_KEY=super-secret\n")
    c = cs.check_env(tmp_path)
    assert c.ok and "super-secret" not in c.detail


def test_env_missing_file(tmp_path):
    c = cs.check_env(tmp_path)
    assert not c.ok and "copy .env.example to .env" in c.detail


def test_env_missing_setting(tmp_path):
    make_project(tmp_path, env="APP_NAME=x\n")
    c = cs.check_env(tmp_path)
    assert not c.ok and c.detail == "missing: API_KEY"


# 5. .gitignore
def test_gitignore_ok(tmp_path):
    make_project(tmp_path)
    assert cs.check_gitignore(tmp_path).ok


def test_gitignore_accepts_venv_without_slash(tmp_path):
    (tmp_path / ".gitignore").write_text(".env\n.venv\n")
    assert cs.check_gitignore(tmp_path).ok


def test_gitignore_missing_env(tmp_path):
    (tmp_path / ".gitignore").write_text(".venv/\n")
    c = cs.check_gitignore(tmp_path)
    assert not c.ok and c.detail == "add: .env"


def test_no_gitignore(tmp_path):
    assert cs.check_gitignore(tmp_path).detail == "add: .env, .venv/"


# 6. git
def test_git_repo(tmp_path):
    (tmp_path / ".git").mkdir()
    assert cs.check_git(tmp_path).ok


def test_not_git_repo(tmp_path):
    assert not cs.check_git(tmp_path).ok


# the whole report
def test_main_all_ok(tmp_path, monkeypatch, capsys):
    make_project(tmp_path)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "prefix", "/p/.venv")
    monkeypatch.setattr(sys, "base_prefix", "/usr")
    assert cs.main() == 0
    out = capsys.readouterr().out
    assert "6/6 checks passed" in out and "[!!]" not in out


def test_main_reports_problems(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)  # empty folder: almost everything fails
    assert cs.main() == 1
    out = capsys.readouterr().out
    assert "[!!] Git repository" in out and "checks passed" in out
