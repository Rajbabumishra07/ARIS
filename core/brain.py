"""
ARIS V11 - Brain Engine
Version : 11.2
"""

from core.identity import aris
from core.memory import Memory
from core.commands import execute
from brain.advisor import advisor

memory = Memory()


def process_command(command):

    command = command.strip()
    lower = command.lower()

    # -------- Exit -------- #

    if lower in ["exit", "quit", "stop", "bye", "goodbye"]:
        return "exit"

    # -------- Advisor -------- #

    advice = advisor.suggest(command)

    if advice:
        print("💡 Advice:", advice)

    # -------- Greeting -------- #

    if lower in ["hello", "hi", "hey", "namaste", "नमस्ते"]:
        return aris.greeting

    # -------- Identity -------- #

    if lower in ["who are you", "your name", "tumhara naam", "नाम"]:
        return f"मेरा नाम {aris.name} है, सर।"

    # -------- User Name -------- #

    if lower in ["what is my name", "mera naam kya hai"]:

        results = memory.search("my name is")

        if results:
            last = results[-1]
            name = last.replace("my name is", "").strip()
            return f"सर, आपका नाम {name} है।"

        return "सर, मुझे अभी आपका नाम याद नहीं है।"

    # -------- Remember -------- #

    if lower.startswith("remember "):

        text = command[9:].strip()

        memory.remember(text)

        return "जी सर, मैंने इसे अपनी स्मृति में सुरक्षित कर लिया है।"

    # -------- Note -------- #

    if lower.startswith("note "):

        memory.add_note(command[5:].strip())

        return "जी सर, नोट सुरक्षित कर दिया गया है।"

    # -------- Goal -------- #

    if lower.startswith("goal "):

        memory.add_goal(command[5:].strip())

        return "जी सर, लक्ष्य सुरक्षित कर दिया गया है।"

    # -------- Search -------- #

    if lower.startswith("search "):

        keyword = command[7:].strip()

        results = memory.search(keyword)

        if results:
            return "सर, मुझे यह याद है:\n" + "\n".join(results)

        return "सर, मुझे इससे संबंधित कुछ याद नहीं है।"

    # -------- Show Memory -------- #

    if lower == "show memory":
        return str(memory.get_memory())

    # -------- Execute -------- #

    result = execute(command)

    if result:
        return result

    return "क्षमा करें सर, मैं अभी इस आदेश को नहीं समझ पाया।"