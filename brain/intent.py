"""
ARIS V12 - Intent Engine
Author : Raj Babu Mishra
"""

import re


class IntentEngine:

    def __init__(self):

        self.intents = {

            "open_app": [
                "open",
                "start",
                "launch",
                "run",
                "khol",
                "khol do",
                "chalu karo",
                "open app",
            ],

            "search": [
                "search",
                "find",
                "look for",
                "dhundo",
                "khojo",
            ],

            "remember": [
                "remember",
                "yaad rakho",
                "remember that",
            ],

            "note": [
                "note",
                "likho",
                "note down",
            ],

            "goal": [
                "goal",
                "target",
                "lakshya",
            ],

            "exit": [
                "exit",
                "quit",
                "stop",
                "bye",
                "goodbye",
                "band ho jao",
            ]
        }

    def detect(self, text):

        text = text.lower().strip()

        text = re.sub(r"\s+", " ", text)

        for intent, words in self.intents.items():

            for word in words:

                if word in text:

                    return intent

        return "conversation"


intent = IntentEngine()