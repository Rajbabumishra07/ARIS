"""
ARIS V12 - Context Engine
"""

from collections import deque


class ContextEngine:

    def __init__(self):

        self.history = deque(maxlen=20)

        self.last_command = ""

        self.last_subject = ""

        self.last_action = ""

    def remember(self, command):

        command = command.strip()

        self.history.append(command)

        self.last_command = command

        words = command.lower().split()

        if len(words):

            self.last_action = words[0]

        if len(words) > 1:

            self.last_subject = " ".join(words[1:])

    def resolve(self, command):

        text = command.lower().strip()

        if text in [

            "again",
            "repeat",

            "phir",

            "fir",

            "dobara",

            "again please"

        ]:

            return self.last_command

        replace = {

            "it": self.last_subject,
            "him": self.last_subject,
            "her": self.last_subject,
            "that": self.last_subject,
            "this": self.last_subject,
            "use": self.last_subject,
            "usko": self.last_subject,
            "vo": self.last_subject,
            "wah": self.last_subject

        }

        for key, value in replace.items():

            if value:

                text = text.replace(key, value)

        return text

    def get_last(self):

        return self.last_command

    def clear(self):

        self.history.clear()

        self.last_command = ""

        self.last_subject = ""

        self.last_action = ""


context = ContextEngine()