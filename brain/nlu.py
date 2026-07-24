"""
ARIS V15 - Natural Language Understanding Engine
Author : Raj Babu Mishra
"""

import re


class NLU:

    def __init__(self):

        self.filler_words = {
            "the", "a", "an",
            "please", "pls", "plz",
            "can", "could", "would",
            "kindly", "just",
            "sir", "hey",
            "ok", "okay",
            "i", "me", "myself"
        }

        self.replacements = {

            # Hindi
            "yaad rakho": "remember",
            "yaad rakhna": "remember",
            "dhundo": "search",
            "khojo": "search",
            "google karo": "search",
            "khol do": "open",
            "khol": "open",
            "band karo": "close",
            "band": "close",
            "dobara": "again",
            "fir": "again",
            "phir": "again",

            # English Variants
            "i remember": "remember",
            "please remember": "remember",
            "can you remember": "remember",
            "could you remember": "remember",
            "would you remember": "remember",

            # Common Recognition Mistakes
            "what each": "what is",
            "what eg": "what is",
            "why these": "what is",
            "boy at": "who are",
            "colour": "color",
            "favourite": "favorite",
            "period": "favorite",
        }

    # ---------------- Normalize ---------------- #

    def normalize(self, text):

        text = text.lower().strip()

        for old, new in self.replacements.items():
            text = text.replace(old, new)

        text = re.sub(r"[^a-z0-9 ]+", " ", text)
        text = re.sub(r"\s+", " ", text)

        words = []

        for word in text.split():

            if word in self.filler_words:
                continue

            words.append(word)

        return " ".join(words).strip()

    # ---------------- Intent ---------------- #

    def intent(self, text):

        text = self.normalize(text)

        if text in {
            "hello",
            "hi",
            "hey",
            "namaste"
        }:
            return "greeting"

        if text in {
            "exit",
            "quit",
            "stop",
            "goodbye"
        }:
            return "exit"

        if text == "again":
            return "again"

        if text.startswith("remember "):
            return "remember"

        if text.startswith("search "):
            return "search"

        if text.startswith("open "):
            return "open"

        if text.startswith("close "):
            return "close"

        if (
            "who are you" in text
            or "what is your name" in text
            or "whats your name" in text
            or "tell me your name" in text
            or text == "your name"
        ):
            return "ask_name"

        if (
            "what is my name" in text
            or "who am i" in text
            or "my name" == text
            or text.startswith("what is my name")
        ):
            return "ask_my_name"

        return "conversation"

    # ---------------- Entities ---------------- #

    def entities(self, text):

        text = self.normalize(text)

        data = {
            "intent": self.intent(text),
            "text": text,
            "app": None,
            "query": None
        }

        apps = [
            "chrome",
            "youtube",
            "google",
            "calculator",
            "notepad",
            "paint",
            "camera",
            "settings"
        ]

        for app in apps:

            if app in text:
                data["app"] = app
                break

        if text.startswith("remember "):
            data["query"] = text.replace("remember", "", 1).strip()

        elif text.startswith("search "):
            data["query"] = text.replace("search", "", 1).strip()

        return data


nlu = NLU()