"""
ARIS V14 Memory Engine
Author : Raj Babu Mishra
"""

import json
import os

MEMORY_FILE = "data/memory.json"


class Memory:

    def __init__(self):
        self.data = self.load()

    # -------------------------------- #

    def default(self):

        return {

            "owner": "Raj Babu Mishra",

            "profile": {},

            "preferences": {},

            "knowledge": {},

            "goals": [],

            "projects": [],

            "notes": [],

            "daily_tasks": [],

            "conversation_history": [],

            "important_memory": []

        }

    # -------------------------------- #

    def load(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(MEMORY_FILE):

            data = self.default()

            self.save(data)

            return data

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as f:

                return json.load(f)

        except Exception:

            data = self.default()

            self.save(data)

            return data

    # -------------------------------- #

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

    # -------------------------------- #

    def remember(self, text):

        text = text.strip()

        if not text:
            return False

        low = text.lower()

        if " is " in low:

            key, value = low.split(" is ", 1)

            self.data["knowledge"][key.strip()] = value.strip()

            self.save()

            return True

        if text not in self.data["important_memory"]:

            self.data["important_memory"].append(text)

            self.save()

        return True

    # -------------------------------- #

    def search(self, keyword):

        keyword = keyword.lower().strip()

        results = []

        for key, value in self.data["knowledge"].items():

            if keyword in key.lower():

                results.append(f"{key} is {value}")

        for section in [

            "important_memory",

            "notes",

            "goals",

            "projects",

            "daily_tasks"

        ]:

            for item in self.data.get(section, []):

                if keyword in str(item).lower():

                    if item not in results:

                        results.append(item)

        return results

    # -------------------------------- #

    def forget(self, keyword):

        keyword = keyword.lower().strip()

        if keyword in self.data["knowledge"]:

            del self.data["knowledge"][keyword]

            self.save()

            return True

        removed = False

        for item in list(self.data["important_memory"]):

            if keyword in item.lower():

                self.data["important_memory"].remove(item)

                removed = True

        if removed:
            self.save()

        return removed

    # -------------------------------- #

    def add_note(self, note):

        if note not in self.data["notes"]:

            self.data["notes"].append(note)

            self.save()

    # -------------------------------- #

    def add_goal(self, goal):

        if goal not in self.data["goals"]:

            self.data["goals"].append(goal)

            self.save()

    # -------------------------------- #

    def add_project(self, project):

        if project not in self.data["projects"]:

            self.data["projects"].append(project)

            self.save()

    # -------------------------------- #

    def add_task(self, task):

        if task not in self.data["daily_tasks"]:

            self.data["daily_tasks"].append(task)

            self.save()

    # -------------------------------- #

    def add_conversation(self, user, aris):

        self.data["conversation_history"].append({

            "user": user,

            "aris": aris

        })

        self.data["conversation_history"] = self.data[
            "conversation_history"
        ][-100:]

        self.save()

    # -------------------------------- #

    def get_memory(self):

        return self.data


memory = Memory()