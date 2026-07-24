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
            "sir", "hey", "ok", "okay",
            "can", "could", "would",
            "kindly", "just"
        }

        self.replacements = {

            "yaad rakho": "remember",
            "yaad rakhna": "remember",

            "dhundo": "search",
            "khojo": "search",
            "google karo": "search",

            "khol do": "open",
            "kholo": "open",

            "band karo": "close",

            "dobara": "again",
            "fir": "again",
            "phir": "again",

            "mera naam": "my name",
            "mera city": "my city",
            "meri city": "my city",

            "colour": "color",
            "favourite": "favorite"
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

            if word not in self.filler_words:
                words.append(word)

        return " ".join(words)
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
            "close",
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
            or "tell me your name" in text
            or text == "your name"
        ):
            return "ask_name"

        if (
            "what is my name" in text
            or "who am i" in text
            or text == "my name"
        ):
            return "ask_my_name"

        if (
            "what is my favorite color" in text
            or text == "favorite color"
            or text == "my favorite color"
        ):
            return "ask_favorite_color"

        return "conversation"
        # ---------------- Entities ---------------- #

    def entities(self, text):

        text = self.normalize(text)

        data = {
            "intent": self.intent(text),
            "text": text,
            "query": None,
            "app": None
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
        # ---------------- Helpers ---------------- #

    def is_remember(self, text):
        return self.intent(text) == "remember"

    def is_search(self, text):
        return self.intent(text) == "search"

    def is_open(self, text):
        return self.intent(text) == "open"

    def is_close(self, text):
        return self.intent(text) == "close"

    def is_greeting(self, text):
        return self.intent(text) == "greeting"

    def is_exit(self, text):
        return self.intent(text) == "exit"

    def is_again(self, text):
        return self.intent(text) == "again"


nlu = NLU()
