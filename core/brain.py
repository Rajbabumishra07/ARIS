"""
ARIS V12 Brain Engine
"""

from core.identity import aris
from core.memory import Memory
from core.commands import execute

from brain.intent import intent
from brain.context import context
from brain.reasoning import reasoning
from brain.conversation import conversation
from brain.personality import personality
from brain.advisor import advisor

memory = Memory()


def process_command(command):

    command = command.strip()

    if not command:
        return None

    lower = command.lower()

    context.remember(command)

    command = context.resolve(command)

    current_intent = intent.detect(command)

    print("🧠 Intent :", current_intent)

    # ---------------- Exit ---------------- #

    if current_intent == "exit":
        return "exit"

    # ---------------- Greeting ---------------- #

    if lower in [
        "hello",
        "hi",
        "hey",
        "namaste",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return personality.greet()

    # ---------------- Identity ---------------- #

    if lower in [
        "who are you",
        "your name",
        "tumhara naam",
        "naam"
    ]:
        return aris.introduce()

    # ---------------- My Name ---------------- #

    if lower in [
        "what is my name",
        "mera naam kya hai"
    ]:

        names = memory.search("my name")

        if names:

            return f"सर, मुझे याद है {names[-1]}"

        return "सर, मुझे अभी आपका नाम याद नहीं है।"

    # ---------------- Remember ---------------- #

    if current_intent == "remember":

        text = command.replace("remember", "", 1).strip()

        if text:

            memory.remember(text)

            return "जी सर। मैंने इसे अपनी स्मृति में सुरक्षित कर लिया है।"

        return "सर, क्या याद रखना है?"

    # ---------------- Note ---------------- #

    if current_intent == "note":

        text = command.replace("note", "", 1).strip()

        if text:

            memory.add_note(text)

            return "जी सर। नोट सुरक्षित कर दिया गया है।"

        return "सर, क्या लिखना है?"

    # ---------------- Goal ---------------- #

    if current_intent == "goal":

        text = command.replace("goal", "", 1).strip()

        if text:

            memory.add_goal(text)

            return "जी सर। लक्ष्य सुरक्षित कर दिया गया है।"

        return "सर, लक्ष्य बताइए।"

    # ---------------- Search ---------------- #

    if current_intent == "search":

        keyword = command

        for word in [
            "search",
            "find",
            "look for"
        ]:
            keyword = keyword.replace(word, "")

        keyword = keyword.strip()

        data = memory.search(keyword)

        if data:

            return "सर, मुझे यह याद है:\n\n" + "\n".join(data)

        return "सर, इससे संबंधित कुछ याद नहीं मिला।"

    # ---------------- Reasoning ---------------- #

    thought = reasoning.think(command)

    if thought:

        print("🧠", thought)

    # ---------------- Advisor ---------------- #

    advice = advisor.suggest(command)

    if advice:

        print("💡", advice)

    # ---------------- Execute ---------------- #

    result = execute(command)

    if result:

        return result

    # ---------------- Unknown ---------------- #

    return personality.unknown()