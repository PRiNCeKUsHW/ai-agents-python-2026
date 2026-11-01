"""Long-term memory: facts about the learner that outlive any conversation.

The model saves and deletes facts with tools, and the most relevant ones are
put into the system prompt of every new chat. "Relevant" here is simple word
overlap; Module 10 (RAG) replaces it with embeddings.
"""
import re
from dataclasses import dataclass
from datetime import date

from companion.db import Database
from companion.errors import ToolError

TOPICS = ("profile", "goal", "struggle", "progress", "preference")
SECRET = re.compile(r"(password|passcode|api[ _-]?key|sk-[a-z0-9-]{8,}|"
                    r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b)", re.I)
STOP = {"the", "a", "an", "is", "are", "and", "or", "of", "to", "in", "on",
        "my", "me", "i", "you", "what", "do", "about", "for", "that", "please"}


@dataclass
class Fact:
    id: int
    text: str
    topic: str
    saved: str              # ISO date


def words(text: str) -> set[str]:
    text = text.lower().replace("'s", "")          # learner's -> learner
    return {w for w in re.findall(r"[a-z0-9]+", text) if w not in STOP}


class LongTermMemory:
    """One user's facts. Every query is filtered by this user's id."""

    def __init__(self, db: Database, user: str, today: date) -> None:
        self.db = db
        self.user = user
        self.today = today

    def facts(self) -> list[Fact]:
        rows = self.db.query("SELECT id, text, topic, saved FROM facts "
                             "WHERE user_id = ? ORDER BY id", self.user)
        return [Fact(**dict(r)) for r in rows]

    def remember(self, text: str, topic: str) -> Fact:
        """Save one fact. Refuses secrets; doesn't save the same fact twice."""
        text = text.strip().rstrip(".")
        if SECRET.search(text):
            raise ToolError("refused: never store passwords, keys or card "
                            "numbers in memory")
        for fact in self.facts():
            if fact.text.lower() == text.lower():
                return fact                              # already known
        saved = self.today.isoformat()
        new_id = self.db.write("INSERT INTO facts (user_id, text, topic, saved)"
                               " VALUES (?, ?, ?, ?)",
                               self.user, text, topic, saved)
        return Fact(new_id, text, topic, saved)

    def recall(self, query: str, limit: int = 5) -> list[Fact]:
        """Facts sharing the most words with the query, best first."""
        wanted = words(query)
        scored = [(len(wanted & words(f.text + " " + f.topic)), f)
                  for f in self.facts()]
        hits = [(s, f) for s, f in scored if s > 0]
        hits.sort(key=lambda sf: (-sf[0], sf[1].id))
        return [f for _, f in hits[:limit]]

    def forget(self, fact_id: int) -> Fact:
        for fact in self.facts():
            if fact.id == fact_id:
                self.db.write("DELETE FROM facts WHERE user_id = ? AND id = ?",
                              self.user, fact_id)
                return fact
        raise ToolError(f"no fact #{fact_id}: use recall_facts to find the "
                        f"right number")

    def for_prompt(self, query: str, limit: int = 6) -> list[Fact]:
        """What goes into the system prompt: the profile, then relevant facts."""
        facts = self.facts()
        chosen = [f for f in facts if f.topic == "profile"]
        for fact in self.recall(query, limit) + facts[-3:]:   # + the newest
            if fact not in chosen:
                chosen.append(fact)
        return chosen[:limit]


def describe(fact: Fact) -> str:
    return f"#{fact.id} [{fact.topic}] {fact.text} (saved {fact.saved})"
