"""
ARIS V14 - Natural Language Understanding Engine
Author : Raj Babu Mishra
"""

import re


class NLU:

    def __init__(self):

        self.filler_words = {
            "the", "a", "an", "please", "pls", "plz",
            "can", "could", "would", "kindly",
            "just", "sir", "hey", "ok", "okay"
        }

        self.replacements = {
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
            "phir": "again"
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

        # Greeting
        if text in {
            "hello",
            "hi",
            "hey",
            "namaste"
        }:
            return "greeting"

        # Exit
        if text in {
            "exit",
            "quit",
            "stop",
            "close",
            "goodbye"
        }:
            return "exit"

        # Remember
        if text.startswith("remember "):
            return "remember"

        # Search
        if text.startswith("search "):
            return "search"

        # Open
        if text.startswith("open "):
            return "open"

        # Close
        if text.startswith("close "):
            return "close"

        # Name Questions
        if (
            "what is your name" in text
            or "whats your name" in text
            or "who are you" in text
            or "tell me your name" in text
            or "your name" == text
            or "apna naam batao" in text
            or "tumhara naam" in text
        ):
            return "ask_name"

        # My Name
        if (
            "what is my name" in text
            or "who am i" in text
            or "mera naam" in text
        ):
            return "ask_my_name"

        # Again
        if text == "again":
            return "again"

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

        if text.startswith("search "):
            data["query"] = text[7:].strip()

        elif text.startswith("remember "):
            data["query"] = text[9:].strip()

        return data


nlu = NLU()