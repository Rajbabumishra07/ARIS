"""
ARIS V14 Context Engine
Author : Raj Babu Mishra
"""

from collections import deque


class ContextEngine:

    def __init__(self):

        self.history = deque(maxlen=50)

        self.last_command = ""
        self.last_intent = ""
        self.last_subject = ""
        self.last_app = ""
        self.last_response = ""

    # ---------------- Remember ---------------- #

    def remember(self, command, intent="", subject="", app=""):

        command = command.strip()

        self.history.append({
            "command": command,
            "intent": intent,
            "subject": subject,
            "app": app
        })

        self.last_command = command
        self.last_intent = intent

        if subject:
            self.last_subject = subject

        if app:
            self.last_app = app

    # ---------------- Resolve ---------------- #

    def resolve(self, command):

        text = command.lower().strip()

        if text in (
            "again",
            "repeat",
            "dobara",
            "phir",
            "fir",
            "once more"
        ):
            return self.last_command

        replace = {

            "it": self.last_subject,
            "this": self.last_subject,
            "that": self.last_subject,
            "him": self.last_subject,
            "her": self.last_subject,
            "usko": self.last_subject,
            "vo": self.last_subject,
            "wah": self.last_subject,

            "app": self.last_app,
            "application": self.last_app

        }

        words = text.split()

        output = []

        for word in words:

            if word in replace and replace[word]:
                output.append(replace[word])
            else:
                output.append(word)

        return " ".join(output)

    # ---------------- Response ---------------- #

    def set_response(self, response):

        self.last_response = response

    def response(self):

        return self.last_response

    # ---------------- History ---------------- #

    def previous(self):

        if len(self.history) < 2:
            return None

        return list(self.history)[-2]

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    # ---------------- Clear ---------------- #

    def clear(self):

        self.history.clear()

        self.last_command = ""
        self.last_intent = ""
        self.last_subject = ""
        self.last_app = ""
        self.last_response = ""


context = ContextEngine()