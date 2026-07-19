from brain.intent import detect_intent
from brain.context import context
from core.commands import execute
from ai.search import internet_search


def route(command):

    intent = detect_intent(command)

    print("🧠 Intent:", intent)

    if intent == "chrome":

        context.update("open chrome")

        return execute("open chrome")

    elif intent == "vscode":

        context.update("open vscode")

        return execute("open vscode")

    elif intent == "youtube":

        context.update(command)

        return internet_search("youtube")

    elif intent == "google":

        context.update(command)

        return internet_search("google")

    elif intent == "play":

        context.update(command)

        return internet_search(command)

    return None