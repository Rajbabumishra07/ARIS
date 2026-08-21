"""
ARIS V18 Smart Intent Engine
Author : Raj Babu Mishra

P1.9
Intent Priority + Information Routing
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
        "what is today's date",
        "what is date",
        "tell me the date"
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

    # =====================================================
    # CREATOR
    # =====================================================

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

    # =====================================================
    # MY NAME
    # =====================================================

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
# EXPLICIT COMMAND PREFIXES
#
# These MUST be checked before fuzzy matching.
#
# Examples:
#
# search weather       -> search
# find weather         -> search
# google weather       -> search
#
# remember my birthday -> remember
# save my birthday     -> remember
# store my birthday    -> remember
#
# open chrome          -> open
# close chrome         -> close
# =========================================================

PREFIX_INTENTS = {

    "search": (
        "search ",
        "search for ",
        "find ",
        "google ",
        "look for "
    ),

    "remember": (
        "remember ",
        "save ",
        "store ",
        "memorize ",
        "note "
    ),

    "open": (
        "open ",
        "launch ",
        "start ",
        "run "
    ),

    "close": (
        "close ",
        "terminate ",
        "kill "
    ),

    "minimize": (
        "minimize ",
    ),

    "maximize": (
        "maximize ",
    ),

    "restore": (
        "restore ",
    ),

    "switch": (
        "switch ",
        "switch to "
    )
}


# =========================================================
# PREFIX MATCH
# =========================================================

def _prefix_match(text):

    for intent, prefixes in PREFIX_INTENTS.items():

        for prefix in prefixes:

            if text.startswith(prefix):

                return intent

    return None


# =========================================================
# INFORMATION PHRASE MATCH
# =========================================================

def _information_match(text):

    # =====================================================
    # TIME
    # =====================================================

    time_patterns = (
        "time",
        "what is the time",
        "what is time",
        "what's the time",
        "whats the time",
        "tell me the time",
        "current time",
        "what time is it"
    )

    for pattern in time_patterns:

        if text == pattern:

            return "time"

    # =====================================================
    # DATE
    # =====================================================

    date_patterns = (
        "date",
        "today date",
        "today's date",
        "what is the date",
        "what's the date",
        "whats the date",
        "what is today's date",
        "what is date",
        "tell me the date"
    )

    for pattern in date_patterns:

        if text == pattern:

            return "date"

    # =====================================================
    # MONTH
    # =====================================================

    month_patterns = (
        "month",
        "current month",
        "what month is this",
        "which month is this",
        "what is the current month"
    )

    for pattern in month_patterns:

        if text == pattern:

            return "month"

    # =====================================================
    # YEAR
    # =====================================================

    year_patterns = (
        "year",
        "current year",
        "what year is this",
        "which year is this",
        "what is the current year"
    )

    for pattern in year_patterns:

        if text == pattern:

            return "year"

    # =====================================================
    # CALENDAR
    # =====================================================

    calendar_patterns = (
        "calendar",
        "calender",
        "show calendar",
        "show calender",
        "current calendar",
        "this month calendar"
    )

    for pattern in calendar_patterns:

        if text == pattern:

            return "calendar"

    # =====================================================
    # WEATHER
    #
    # Weather queries with city names are also supported.
    # =====================================================

    if "weather" in text:

        return "weather"

    # =====================================================
    # CREATOR
    # =====================================================

    creator_patterns = (
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
    )

    for pattern in creator_patterns:

        if text == pattern:

            return "ask_creator"

    # =====================================================
    # IDENTITY
    # =====================================================

    identity_patterns = (
        "who are you",
        "what is your name",
        "whats your name",
        "what's your name",
        "tell me your name"
    )

    for pattern in identity_patterns:

        if text == pattern:

            return "ask_name"

    # =====================================================
    # MY NAME
    # =====================================================

    my_name_patterns = (
        "what is my name",
        "whats my name",
        "what's my name",
        "tell me my name",
        "who am i",
        "do you know my name"
    )

    for pattern in my_name_patterns:

        if text == pattern:

            return "ask_my_name"

    return None


# =========================================================
# INTENT MATCHER
# =========================================================

def match_intent(text):

    if not text:

        return None

    text = str(text).lower().strip()

    if not text:

        return None

    # =====================================================
    # 1. EXPLICIT COMMAND PREFIX
    #
    # IMPORTANT:
    # This comes BEFORE weather detection.
    #
    # Therefore:
    #
    # search weather -> search
    # find weather   -> search
    # google weather -> search
    #
    # while:
    #
    # weather Delhi  -> weather
    # =====================================================

    result = _prefix_match(text)

    if result:

        return result

    # =====================================================
    # 2. EXACT INFORMATION MATCH
    # =====================================================

    result = _information_match(text)

    if result:

        return result

    # =====================================================
    # 3. HIGH PRIORITY WINDOW COMMANDS
    # =====================================================

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

    # =====================================================
    # 4. EXACT MATCH
    # =====================================================

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            if text == pattern.lower():

                return intent

    # =====================================================
    # 5. SMART FUZZY MATCH
    # =====================================================

    best_intent = None
    best_score = 0

    text_words = set(text.split())

    for intent, patterns in INTENTS.items():

        for pattern in patterns:

            pattern = pattern.lower()

            pattern_words = set(pattern.split())

            # -------------------------------------------------
            # Similarity
            # -------------------------------------------------

            similarity = SequenceMatcher(
                None,
                text,
                pattern
            ).ratio()

            score = int(similarity * 20)

            # -------------------------------------------------
            # Pattern contained in text
            # -------------------------------------------------

            if pattern in text:

                score += 20

            # -------------------------------------------------
            # Text starts with pattern
            # -------------------------------------------------

            if text.startswith(pattern):

                score += 10

            # -------------------------------------------------
            # First word match
            # -------------------------------------------------

            if (
                text_words
                and pattern_words
                and next(iter(text_words)) in pattern_words
            ):

                score += 5

            # -------------------------------------------------
            # Word overlap
            # -------------------------------------------------

            overlap = text_words & pattern_words

            if overlap:

                score += len(overlap) * 5

            # -------------------------------------------------
            # Best result
            # -------------------------------------------------

            if score > best_score:

                best_score = score
                best_intent = intent

    # =====================================================
    # 6. FUZZY THRESHOLD
    # =====================================================

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