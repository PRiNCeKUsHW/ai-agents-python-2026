"""Lets the lesson scripts import the project's `companion` package."""
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2] / "project/study-companion"
sys.path.insert(0, str(PROJECT))
