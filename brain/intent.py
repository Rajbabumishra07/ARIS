import json
from rapidfuzz import fuzz

COMMAND_FILE = "database/commands.json"


def load_commands():
    with open(COMMAND_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def detect_intent(command):

    command = command.lower().strip()

    commands = load_commands()

    best_intent = None
    best_score = 0

    for intent, phrases in commands.items():

        for phrase in phrases:

            score = fuzz.token_sort_ratio(command, phrase)

            if command == phrase:
                return intent

            if phrase in command:
                score += 10

            if score > best_score:
                best_score = score
                best_intent = intent

    # Debug sirf high confidence par
    if best_score >= 80:
        print(f"🧠 Intent: {best_intent} ({best_score:.1f})")
        return best_intent

    # 80 se kam matlab koi valid intent nahi
    return None