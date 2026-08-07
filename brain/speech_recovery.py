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


# ---------------------------------------------------------
# Protected Token
# ---------------------------------------------------------

def _protected(word):

    return (
        "." in word
        or "\\" in word
        or "/" in word
        or ":" in word
    )


# ---------------------------------------------------------
# Exact Alias Replacement
# ---------------------------------------------------------

def _replace(text, aliases):

    words = text.split()
    result = []

    for word in words:

        # Never modify filenames / paths
        if _protected(word):
            result.append(word)
            continue

        # IMPORTANT:
        # Exact-word replacement only.
        #
        # document  -> documents
        # documents -> documents
        #
        # Never:
        # documents -> documentss
        #

        result.append(
            aliases.get(word, word)
        )

    return " ".join(result)


# ---------------------------------------------------------
# Fuzzy Recovery
# ---------------------------------------------------------

def _recover_words(text, aliases):

    words = []
    keys = list(aliases.keys())
    values = set(aliases.values())

    for word in text.split():

        # Protect filenames and paths
        if _protected(word):
            words.append(word)
            continue

        # Already valid alias/value
        if word in keys or word in values:
            words.append(word)
            continue

        match = get_close_matches(
            word,
            keys,
            n=1,
            cutoff=0.90
        )

        if match:

            words.append(
                aliases[match[0]]
            )

        else:

            words.append(word)

    return " ".join(words)


# ---------------------------------------------------------
# Main Recovery
# ---------------------------------------------------------

def recover(text):

    text = text.lower().strip()

    if not text:
        return text

    # -----------------------------------------------------
    # Common
    # -----------------------------------------------------

    text = _replace(
        text,
        COMMON
    )

    text = _recover_words(
        text,
        COMMON
    )

    # -----------------------------------------------------
    # File / Folder
    # -----------------------------------------------------

    if (
        text.startswith("create ")
        or text.startswith("make ")
        or text.startswith("delete ")
        or text.startswith("rename ")
        or text.startswith("copy ")
        or text.startswith("move ")
        or text.startswith("open file ")
        or text.startswith("open folder ")
        or text.startswith("open desktop")
        or text.startswith("open documents")
        or text.startswith("open downloads")
        or text.startswith("open pictures")
        or text.startswith("open music")
        or text.startswith("open videos")
    ):

        text = _replace(
            text,
            FILES
        )

        text = _recover_words(
            text,
            FILES
        )

    # -----------------------------------------------------
    # Apps
    # -----------------------------------------------------

    if (
        text.startswith("open ")
        or text.startswith("launch ")
        or text.startswith("start ")
        or text.startswith("run ")
        or text.startswith("minimize ")
        or text.startswith("maximize ")
        or text.startswith("restore ")
        or text.startswith("switch ")
    ):

        text = _replace(
            text,
            APPS
        )

        text = _recover_words(
            text,
            APPS
        )

    # -----------------------------------------------------
    # Browser
    # -----------------------------------------------------

    text = _replace(
        text,
        BROWSER
    )

    text = _recover_words(
        text,
        BROWSER
    )

    # -----------------------------------------------------
    # System
    # -----------------------------------------------------

    text = _replace(
        text,
        SYSTEM
    )

    text = _recover_words(
        text,
        SYSTEM
    )

    return text


speech_recovery = recover