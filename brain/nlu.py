"""
ARIS V18 Smart NLU
Author : Raj Babu Mishra

P1.6
Information Intent + Weather Entity Routing
"""

import re

from brain.intent_patterns import match_intent


class NLU:

    def __init__(self):

        self.filler_words = {
            "the",
            "a",
            "an",
            "please",
            "pls",
            "plz",
            "sir",
            "hey",
            "ok",
            "okay",
            "can",
            "could",
            "would",
            "kindly",
            "just"
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

    # =====================================================
    # FILE / PATH CHECK
    # =====================================================

    def _is_file_or_path(self, word):

        return (
            "." in word
            or "\\" in word
            or "/" in word
            or ":" in word
        )

    # =====================================================
    # NORMALIZE
    # =====================================================

    def normalize(self, text):

        if not text:

            return ""

        text = str(text).lower().strip()

        # -------------------------------------------------
        # Replacements
        # -------------------------------------------------

        for old, new in self.replacements.items():

            text = text.replace(
                old,
                new
            )

        # -------------------------------------------------
        # Preserve filenames and paths
        # -------------------------------------------------

        tokens = text.split()

        cleaned_tokens = []

        for token in tokens:

            if self._is_file_or_path(token):

                cleaned_tokens.append(token)

                continue

            token = re.sub(
                r"[^a-z0-9_-]+",
                "",
                token
            )

            if token:

                cleaned_tokens.append(token)

        # -------------------------------------------------
        # Remove filler words
        # -------------------------------------------------

        words = []

        for word in cleaned_tokens:

            if word in self.filler_words:

                continue

            words.append(word)

        return " ".join(words)

    # =====================================================
    # INTENT
    # =====================================================

    def intent(self, text):

        text = self.normalize(text)

        return match_intent(text)

    # =====================================================
    # ENTITIES
    # =====================================================

    def entities(self, text):

        text = self.normalize(text)

        intent = self.intent(text)

        data = {

            "intent": intent,

            "text": text,

            "query": "",

            "app": "",

            "location": ""
        }

        # =================================================
        # WEATHER
        # =================================================

        if intent == "weather":

            location = ""

            # ---------------------------------------------
            # Remove common weather phrases
            # ---------------------------------------------

            weather_patterns = [
                "what is the weather in ",
                "what is weather in ",
                "what's the weather in ",
                "whats the weather in ",
                "tell me the weather in ",
                "current weather in ",
                "weather in ",

                "what is the weather at ",
                "what is weather at ",
                "weather at ",

                "what is the weather for ",
                "weather for ",

                "weather "
            ]

            for prefix in weather_patterns:

                if text.startswith(prefix):

                    location = text[
                        len(prefix):
                    ].strip()

                    break

            # ---------------------------------------------
            # Generic weather command
            # ---------------------------------------------

            if location in (
                "",
                "today"
            ):

                location = ""

            data["location"] = location

            data["query"] = location

            return data

        # =================================================
        # OPEN
        # =================================================

        if intent == "open":

            prefixes = [
                "open",
                "launch",
                "start",
                "run"
            ]

            for prefix in prefixes:

                if text.startswith(prefix):

                    data["app"] = text[
                        len(prefix):
                    ].strip()

                    return data

        # =================================================
        # CLOSE
        # =================================================

        if intent == "close":

            if text.startswith("close"):

                data["app"] = text.replace(
                    "close",
                    "",
                    1
                ).strip()

                return data

        # =================================================
        # MINIMIZE
        # =================================================

        if intent == "minimize":

            data["app"] = text.replace(
                "minimize",
                "",
                1
            ).strip()

            return data

        # =================================================
        # MAXIMIZE
        # =================================================

        if intent == "maximize":

            data["app"] = text.replace(
                "maximize",
                "",
                1
            ).strip()

            return data

        # =================================================
        # RESTORE
        # =================================================

        if intent == "restore":

            data["app"] = text.replace(
                "restore",
                "",
                1
            ).strip()

            return data

        # =================================================
        # SWITCH
        # =================================================

        if intent == "switch":

            app = text

            app = app.replace(
                "switch to",
                ""
            )

            app = app.replace(
                "switch",
                ""
            )

            data["app"] = app.strip()

            return data

        # =================================================
        # SEARCH
        # =================================================

        if intent == "search":

            prefixes = [
                "search for",
                "search",
                "find",
                "google",
                "look for"
            ]

            for prefix in prefixes:

                if text.startswith(prefix):

                    data["query"] = text[
                        len(prefix):
                    ].strip()

                    return data

        # =================================================
        # REMEMBER
        # =================================================

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

                    data["query"] = text[
                        len(prefix):
                    ].strip()

                    return data

        return data

    # =====================================================
    # HELPERS
    # =====================================================

    def is_greeting(self, text):

        return self.intent(text) == "greeting"

    def is_exit(self, text):

        return self.intent(text) == "exit"

    def is_again(self, text):

        return self.intent(text) == "again"

    def is_time(self, text):

        return self.intent(text) == "time"

    def is_date(self, text):

        return self.intent(text) == "date"

    def is_month(self, text):

        return self.intent(text) == "month"

    def is_year(self, text):

        return self.intent(text) == "year"

    def is_calendar(self, text):

        return self.intent(text) == "calendar"

    def is_weather(self, text):

        return self.intent(text) == "weather"

    def is_open(self, text):

        return self.intent(text) == "open"

    def is_close(self, text):

        return self.intent(text) == "close"

    def is_minimize(self, text):

        return self.intent(text) == "minimize"

    def is_maximize(self, text):

        return self.intent(text) == "maximize"

    def is_restore(self, text):

        return self.intent(text) == "restore"

    def is_switch(self, text):

        return self.intent(text) == "switch"

    def is_search(self, text):

        return self.intent(text) == "search"

    def is_remember(self, text):

        return self.intent(text) == "remember"

    def is_ask_name(self, text):

        return self.intent(text) == "ask_name"

    def is_ask_my_name(self, text):

        return self.intent(text) == "ask_my_name"

    def is_ask_favorite_color(self, text):

        return self.intent(text) == "ask_favorite_color"


nlu = NLU()