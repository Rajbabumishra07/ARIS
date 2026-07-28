"""
ARIS V18 Speech Recovery Engine
Author : Raj Babu Mishra
"""

from difflib import get_close_matches

from brain.aliases.common import ALIASES as COMMON
from brain.aliases.apps import ALIASES as APPS
from brain.aliases.files import ALIASES as FILES
from brain.aliases.browser import ALIASES as BROWSER
from brain.aliases.system import ALIASES as SYSTEM


def _replace(text, aliases):

    for wrong, correct in aliases.items():

        text = text.replace(wrong, correct)

    return text


def _recover_words(text, aliases):

    words = []

    keys = list(aliases.keys())

    for word in text.split():

        match = get_close_matches(
            word,
            keys,
            n=1,
            cutoff=0.90
        )

        if match:

            words.append(aliases[match[0]])

        else:

            words.append(word)

    return " ".join(words)


def recover(text):

    text = text.lower().strip()

    # ---------- Common ----------

    text = _replace(text, COMMON)
    text = _recover_words(text, COMMON)

    # ---------- Files ----------

    if (
        text.startswith("create")
        or text.startswith("make")
        or text.startswith("delete")
        or text.startswith("rename")
        or text.startswith("copy")
        or text.startswith("move")
        or text.startswith("open desktop")
        or text.startswith("open documents")
        or text.startswith("open downloads")
        or text.startswith("open pictures")
        or text.startswith("open music")
        or text.startswith("open videos")
    ):

        text = _replace(text, FILES)
        text = _recover_words(text, FILES)

    # ---------- Apps ----------

    if (
        text.startswith("open")
        or text.startswith("launch")
        or text.startswith("start")
        or text.startswith("run")
        or text.startswith("minimize")
        or text.startswith("maximize")
        or text.startswith("restore")
        or text.startswith("switch")
    ):

        text = _replace(text, APPS)
        text = _recover_words(text, APPS)

    # ---------- Browser ----------

    text = _replace(text, BROWSER)
    text = _recover_words(text, BROWSER)

    # ---------- System ----------

    text = _replace(text, SYSTEM)
    text = _recover_words(text, SYSTEM)

    return text


speech_recovery = recover