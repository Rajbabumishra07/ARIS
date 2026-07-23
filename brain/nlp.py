"""
ARIS V14 NLP Engine
Author : Raj Babu Mishra
"""

import re


class NLP:

    def __init__(self):

        self.replace = {

            # Hindi
            "khol do": "open",
            "khol": "open",
            "kholo": "open",
            "band karo": "close",
            "band": "close",

            "yaad rakho": "remember",
            "yaad rakhna": "remember",

            "dhundo": "search",
            "khojo": "search",

            "dobara": "again",
            "phir": "again",
            "fir": "again",

            # English fixes
            "whats": "what is",
            "whore": "who are",
            "im": "i am",

            # Common Vosk mistakes
            "he stopped": "stop",
            "you stop": "stop",
            "exude": "exit",
            "egypt blue": "is blue",
            "easy blue": "is blue"
        }

    def normalize(self, text):

        text = text.lower().strip()

        for old, new in self.replace.items():
            text = text.replace(old, new)

        text = re.sub(r"\s+", " ", text)

        return text.strip()


nlp = NLP()