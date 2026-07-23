"""
ARIS V12 - Intent Engine 2.0
"""

import re


class IntentEngine:

    def __init__(self):

        self.patterns = {

            "open_app": [

                "open",
                "start",
                "launch",
                "run",
                "khol",
                "khol do",
                "chalu karo",
                "browser kholo",
                "chrome kholo"

            ],

            "close_app": [

                "close",
                "band",
                "shutdown",
                "terminate"

            ],

            "search": [

                "search",
                "find",
                "look",
                "dhundo",
                "khojo"

            ],

            "remember": [

                "remember",
                "yaad",
                "remember that"

            ],

            "note": [

                "note",
                "write",
                "likho"

            ],

            "goal": [

                "goal",
                "target",
                "lakshya"

            ],

            "exit": [

                "exit",
                "quit",
                "bye",
                "goodbye",
                "stop"

            ]

        }

    def clean(self, text):

        text = text.lower()

        text = re.sub(r"[^\w\s]", "", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def detect(self, text):

        text = self.clean(text)

        for intent, words in self.patterns.items():

            for word in words:

                if word in text:

                    return intent

        return "conversation"

    def extract_subject(self, text):

        text = self.clean(text)

        remove = [

            "open",
            "start",
            "launch",
            "run",
            "khol",
            "khol do",
            "chalu karo",

            "search",
            "find",
            "look",

            "remember",
            "note",
            "goal"

        ]

        for word in remove:

            text = text.replace(word, "")

        return text.strip()


intent = IntentEngine()