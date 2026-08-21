"""
ARIS V18
P1.9 Step 1
Command Variation Tests

Author : Raj Babu Mishra

Purpose:
Check whether different natural-language variations
reach the correct ARIS intent.
"""

import sys
from pathlib import Path


# =========================================================
# PROJECT ROOT
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# =========================================================
# NLU
# =========================================================

from brain.nlu import nlu


# =========================================================
# TEST HELPER
# =========================================================

def run_test(name, command, expected):

    print(f"\n🧪 TEST: {name}")
    print(f"   Command  : {command}")
    print(f"   Expected : {expected}")

    try:

        result = nlu.intent(command)

        print(f"   Detected : {result}")

        if result == expected:

            print("   ✅ PASS")
            return True

        print("   ❌ FAIL")

        return False

    except Exception as error:

        print(f"   ❌ ERROR: {error}")

        return False


# =========================================================
# COMMAND VARIATION TESTS
# =========================================================

def main():

    print("=" * 60)
    print("🤖 ARIS P1.9 COMMAND VARIATION TEST")
    print("=" * 60)

    tests = [

        # -------------------------------------------------
        # OPEN
        # -------------------------------------------------

        (
            "Open",
            "open chrome",
            "open"
        ),

        (
            "Launch",
            "launch chrome",
            "open"
        ),

        (
            "Start",
            "start chrome",
            "open"
        ),

        (
            "Run",
            "run chrome",
            "open"
        ),

        # -------------------------------------------------
        # CLOSE
        # -------------------------------------------------

        (
            "Close",
            "close chrome",
            "close"
        ),

        # -------------------------------------------------
        # WINDOW
        # -------------------------------------------------

        (
            "Minimize",
            "minimize chrome",
            "minimize"
        ),

        (
            "Maximize",
            "maximize chrome",
            "maximize"
        ),

        (
            "Restore",
            "restore chrome",
            "restore"
        ),

        (
            "Switch",
            "switch to chrome",
            "switch"
        ),

        # -------------------------------------------------
        # SEARCH
        # -------------------------------------------------

        (
            "Search",
            "search weather",
            "search"
        ),

        (
            "Find",
            "find weather",
            "search"
        ),

        (
            "Google",
            "google weather",
            "search"
        ),

        # -------------------------------------------------
        # MEMORY
        # -------------------------------------------------

        (
            "Remember",
            "remember my birthday",
            "remember"
        ),

        (
            "Save",
            "save my birthday",
            "remember"
        ),

        (
            "Store",
            "store my birthday",
            "remember"
        ),

        # -------------------------------------------------
        # CONVERSATION / INFORMATION
        # -------------------------------------------------

        (
            "Time",
            "what is the time",
            "time"
        ),

        (
            "Date",
            "what is the date",
            "date"
        ),

        (
            "Weather",
            "what is the weather",
            "weather"
        ),

        (
            "Weather City",
            "what is the weather in Lucknow",
            "weather"
        ),

        # -------------------------------------------------
        # IDENTITY
        # -------------------------------------------------

        (
            "Identity",
            "who are you",
            "ask_name"
        ),

        (
            "Creator",
            "who made you",
            "ask_creator"
        ),

        (
            "My Name",
            "what is my name",
            "ask_my_name"
        ),

    ]

    passed = 0
    failed = 0

    # =====================================================
    # RUN
    # =====================================================

    for name, command, expected in tests:

        result = run_test(
            name,
            command,
            expected
        )

        if result:

            passed += 1

        else:

            failed += 1

    # =====================================================
    # SUMMARY
    # =====================================================

    print("\n" + "=" * 60)
    print("📊 COMMAND VARIATION SUMMARY")
    print("=" * 60)

    print(f"Total : {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed == 0:

        print("\n🟢 ALL COMMAND VARIATION TESTS PASSED")

        return 0

    print("\n🔴 COMMAND VARIATION TESTS FAILED")

    return 1


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    raise SystemExit(
        main()
    )