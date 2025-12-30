SYSTEM_PROMPT = (
    "You are a helpful customer support assistant. "
    "Be clear, practical, and polite. "
    "If needed, ask 1-2 clarifying questions. "
    "Do not invent company policies."
)

def build_prompt(user_message: str, history: list[tuple[str, str]]) -> str:
    text = f"### System:\n{SYSTEM_PROMPT}\n\n"
    for u, a in history[-6:]:
        text += f"### User:\n{u}\n\n### Assistant:\n{a}\n\n"
    text += f"### User:\n{user_message}\n\n### Assistant:\n"
    return text
