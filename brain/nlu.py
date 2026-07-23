"""
ARIS V13 - Natural Language Understanding Engine
"""

import re


class NLU:

    def normalize(self, text):

        text = text.lower().strip()

        replacements = {
            "pls": "please",
            "plz": "please",
            "khol do": "open",
            "khol": "open",
            "chalu karo": "open",
            "band karo": "close",
            "yaad rakho": "remember",
            "dhundo": "search",
            "khojo": "search",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        text = re.sub(r"\s+", " ", text)

        return text

    def intent(self, text):

        text = self.normalize(text)

        if "remember" in text:
            return "remember"

        if "search" in text:
            return "search"

        if "open" in text:
            return "open"

        if "close" in text:
            return "close"

        if any(x in text for x in [
            "who am i",
            "what is my name",
            "mera naam",
            "my name"
        ]):
            return "ask_name"

        if any(x in text for x in [
            "hello",
            "hi",
            "hey"
        ]):
            return "greeting"

        return "conversation"


nlu = NLU()