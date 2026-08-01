"""
ARIS V17.8 Smart Intent Engine
Author : Raj Babu Mishra
"""

from difflib import SequenceMatcher

INTENTS = {

    "greeting": [
        "hello",
        "hi",
        "hey",
        "namaste",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "exit": [
        "exit",
        "quit",
        "stop",
        "bye",
        "goodbye"
    ],

    "again": [
        "again",
        "repeat",
        "once again",
        "one more time"
    ],

    "ask_name": [
        "who are you",
        "what is your name",
        "whats your name",
        "what's your name",
        "tell me your name"
    ],

    "ask_my_name": [
        "what is my name",
        "whats my name",
        "what's my name",
        "tell me my name",
        "who am i",
        "do you know my name"
    ],

    "ask_favorite_color": [
        "what is my favorite color",
        "whats my favorite color",
        "what's my favorite color",
        "tell me my favorite color"
    ],

    "ask_creator": [
        "who created you",
        "who made you",
        "who is your creator",
        "who developed you"
    ],

    "ask_owner": [
        "who is your owner",
        "who owns you",
        "who is your master"
    ],

    "ask_version": [
        "what is your version",
        "tell me your version",
        "your version",
        "version"
    ],

    "ask_identity": [
        "what is aris",
        "tell me about yourself",
        "introduce yourself",
        "introduce",
        "about yourself"
    ],

    "ask_purpose": [
        "why were you created",
        "what is your purpose",
        "what can you do",
        "why do you exist"
    ],

    "ask_full_form": [
        "full form of aris",
        "what does aris stand for",
        "aris full form"
    ],

    "remember": [
        "remember",
        "save",
        "store",
        "memorize",
        "note"
    ],

    "search": [
        "search",
        "search for",
        "find",
        "google",
        "look for"
    ],

    "open": [
        "open",
        "launch",
        "start",
        "run"
    ],

    "close": [
        "close",
        "terminate",
        "kill"
    ],

    "minimize": [
        "minimize"
    ],

    "maximize": [
        "maximize"
    ],

    "restore": [
        "restore"
    ],

    "switch": [
        "switch",
        "switch to"
    ]
}


def match_intent(text):

    text = text.lower().strip()

    words = text.split()

    if words:

        first = words[0]

        priority = {
            "open": "open",
            "launch": "open",
            "start": "open",
            "run": "open",
            "close": "close",
            "minimize": "minimize",
            "maximize": "maximize",
            "restore": "restore",
            "switch": "switch"
        }

        if first in priority:
            return priority[first]

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            if text == pattern.lower():
                return intent

    best_intent = None
    best_score = 0

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            pattern = pattern.lower()

            score = 0

            similarity = SequenceMatcher(
                None,
                text,
                pattern
            ).ratio()

            score += int(similarity * 20)

            if pattern in text:
                score += 20

            if score > best_score:
                best_score = score
                best_intent = intent

    if best_score >= 45:
        return best_intent

    return None


def has_intent(text, intent_name):
    return match_intent(text) == intent_name


def get_score(text):

    scores = {}

    for intent in INTENTS:
        scores[intent] = (
            100 if match_intent(text) == intent else 0
        )

    return scores