"""
ARIS V18 Smart Intent Engine
Author : Raj Babu Mishra

P1.6
Information Intent Routing
"""

from difflib import SequenceMatcher


# =========================================================
# INTENTS
# =========================================================

INTENTS = {

    # =====================================================
    # GREETING
    # =====================================================

    "greeting": [
        "hello",
        "hi",
        "hey",
        "namaste",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    # =====================================================
    # TIME
    # =====================================================

    "time": [
        "time",
        "what is the time",
        "what is time",
        "what's the time",
        "whats the time",
        "tell me the time",
        "current time",
        "what time is it"
    ],

    # =====================================================
    # DATE
    # =====================================================

    "date": [
        "date",
        "today date",
        "today's date",
        "what is the date",
        "what's the date",
        "whats the date",
        "what is today's date"
    ],

    # =====================================================
    # MONTH
    # =====================================================

    "month": [
        "month",
        "current month",
        "what month is this",
        "which month is this",
        "what is the current month"
    ],

    # =====================================================
    # YEAR
    # =====================================================

    "year": [
        "year",
        "current year",
        "what year is this",
        "which year is this",
        "what is the current year"
    ],

    # =====================================================
    # CALENDAR
    # =====================================================

    "calendar": [
        "calendar",
        "calender",
        "show calendar",
        "show calender",
        "current calendar",
        "this month calendar"
    ],

    # =====================================================
    # WEATHER
    # =====================================================

    "weather": [
        "weather",
        "current weather",
        "what is the weather",
        "what's the weather",
        "whats the weather",
        "tell me the weather",
        "weather today",
        "how is the weather",
        "how's the weather",
        "weather in",
        "weather at",
        "weather for"
    ],

    # =====================================================
    # EXIT
    # =====================================================

    "exit": [
        "exit",
        "quit",
        "stop",
        "bye",
        "goodbye",
        "stop listening"
    ],

    # =====================================================
    # AGAIN / REPEAT
    # =====================================================

    "again": [
        "again",
        "repeat",
        "once again",
        "one more time"
    ],

    # =====================================================
    # IDENTITY
    # =====================================================

    "ask_name": [
        "who are you",
        "what is your name",
        "whats your name",
        "what's your name",
        "tell me your name"
    ],

"ask_creator": [
    "who made you",
    "who created you",
    "who is your creator",
    "who is your owner",
    "who developed you",
    "who built you",
    "who programmed you",
    "who is your maker",
    "tell me your creator",
    "tell me who made you"
],

    "ask_my_name": [
        "what is my name",
        "whats my name",
        "what's my name",
        "tell me my name",
        "who am i",
        "do you know my name"
    ],

    # =====================================================
    # MEMORY
    # =====================================================

    "remember": [
        "remember",
        "save",
        "store",
        "memorize",
        "note"
    ],

    # =====================================================
    # SEARCH
    # =====================================================

    "search": [
        "search",
        "search for",
        "find",
        "google",
        "look for"
    ],

    # =====================================================
    # OPEN
    # =====================================================

    "open": [
        "open",
        "launch",
        "start",
        "run"
    ],

    # =====================================================
    # CLOSE
    # =====================================================

    "close": [
        "close",
        "terminate",
        "kill"
    ],

    # =====================================================
    # WINDOW CONTROL
    # =====================================================

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


# =========================================================
# INTENT MATCHER
# =========================================================

def match_intent(text):

    if not text:
        return None

    text = text.lower().strip()

    words = text.split()

    # =====================================================
    # HIGH PRIORITY INFORMATION COMMANDS
    # =====================================================

    # Weather must be checked before generic search/open
    # because phrases such as:
    # "what is the weather in Lucknow"
    # contain additional words.

    if "weather" in text:

        return "weather"

    # =====================================================
    # EXACT INFORMATION MATCH
    # =====================================================

    for intent in (
        "time",
        "date",
        "month",
        "year",
        "calendar"
    ):

        for pattern in INTENTS[intent]:

            if text == pattern.lower():

                return intent

    # =====================================================
    # HIGH PRIORITY COMMANDS
    # =====================================================

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

    # =====================================================
    # EXACT MATCH
    # =====================================================

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            if text == pattern.lower():

                return intent

    # =====================================================
    # SMART FUZZY MATCH
    # =====================================================

    best_intent = None
    best_score = 0

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            pattern = pattern.lower()

            similarity = SequenceMatcher(
                None,
                text,
                pattern
            ).ratio()

            score = int(similarity * 20)

            if pattern in text:

                score += 20

            if text.startswith(pattern):

                score += 10

            if score > best_score:

                best_score = score
                best_intent = intent

    if best_score >= 45:

        return best_intent

    return None


# =========================================================
# HELPERS
# =========================================================

def has_intent(text, intent_name):

    return match_intent(text) == intent_name


def get_score(text):

    scores = {}

    matched = match_intent(text)

    for intent in INTENTS:

        scores[intent] = (
            100
            if matched == intent
            else 0
        )

    return scores