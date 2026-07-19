import json
import os
import datetime

MEMORY_FILE = "memory/brain_memory.json"


class MemoryCore:

    def __init__(self):

        if not os.path.exists(MEMORY_FILE):

            data = {

                "user": {},

                "preferences": {},

                "goals": [],

                "conversation": [],

                "projects": {},

                "knowledge": {},

                "experience": []

            }

            with open(MEMORY_FILE, "w", encoding="utf-8") as f:

                json.dump(data, f, indent=4)

    def load(self):

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    def save(self, data):

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:

            json.dump(data, f, indent=4)

    def remember(self, key, value):

        data = self.load()

        data["knowledge"][key] = value

        self.save(data)

    def recall(self, key):

        data = self.load()

        return data["knowledge"].get(key)

    def add_conversation(self, user, aris):

        data = self.load()

        data["conversation"].append({

            "time": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),

            "user": user,

            "aris": aris

        })

        self.save(data)


memory = MemoryCore()