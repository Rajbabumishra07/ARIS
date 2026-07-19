from core.commands import execute
from ai.search import internet_search
from ai.nlp import normalize_command
from ai.personal_ai import personal_ai
from brain.suggestions import suggestion

from brain.router import route
from brain.conversation import conversation
from skills.repeat import repeat_last

import wikipedia
import webbrowser
from urllib.parse import quote
from datetime import datetime


def smart_command(command):

    command = normalize_command(command)
    command = command.lower().strip()

    # ---------------- Conversation ---------------- #

    result = conversation(command)

    if result:
        return result

    # ---------------- Suggestions ---------------- #

    result = suggestion(command)

    if result:
        return result

    # ---------------- Personal AI ---------------- #

    result = personal_ai(command)

    if result:
        return result

    # ---------------- Repeat ---------------- #

    if command in [
        "again",
        "repeat",
        "once more"
    ]:

        cmd = repeat_last()

        if cmd:
            command = cmd

    # ---------------- Router ---------------- #

    result = route(command)

    if result:
        return result

    # ---------------- Play Music ---------------- #

    if command.startswith("play "):

        song = command.replace("play", "", 1).strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={quote(song)}"
        )

        return f"Playing {song} on YouTube."

    # ---------------- Hanuman Chalisa ---------------- #

    elif command in [
        "hanuman chalisa",
        "play hanuman chalisa"
    ]:

        webbrowser.open(
            "https://www.youtube.com/results?search_query=Hanuman+Chalisa"
        )

        return "Playing Hanuman Chalisa."

    # ---------------- Websites ---------------- #

    elif command == "youtube":

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube."

    elif command == "google":

        webbrowser.open("https://www.google.com")

        return "Opening Google."

    elif command == "gmail":

        webbrowser.open("https://mail.google.com")

        return "Opening Gmail."

    elif command == "github":

        webbrowser.open("https://github.com")

        return "Opening GitHub."

    elif command == "chatgpt":

        webbrowser.open("https://chatgpt.com")

        return "Opening ChatGPT."

    # ---------------- System Commands ---------------- #

    result = execute(command)

    if result:
        return result

    # ---------------- Internet Search ---------------- #

    result = internet_search(command)

    if result:
        return result

    # ---------------- Greetings ---------------- #

    if command in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return "Hello! How can I help you?"

    # ---------------- AI ---------------- #

    elif command == "who are you":
        return "I am ARIS, your personal AI assistant."

    elif command == "who made you":
        return "I was created by Raj Babu Mishra."

    elif command == "how are you":
        return "I am doing great. Ready to help you."

    elif command == "what can you do":
        return (
            "I can open apps, search Google, search YouTube,"
            "search Wikipedia, remember information, "
            "tell time and date and help you with many tasks."
        )

    # ---------------- Calculator ---------------- #

    elif command.startswith("calculate "):

        expression = command.replace("calculate", "", 1).strip()

        try:
            return str(eval(expression))
        except Exception:
            return "Invalid calculation."

    # ---------------- Wikipedia ---------------- #

    elif command.startswith("wiki "):

        topic = command.replace("wiki", "", 1).strip()

        try:

            wikipedia.set_lang("en")

            return wikipedia.summary(
                topic,
                sentences=2,
                auto_suggest=True
            )

        except wikipedia.exceptions.DisambiguationError as e:
            return "Multiple topics found: " + ", ".join(e.options[:5])

        except wikipedia.exceptions.PageError:
            return "No Wikipedia page found."

        except Exception:
            return "No information found."

    # ---------------- Time ---------------- #

    elif command in [
        "time",
        "what is the time"
    ]:

        return datetime.now().strftime("%I:%M %p")

    # ---------------- Date ---------------- #

    elif command in [
        "date",
        "today date"
    ]:

        return datetime.now().strftime("%d-%m-%Y")

    # ---------------- Weather ---------------- #

    elif command.startswith("weather"):

        return "Weather module will be added soon."

    # ---------------- News ---------------- #

    elif command == "news":

        return "News module will be added soon."

    # ---------------- Translation ---------------- #

    elif command.startswith("translate"):

        return "Translation module will be added soon."

    # ---------------- Thanks ---------------- #

    elif command in [
        "thank you",
        "thanks",
        "thankyou"
    ]:

        return "You're welcome, Raj."

    # ---------------- Bye ---------------- #

    elif command in [
        "bye",
        "goodbye",
        "see you"
    ]:

        return "Goodbye Raj. Have a great day."

    # ---------------- Exit ---------------- #

    elif command in [
        "exit",
        "quit",
        "stop",
        "close",
        "stop listening",
        "band ho jao",
        "so jao"
    ]:

        return "exit"

    # ---------------- Unknown ---------------- #

    return None