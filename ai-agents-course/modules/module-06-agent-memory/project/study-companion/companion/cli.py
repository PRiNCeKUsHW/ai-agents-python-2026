import argparse
import json
import os
import sys

from companion import __version__
from companion.agent import Reply, Step, StudyCompanion
from companion.client import make_client
from companion.config import Settings, load_settings
from companion.db import Database
from companion.errors import AgentError, ToolError
from companion.memory import LongTermMemory, describe
from companion.pricing import CostTracker

STOP_MESSAGES = {
    "max_steps": "stopped without an answer (too many tool turns)",
    "refused": "the model declined this request",
    "cut_off": "the reply was cut off at max_tokens",
    "budget": "the budget is used up; raise COMP_BUDGET_USD",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="companion", description="A study companion that remembers you.")
    parser.add_argument("--version", action="version",
                        version=f"%(prog)s {__version__}")
    parser.add_argument("--offline", action="store_true",
                        help="use the built-in fake API (no key needed)")
    parser.add_argument("--user", default=os.environ.get("COMP_USER", "me"),
                        help="whose memory to use (default: me)")
    commands = parser.add_subparsers(dest="command", required=True)

    for name, text in (("ask", "send one message"), ("chat", "chat until 'bye'")):
        cmd = commands.add_parser(name, help=text)
        if name == "ask":
            cmd.add_argument("message")
        cmd.add_argument("--session", default=None,
                         help="conversation to continue (default: today's date)")
    commands.add_parser("memory", help="show everything remembered about you")
    forget = commands.add_parser("forget", help="delete one remembered fact")
    forget.add_argument("fact_id", type=int)
    commands.add_parser("sessions", help="list your conversations")
    history = commands.add_parser("history", help="show one conversation")
    history.add_argument("session")
    purge = commands.add_parser("purge", help="delete old conversations")
    purge.add_argument("--days", type=int, required=True)
    delete = commands.add_parser("delete-me", help="delete ALL your data")
    delete.add_argument("--yes", action="store_true", help="don't ask first")
    return parser


def show_step(step: Step) -> None:
    args = ", ".join(f"{k}={v!r}" for k, v in step.input.items())
    mark = "!" if step.is_error else "="
    first, *rest = step.output.splitlines() or [""]
    print(f"  memory   {step.tool}({args})")
    print(f"           {mark} {first}")
    for line in rest:
        print(f"             {line}")


def footer(reply: Reply, settings: Settings) -> None:
    folded = (f" · {reply.folded} old messages summarized" if reply.folded
              else "")
    print(f"[conversation ~{reply.tokens} tokens{folded} · "
          f"${reply.cost_usd:.5f}{' estimated' if settings.offline else ''}]",
          file=sys.stderr)


def turn(companion: StudyCompanion, text: str, settings: Settings) -> None:
    reply = companion.chat(text, on_step=show_step)
    if not reply.ok:
        raise AgentError(STOP_MESSAGES[reply.stop])
    print(reply.answer)
    footer(reply, settings)


def open_companion(args: argparse.Namespace, settings: Settings,
                   db: Database) -> StudyCompanion:
    session = args.session or settings.today.isoformat()
    companion = StudyCompanion(make_client(settings), settings,
                               CostTracker(settings.budget_usd), db,
                               args.user, session)
    turns = len(companion.conv.turns())
    state = f"resumed, {turns} turn{'s' * (turns != 1)}" if turns else "new"
    print(f"session {session} ({state}) · user {args.user}", file=sys.stderr)
    return companion


def chat(companion: StudyCompanion, settings: Settings) -> None:
    """A read-eval-print loop. Piped input works: printf 'hi\\nbye\\n' | ..."""
    while True:
        print("you> ", end="", flush=True)
        line = sys.stdin.readline()
        if not sys.stdin.isatty():
            print(line.rstrip("\n"))            # echo piped input, like a terminal
        text = line.strip()
        if not line or text.lower() in ("bye", "exit", "quit"):
            print("companion> See you next time. I'll remember.")
            return
        if text:
            print("companion> ", end="")
            turn(companion, text, settings)


def run(args: argparse.Namespace, settings: Settings, db: Database) -> int:
    memory = LongTermMemory(db, args.user, settings.today)
    if args.command == "ask":
        turn(open_companion(args, settings, db), args.message, settings)
    elif args.command == "chat":
        chat(open_companion(args, settings, db), settings)
    elif args.command == "memory":
        facts = memory.facts()
        print("\n".join(describe(f) for f in facts) if facts else "no facts yet")
    elif args.command == "forget":
        print(f"forgot {describe(memory.forget(args.fact_id))}")
    elif args.command == "sessions":
        rows = db.sessions(args.user)
        for r in rows:
            note = ", with summary" if r["summarized"] else ""
            print(f"{r['id']:<12} last used {r['updated']} · "
                  f"{r['messages']} messages{note}")
        if not rows:
            print("no sessions yet")
    elif args.command == "history":
        summary, messages = db.load_session(args.user, args.session)
        if not (summary or messages):
            raise AgentError(f"no session {args.session!r}")
        if summary:
            print(f"summary: {summary}")
        for m in messages:
            content = m["content"]
            text = content if isinstance(content, str) else json.dumps(content)
            short = text if len(text) < 90 else text[:87] + "..."
            print(f"{m['role']:>9}: {short}")
    elif args.command == "purge":
        n = db.purge(args.user, args.days, settings.today)
        print(f"deleted {n} session(s) not used in {args.days} days")
    elif args.command == "delete-me":
        if not args.yes:
            print(f"  confirm  Delete every fact and session of {args.user}? "
                  "[y/N] ", end="", flush=True)
            answer = sys.stdin.readline().strip().lower()
            if not sys.stdin.isatty():
                print(answer)
            if answer not in ("y", "yes"):
                raise AgentError("nothing was deleted")
        n_facts, n_sessions = db.delete_user(args.user)
        print(f"deleted {n_facts} fact(s) and {n_sessions} session(s) "
              f"of {args.user}")
    return 0


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):     # keep stdout and stderr in order
        sys.stdout.reconfigure(line_buffering=True)
    args = build_parser().parse_args(argv)
    settings = load_settings(force_offline=args.offline)
    try:
        db = Database(settings.home / "companion.db")
    except AgentError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    try:
        return run(args, settings, db)
    except (AgentError, ToolError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    finally:
        db.close()
