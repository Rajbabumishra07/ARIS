from memory.profile import remember, recall, recall_all


def personal_ai(command):

    command = command.lower().strip()

    # Remove punctuation
    command = command.replace("?", "")
    command = command.replace(".", "")
    command = command.replace(",", "")

    # ---------------- Remember Name ---------------- #

    if command.startswith("my name is"):

        name = command.replace("my name is", "", 1).strip()

        if name:
            remember("name", name)
            return f"Nice to meet you, {name}."

    # ---------------- Recall Name ---------------- #

    if command in [
        "what is my name",
        "tell me my name",
        "who am i",
        "my name"
    ]:

        name = recall("name")

        if name:
            return f"Your name is {name}."

        return "I don't know your name yet."

    # ---------------- Show Memory ---------------- #

    if command in [
        "what do you remember",
        "show memory",
        "memory",
        "show my memory"
    ]:

        data = recall_all()

        if not data:
            return "I don't remember anything yet."

        text = ""

        for key, value in data.items():
            text += f"{key} : {value}\n"

        return text.strip()

    return None