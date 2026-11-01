import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path

DEFAULT_MODEL = "claude-opus-5-5"


@dataclass(frozen=True)
class Settings:
    model: str
    offline: bool
    budget_usd: float
    max_retries: int
    max_steps: int
    home: Path              # folder with memory.json and sessions/
    keep_turns: int         # recent turns kept word for word
    summarize_at: int       # estimated tokens that trigger a summary
    today: date


def load_settings(force_offline: bool = False) -> Settings:
    """Read settings from environment variables. No key means offline mode."""
    has_key = bool(os.environ.get("ANTHROPIC_API_KEY", "").strip())
    today = os.environ.get("COMP_TODAY")        # fixed date for tests and demos
    return Settings(
        model=os.environ.get("COMP_MODEL", DEFAULT_MODEL),
        offline=force_offline or not has_key,
        budget_usd=float(os.environ.get("COMP_BUDGET_USD", "0.50")),
        max_retries=int(os.environ.get("COMP_MAX_RETRIES", "2")),
        max_steps=int(os.environ.get("COMP_MAX_STEPS", "6")),
        home=Path(os.environ.get("COMP_HOME", ".companion")),
        keep_turns=max(1, int(os.environ.get("COMP_KEEP_TURNS", "4"))),
        summarize_at=int(os.environ.get("COMP_SUMMARIZE_AT", "1500")),
        today=date.fromisoformat(today) if today else date.today(),
    )
