"""A tiny agent loop. The "model" is a FAKE: two fixed rules, not a real LLM (that comes in Module 2)."""


def fake_model(goal: str, notes: list[str]) -> dict[str, str]:
    """Decide the next step. A real agent asks a language model; this fake follows fixed rules."""
    if not notes:
        return {"action": "calculator", "input": "23 * 19"}
    if len(notes) == 1:
        return {"action": "calculator", "input": f"{notes[0]} + 7"}
    return {"action": "finish", "answer": notes[-1]}


def calculator(expression: str) -> str:
    a, op, b = expression.split()
    x, y = int(a), int(b)
    return str(x * y if op == "*" else x + y)


def run_agent(goal: str, max_steps: int = 5) -> str:
    notes: list[str] = []
    for step in range(1, max_steps + 1):
        decision = fake_model(goal, notes)  # 1. decide
        if decision["action"] == "finish":
            print(f"step {step}: finish -> {decision['answer']}")
            return decision["answer"]
        result = calculator(decision["input"])  # 2. act
        notes.append(result)  # 3. observe
        print(f"step {step}: calculator({decision['input']}) -> {result}")
    return "stopped: step limit reached"  # 4. safety limit


if __name__ == "__main__":
    print("answer:", run_agent("What is 23 * 19 + 7?"))
