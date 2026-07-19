import json
import os
import difflib

DB = "database/commands.json"


def load_commands():

    if not os.path.exists(DB):
        return {}

    with open(DB, "r", encoding="utf-8") as f:
        return json.load(f)


def match_command(command):

    command = command.lower().strip()

    data = load_commands()

    best = None
    best_score = 0

    for action, phrases in data.items():

        for phrase in phrases:

            score = difflib.SequenceMatcher(
                None,
                command,
                phrase
            ).ratio()

            if score > best_score:
                best_score = score
                best = action

    if best_score >= 0.75:
        return best

    return None