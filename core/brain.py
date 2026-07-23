"""
ARIS V14 - Brain Engine
"""

from core.identity import aris
from core.memory import Memory
from core.commands import execute
from brain.nlu import nlu
from brain.advisor import advisor

memory = Memory()


def process_command(command):

    text = nlu.normalize(command)

    intent = nlu.intent(text)

    data = nlu.entities(text)

    print("🧠 Intent:", intent)

    # ---------------- Greeting ---------------- #

    if intent == "greeting":
        return "Hello Sir. Welcome back."

    # ---------------- Ask Name ---------------- #

    if intent == "ask_name":
        return (
            f"{aris.greeting}\n"
            f"My name is {aris.name}. "
            "I am your personal AI assistant."
        )

    # ---------------- Ask My Name ---------------- #

    if intent == "ask_my_name":

        result = memory.search("my name")

        if result:
            return "Sir, " + result[-1]

        return "Sir, I don't know your name yet."

    # ---------------- Remember ---------------- #

    if intent == "remember":

        value = data["query"]

        if not value:
            return "Sir, what should I remember?"

        memory.remember(value)

        return (
            "Sir, I heard:\n"
            f"'{value}'\n\n"
            "Memory saved successfully."
        )

    # ---------------- Search ---------------- #

    if intent == "search":

        keyword = data["query"]

        result = memory.search(keyword)

        if result:
            return "\n".join(result)

        return "Sir, nothing found."

    # ---------------- Exit ---------------- #

    if intent == "exit":
        return "exit"

    # ---------------- Execute ---------------- #

    result = execute(text)

    if result:
        return result

    # ---------------- Advice ---------------- #

    advice = advisor.suggest(text)

    if advice:
        print("💡", advice)

    # ---------------- Unknown ---------------- #

    return (
        "Sir, I didn't understand that.\n"
        "Could you please say it differently?"
    )