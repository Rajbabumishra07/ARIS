"""
ARIS V11 - Memory Engine
"""

import json
import os

MEMORY_FILE = "data/memory.json"


class Memory:

    def __init__(self):
        self.data = self.load()

    def load(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(MEMORY_FILE):

            default = {
                "owner": "Raj Babu Mishra",
                "profile": {},
                "preferences": {},
                "goals": [],
                "projects": [],
                "notes": [],
                "daily_tasks": [],
                "conversation_history": [],
                "important_memory": []
            }

            self.save(default)
            return default

        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

        except Exception:

            default = {
                "owner": "Raj Babu Mishra",
                "profile": {},
                "preferences": {},
                "goals": [],
                "projects": [],
                "notes": [],
                "daily_tasks": [],
                "conversation_history": [],
                "important_memory": []
            }

            self.save(default)
            return default

    def save(self, data=None):

        if data is not None:
            self.data = data

        os.makedirs("data", exist_ok=True)

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def remember(self, text):

        self.data["important_memory"].append(text)
        self.save()

    def add_note(self, note):

        self.data["notes"].append(note)
        self.save()

    def add_goal(self, goal):

        self.data["goals"].append(goal)
        self.save()

    def add_project(self, project):

        self.data["projects"].append(project)
        self.save()

    def add_task(self, task):

        self.data["daily_tasks"].append(task)
        self.save()

    def search(self, keyword):

        keyword = keyword.lower().strip()

        results = []

        for section in [
            "important_memory",
            "notes",
            "goals",
            "projects",
            "daily_tasks"
        ]:

            for item in self.data.get(section, []):

                if keyword in str(item).lower():
                    results.append(item)

        return results

    def add_conversation(self, user, aris):

        self.data["conversation_history"].append({
            "user": user,
            "aris": aris
        })
        if len(self.data["conversation_history"]) > 100:
            self.data["conversation_history"] = self.data["conversation_history"][-100:]

        self.save()

    def get_memory(self):

        return self.data