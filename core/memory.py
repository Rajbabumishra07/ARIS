"""
ARIS V15 - Smart Memory Engine
Author : Raj Babu Mishra
"""

import json
import os

MEMORY_FILE = "data/memory.json"


class Memory:

    def __init__(self):

        self.data = self.load()

    # ---------------- Load ---------------- #

    def default_data(self):

        return {
            "owner": "Raj Babu Mishra",
            "profile": {},
            "preferences": {},
            "knowledge": {},
            "goals": [],
            "projects": [],
            "notes": [],
            "daily_tasks": [],
            "conversation_history": []
        }

    def load(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(MEMORY_FILE):

            data = self.default_data()

            self.save(data)

            return data

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as f:

                data = json.load(f)

        except Exception:

            data = self.default_data()

            self.save(data)

            return data

        if "knowledge" not in data:
            data["knowledge"] = {}

        return data

    # ---------------- Save ---------------- #

    def save(self, data=None):

        if data is not None:
            self.data = data

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )

    # ---------------- Remember ---------------- #

    def remember(self, text):

        text = text.lower().strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

        elif "=" in text:

            key, value = text.split("=", 1)

        else:

            self.data["notes"].append(text)

            self.save()

            return

        key = key.strip()

        value = value.strip()

        if key.startswith("my "):
            key = key[3:]

        self.data["knowledge"][key] = value

        self.save()
        # ---------------- Search ---------------- #

    def search(self, keyword):

        keyword = keyword.lower().strip()

        if keyword.startswith("my "):
            keyword = keyword[3:]

        results = []

        # Exact Key
        if keyword in self.data["knowledge"]:
            results.append(self.data["knowledge"][keyword])

        # Partial Match
        for key, value in self.data["knowledge"].items():

            if keyword in key or keyword in value.lower():

                if value not in results:
                    results.append(value)

        # Notes
        for note in self.data["notes"]:

            if keyword in note.lower():
                results.append(note)

        return results

    # ---------------- Notes ---------------- #

    def add_note(self, note):

        self.data["notes"].append(note)

        self.save()

    # ---------------- Goal ---------------- #

    def add_goal(self, goal):

        self.data["goals"].append(goal)

        self.save()

    # ---------------- Project ---------------- #

    def add_project(self, project):

        self.data["projects"].append(project)

        self.save()

    # ---------------- Task ---------------- #

    def add_task(self, task):

        self.data["daily_tasks"].append(task)

        self.save()

    # ---------------- Conversation ---------------- #

    def add_conversation(self, user, aris):

        self.data["conversation_history"].append({

            "user": user,

            "aris": aris

        })

        if len(self.data["conversation_history"]) > 100:

            self.data["conversation_history"] = (
                self.data["conversation_history"][-100:]
            )

        self.save()

    # ---------------- Get Memory ---------------- #

    def get_memory(self):

        return self.data