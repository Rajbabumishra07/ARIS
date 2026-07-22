import json
import os

FILE = "memory/learning.json"


class LearningEngine:

    def __init__(self):
        if not os.path.exists(FILE):
            with open(FILE, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def learn(self, command):

        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        command = command.lower().strip()

        data[command] = data.get(command, 0) + 1

        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def favourite(self):

        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            return None

        return max(data, key=data.get)


learning = LearningEngine()