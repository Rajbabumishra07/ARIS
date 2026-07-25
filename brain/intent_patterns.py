"""
ARIS V16.1 Smart Intent Engine
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
        "goodbye",
        "bye"
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
        "what's your name",
        "whats your name",
        "tell me your name"
    ],

    "ask_my_name": [
        "what is my name",
        "what's my name",
        "whats my name",
        "tell me my name",
        "do you know my name",
        "who am i"
    ],

    "ask_favorite_color": [
        "what is my favorite color",
        "what's my favorite color",
        "whats my favorite color",
        "tell me my favorite color",
        "do you know my favorite color"
    ],

    "remember": [
        "remember",
        "remember my",
        "save",
        "save my",
        "store",
        "store my",
        "note",
        "memorize"
    ],

    "search": [
        "search",
        "search for",
        "find",
        "look for",
        "google"
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
    ]
}


def match_intent(text):

    text = text.lower().strip()

    best_intent = None
    best_score = 0

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            pattern = pattern.lower()

            if text == pattern:
                return intent

            score = 0

            if text.startswith(pattern):
                score += 100

            elif pattern.startswith(text):
                score += 80

            elif pattern in text:
                score += 60

            pattern_words = pattern.split()

            for word in pattern_words:

                if word in text:
                    score += 15

            similarity = SequenceMatcher(
                None,
                text,
                pattern
            ).ratio()

            score += int(similarity * 40)
            if score > best_score:

                best_score = score
                best_intent = intent

    if best_score < 25:
        return None

    return best_intent


def has_intent(text, intent_name):

    return match_intent(text) == intent_name


def get_score(text):

    text = text.lower().strip()

    scores = {}

    for intent, patterns in INTENTS.items():

        best = 0

        for pattern in patterns:

            pattern = pattern.lower()

            score = 0

            if text == pattern:
                score = 100

            elif text.startswith(pattern):
                score = 90

            elif pattern in text:
                score = 70

            similarity = SequenceMatcher(
                None,
                text,
                pattern
            ).ratio()

            score += int(similarity * 30)

            if score > best:
                best = score

        scores[intent] = best

    return scores