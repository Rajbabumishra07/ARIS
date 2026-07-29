"""
ARIS V17.9 Smart Speech Cleaner
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
            "start a": "open",
            "run a": "open",

            "launch": "open",
            "start": "open",
            "run": "open",

            "oh pen": "open",
            "oh penn": "open",
            "o pen": "open",
            "opan": "open",

            # -------- Conversation Fillers -------- #

            "can you ": "",
            "could you ": "",
            "would you ": "",
            "please ": "",
            "kindly ": "",
            "to ": "",

            "create a ": "create ",
            "open a ": "open ",
            "delete a ": "delete ",
            "rename a ": "rename ",
            "copy a ": "copy ",
            "move a ": "move ",

            "folder named ": "folder ",
            "file named ": "file ",

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
            "the": "",
            " a ": " ",
            " an ": " ",
            " to ": " "
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

    def fuzzy_match_apps(self, text):

        words = text.split()

        new_words = []

        for word in words:

            match = difflib.get_close_matches(
                word,
                self.apps,
                n=1,
                cutoff=0.65
            )

            if match:
                new_words.append(match[0])
            else:
                new_words.append(word)

        return " ".join(new_words)

    def clean(self, text):

        text = text.lower().strip()

        for old, new in self.replacements.items():
            text = text.replace(old, new)

        text = re.sub(r"\s+", " ", text)

        text = self.fuzzy_match_apps(text)

        return text.strip()


speech_cleaner = SpeechCleaner()