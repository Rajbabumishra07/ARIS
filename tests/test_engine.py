"""
ARIS V18
P1.8 Step 1
Regression Test Layer

Author : Raj Babu Mishra

Purpose:
Verify that critical ARIS commands continue
to work while new features are added.
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
# ARIS ENGINE
# =========================================================

from core.engine import engine


# =========================================================
# TEST HELPER
# =========================================================

def run_test(name, command, expected=None):

    print(f"\n🧪 TEST: {name}")
    print(f"   Command : {command}")

    try:

        result = engine.process(command)

        print(f"   Result  : {result}")

        if result is None:

            print("   ❌ FAIL")

            return False

        if expected is not None:

            if expected.lower() not in str(result).lower():

                print(
                    f"   ❌ FAIL "
                    f"(expected: {expected})"
                )

                return False

        print("   ✅ PASS")

        return True

    except Exception as error:

        print(f"   ❌ ERROR: {error}")

        return False


# =========================================================
# REGRESSION TESTS
# =========================================================

def main():

    print("=" * 60)
    print("🤖 ARIS P1.8 REGRESSION TEST")
    print("=" * 60)

    tests = [

        (
            "Time",
            "time",
            None
        ),

        (
            "Date",
            "date",
            None
        ),

        (
            "Month",
            "month",
            None
        ),

        (
            "Year",
            "year",
            None
        ),

        (
            "Calendar",
            "calendar",
            None
        ),

        (
            "Weather",
            "weather",
            "Weather"
        ),

        (
            "Delhi Weather",
            "weather Delhi",
            "Weather"
        ),

        (
            "Lucknow Weather",
            "what is the weather in Lucknow",
            "Weather"
        ),

        (
            "Identity",
            "who are you",
            "ARIS"
        ),

        (
            "Creator",
            "who made you",
            "Raj"
        ),

    ]

    passed = 0
    failed = 0

    # =====================================================
    # RUN TESTS
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
    print("📊 REGRESSION TEST SUMMARY")
    print("=" * 60)

    print(f"Total : {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    # =====================================================
    # FINAL RESULT
    # =====================================================

    if failed == 0:

        print("\n🟢 ALL TESTS PASSED")
        print("ARIS P1.8 baseline is stable.")

        return 0

    print("\n🔴 SOME TESTS FAILED")
    print("Do not continue to the next milestone.")

    return 1


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    raise SystemExit(
        main()
    )