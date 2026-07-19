import json
import os

SYSTEM_DB = "database/system_commands.json"


def load_system():

    if not os.path.exists(SYSTEM_DB):
        return {}

    with open(SYSTEM_DB, "r", encoding="utf-8") as f:
        return json.load(f)


def execute_system(command):

    command = command.lower().strip()

    data = load_system()

    for key, value in data.items():

        if key in command:

            os.system(value)

            return f"Executing {key}"

    return None