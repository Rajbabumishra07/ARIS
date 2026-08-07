"""
ARIS V18 Smart Speech Cleaner
Author : Raj Babu Mishra
"""

import re
import difflib


class SpeechCleaner:

    def __init__(self):

        self.replacements = {

            # -------- Command Variants -------- #

            "launch a": "launch",
            "open a": "open",
            "start a": "start",
            "run a": "run",

            "launch": "open",
            "start": "open",
            "run": "open",

            "oh pen": "open",
            "oh penn": "open",
            "o pen": "open",
            "opan": "open",

            # -------- Common Command Mistakes -------- #

            "creat file": "create file",
            "creat folder": "create folder",

            "crete file": "create file",
            "crete folder": "create folder",

            "creat": "create",

            "renam file": "rename file",
            "renam folder": "rename folder",

            "delate file": "delete file",
            "delate folder": "delete folder",

            # -------- Common Apps -------- #

            "browser": "chrome",
            "google browser": "chrome",

            "calculate": "calculator",
            "calculate that": "calculator",
            "calc": "calculator",

            "note pad": "notepad",
            "not bad": "notepad",
            "note bad": "notepad",

            "setting": "settings",
            "sitting": "settings",
            "seting": "settings",

            "chimera": "camera",
            "cam": "camera",

            # -------- Fillers -------- #

            "please": "",
            "sir": "",
            "okay": "",
            "ok": "",

        }

        self.apps = [

            "chrome",
            "settings",
            "camera",
            "calculator",
            "notepad",
            "paint",
            "photos",
            "explorer",
            "browser",
            "task manager",
            "control panel"

        ]

    # -------------------------------------------------
    # Filename / path detection
    # -------------------------------------------------

    def _is_protected_token(self, word):

        return (
            "." in word
            or "\\" in word
            or "/" in word
            or ":" in word
            or word.startswith(".")
        )

    # -------------------------------------------------
    # App fuzzy matching
    # -------------------------------------------------

    def fuzzy_match_apps(self, text):

        words = text.split()

        new_words = []

        for word in words:

            # NEVER fuzzy-match filenames or paths.
            if self._is_protected_token(word):
                new_words.append(word)
                continue

            match = difflib.get_close_matches(
                word,
                self.apps,
                n=1,
                cutoff=0.75
            )

            if match:
                new_words.append(match[0])
            else:
                new_words.append(word)

        return " ".join(new_words)

    # -------------------------------------------------
    # Cleaning
    # -------------------------------------------------

    def clean(self, text):

        if not text:
            return ""

        text = text.lower().strip()

        # Fix common speech errors first.
        for old, new in self.replacements.items():
            text = text.replace(old, new)

        # Normalize whitespace only.
        text = re.sub(r"\s+", " ", text)

        # Protect filename-like tokens from app fuzzy matching.
        text = self.fuzzy_match_apps(text)

        return text.strip()


speech_cleaner = SpeechCleaner()