"""
ARIS V17.9 Smart Command Engine
Author : Raj Babu Mishra

P1.4
Information Command Routing
Single Core Execution Path
"""

from core.commands import execute
from ai.search import internet_search
from ai.nlp import normalize_command
from ai.personal_ai import personal_ai
from ai.weather import weather
from brain.suggestions import suggestion

from brain.conversation import conversation
from skills.repeat import repeat_last

import wikipedia
import webbrowser
from urllib.parse import quote
from datetime import datetime


def smart_command(command):

    command = normalize_command(command)
    command = command.lower().strip()

    if not command:
        return None

    # =====================================================
    # CONVERSATION
    # =====================================================

    result = conversation(command)

    if result:
        return result

    # =====================================================
    # REPEAT / CONTEXT
    # =====================================================

    if command in [
        "again",
        "repeat",
        "once more"
    ]:

        cmd = repeat_last()

        if cmd:
            command = cmd

    # =====================================================
    # SUGGESTIONS
    # =====================================================

    result = suggestion(command)

    if result:
        return result

    # =====================================================
    # PERSONAL AI
    # =====================================================

    result = personal_ai(command)

    if result:
        return result

    # =====================================================
    # BASIC INFORMATION
    #
    # These commands must NOT enter core.commands.
    # =====================================================

    if command in [
        "time",
        "what is the time",
        "what is time",
        "current time"
    ]:

        return datetime.now().strftime("%I:%M %p")

    if command in [
        "date",
        "today date",
        "today's date"
    ]:

        return datetime.now().strftime("%d-%m-%Y")

    if command in [
        "month",
        "current month",
        "which month is this"
    ]:

        return datetime.now().strftime("%B")

    if command in [
        "year",
        "current year",
        "which year is this"
    ]:

        return datetime.now().strftime("%Y")

    if command in [
        "calendar",
        "calender",
        "show calendar"
    ]:

        return datetime.now().strftime("%B %Y")

    if command.startswith("weather"):

        return "Weather module will be added soon."

    # =====================================================
    # PLAY MUSIC
    # =====================================================

    if command.startswith("play "):

        song = command.replace(
            "play",
            "",
            1
        ).strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={quote(song)}"
        )

        return f"Playing {song} on YouTube."

    # =====================================================
    # HANUMAN CHALISA
    # =====================================================

    if command in [
        "hanuman chalisa",
        "play hanuman chalisa"
    ]:

        webbrowser.open(
            "https://www.youtube.com/results?search_query=Hanuman+Chalisa"
        )

        return "Playing Hanuman Chalisa."

    # =====================================================
    # WEBSITES
    # =====================================================

    if command == "youtube":

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube."

    if command == "google":

        webbrowser.open("https://www.google.com")

        return "Opening Google."

    if command == "gmail":

        webbrowser.open("https://mail.google.com")

        return "Opening Gmail."

    if command == "github":

        webbrowser.open("https://github.com")

        return "Opening GitHub."

    if command == "chatgpt":

        webbrowser.open("https://chatgpt.com")

        return "Opening ChatGPT."

        # =====================================================
    # WEATHER
    # =====================================================

    if command == "weather":

        return weather()

    if command.startswith("weather "):

        city = command.replace(
            "weather",
            "",
            1
        ).strip()

        return weather(city)

    # =====================================================
    # CORE COMMAND EXECUTOR
    #
    # File / Folder / App / System / Window commands
    # =====================================================

    result = execute(command)

    if result:
        return result

    # =====================================================
    # INTERNET SEARCH
    # =====================================================

    result = internet_search(command)

    if result:
        return result

    # =====================================================
    # GREETINGS
    # =====================================================

    if command in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:

        return "Hello! How can I help you?"

    # =====================================================
    # BASIC AI
    # =====================================================

    if command == "who are you":

        return "I am ARIS, your personal AI assistant."

    if command == "who made you":

        return "I was created by Raj Babu Mishra."

    if command == "how are you":

        return "I am doing great. Ready to help you."

    if command == "what can you do":

        return (
            "I can open apps, search Google, search YouTube, "
            "search Wikipedia, remember information, "
            "tell time and date and help you with many tasks."
        )

    # =====================================================
    # CALCULATOR
    # =====================================================

    if command.startswith("calculate "):

        expression = command.replace(
            "calculate",
            "",
            1
        ).strip()

        try:

            return str(eval(expression))

        except Exception:

            return "Invalid calculation."

    # =====================================================
    # WIKIPEDIA
    # =====================================================

    if command.startswith("wiki "):

        topic = command.replace(
            "wiki",
            "",
            1
        ).strip()

        try:

            wikipedia.set_lang("en")

            return wikipedia.summary(
                topic,
                sentences=2,
                auto_suggest=True
            )

        except wikipedia.exceptions.DisambiguationError as e:

            return (
                "Multiple topics found: "
                + ", ".join(e.options[:5])
            )

        except wikipedia.exceptions.PageError:

            return "No Wikipedia page found."

        except Exception:

            return "No information found."

    # =====================================================
    # NEWS
    # =====================================================

    if command == "news":

        return "News module will be added soon."

    # =====================================================
    # TRANSLATION
    # =====================================================

    if command.startswith("translate"):

        return "Translation module will be added soon."

    # =====================================================
    # THANKS
    # =====================================================

    if command in [
        "thank you",
        "thanks",
        "thankyou"
    ]:

        return "You're welcome, Raj."

    # =====================================================
    # BYE
    # =====================================================

    if command in [
        "bye",
        "goodbye",
        "see you"
    ]:

        return "Goodbye Raj. Have a great day."

    # =====================================================
    # EXIT
    # =====================================================

    if command in [
        "exit",
        "quit",
        "stop",
        "close",
        "stop listening",
        "band ho jao",
        "so jao"
    ]:

        return "exit"

    # =====================================================
    # UNKNOWN
    # =====================================================

    return None