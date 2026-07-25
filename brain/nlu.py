"""
ARIS V16 - Natural Language Understanding Engine
Author : Raj Babu Mishra
"""

import re

from brain.intent_patterns import match_intent


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
            "meri city": "my city",
            "mera city": "my city",

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

            if word in self.filler_words:
                continue

            words.append(word)

        return " ".join(words)

    # ---------------- Intent ---------------- #

    def intent(self, text):

        text = self.normalize(text)

        intent = match_intent(text)

        if intent:
            return intent

        return "conversation"
        # ---------------- Entities ---------------- #

    def entities(self, text):

        text = self.normalize(text)

        intent = self.intent(text)

        data = {
            "intent": intent,
            "text": text,
            "query": "",
            "app": ""
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

        if intent == "remember":

            prefixes = [
                "remember",
                "save",
                "store",
                "note",
                "memorize"
            ]

            for prefix in prefixes:

                if text.startswith(prefix):

                    data["query"] = text[len(prefix):].strip()

                    break

        elif intent == "search":

            prefixes = [
                "search",
                "search for",
                "find",
                "look for",
                "google"
            ]

            for prefix in prefixes:

                if text.startswith(prefix):

                    data["query"] = text[len(prefix):].strip()

                    break

        elif intent == "open":

            prefixes = [
                "open",
                "launch",
                "start",
                "run"
            ]

            for prefix in prefixes:

                if text.startswith(prefix):

                    data["app"] = text[len(prefix):].strip()

                    break

        elif intent == "close":

            prefixes = [
                "close",
                "terminate",
                "kill"
            ]

            for prefix in prefixes:

                if text.startswith(prefix):

                    data["app"] = text[len(prefix):].strip()

                    break

        return data
        # ---------------- Helper Functions ---------------- #

    def is_greeting(self, text):
        return self.intent(text) == "greeting"

    def is_exit(self, text):
        return self.intent(text) == "exit"

    def is_again(self, text):
        return self.intent(text) == "again"

    def is_remember(self, text):
        return self.intent(text) == "remember"

    def is_search(self, text):
        return self.intent(text) == "search"

    def is_open(self, text):
        return self.intent(text) == "open"

    def is_close(self, text):
        return self.intent(text) == "close"

    def is_ask_name(self, text):
        return self.intent(text) == "ask_name"

    def is_ask_my_name(self, text):
        return self.intent(text) == "ask_my_name"

    def is_ask_favorite_color(self, text):
        return self.intent(text) == "ask_favorite_color"


nlu = NLU()