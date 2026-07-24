"""
ARIS V15 Memory System
Author : Raj Babu Mishra
"""

import json
import os
from datetime import datetime


class Memory:

    def __init__(self):

        self.file = os.path.join(
            os.path.dirname(__file__),
            "memory.json"
        )

        self.data = self.default()

        self.load()

    # ---------------- Default ---------------- #

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

    # ---------------- Load ---------------- #

    def load(self):

        if not os.path.exists(self.file):

            self.save()

            return

        with open(self.file, "r", encoding="utf-8") as f:

            self.data = json.load(f)
            # ---------------- Save ---------------- #

    def save(self):

        with open(self.file, "w", encoding="utf-8") as f:

            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )

    # ---------------- Remember ---------------- #

    def remember(self, text):

        text = text.strip()

        if not text:
            return

        if text.startswith("my name is"):

            value = text.replace(
                "my name is",
                "",
                1
            ).strip()

            self.data["profile"]["name"] = value

            self.save()

            return

        if text.startswith("my favorite color is"):

            value = text.replace(
                "my favorite color is",
                "",
                1
            ).strip()

            self.data["preferences"]["favorite_color"] = value

            self.save()

            return

        if "=" in text:

            key, value = text.split("=", 1)

            self.data["knowledge"][key.strip()] = value.strip()

            self.save()

            return

        if ":" in text:

            key, value = text.split(":", 1)

            self.data["knowledge"][key.strip()] = value.strip()

            self.save()

            return

        self.data["important_memory"].append(text)

        self.save()
        # ---------------- Search ---------------- #

    def search(self, keyword):

        keyword = keyword.lower().strip()

        results = []

        # Profile
        for key, value in self.data["profile"].items():

            if keyword in key.lower() or keyword in str(value).lower():
                results.append(f"{key}: {value}")

        # Preferences
        for key, value in self.data["preferences"].items():

            if keyword in key.lower() or keyword in str(value).lower():
                results.append(f"{key}: {value}")

        # Knowledge
        for key, value in self.data["knowledge"].items():

            if keyword in key.lower() or keyword in str(value).lower():
                results.append(f"{key}: {value}")

        # Other Lists
        for section in [
            "important_memory",
            "notes",
            "goals",
            "projects",
            "daily_tasks"
        ]:

            for item in self.data.get(section, []):

                if keyword in str(item).lower():
                    results.append(str(item))

        return results

    # ---------------- Notes ---------------- #

    def add_note(self, note):

        self.data["notes"].append(note)

        self.save()

    # ---------------- Goals ---------------- #

    def add_goal(self, goal):

        self.data["goals"].append(goal)

        self.save()

    # ---------------- Projects ---------------- #

    def add_project(self, project):

        self.data["projects"].append(project)

        self.save()

    # ---------------- Tasks ---------------- #

    def add_task(self, task):

        self.data["daily_tasks"].append(task)

        self.save()
        # ---------------- Conversation ---------------- #

    def add_conversation(self, user, aris):

        self.data["conversation_history"].append({

            "time": datetime.now().strftime("%d-%m-%Y %H:%M"),

            "user": user,

            "aris": aris

        })

        if len(self.data["conversation_history"]) > 100:

            self.data["conversation_history"] = \
                self.data["conversation_history"][-100:]

        self.save()

    # ---------------- Getters ---------------- #

    def get_profile(self):

        return self.data.get("profile", {})

    def get_preferences(self):

        return self.data.get("preferences", {})

    def get_knowledge(self):

        return self.data.get("knowledge", {})

    def get_memory(self):

        return self.data

    # ---------------- Clear ---------------- #

    def clear(self):

        self.data = self.default()

        self.save()


memory = Memory()
# -------------------------------------------------
# Backward Compatibility
# -------------------------------------------------

def get(key, default=None):
    return memory.get_memory().get(key, default)


def save():
    memory.save()


def remember(text):
    memory.remember(text)


def search(keyword):
    return memory.search(keyword)


def add_note(note):
    memory.add_note(note)


def add_goal(goal):
    memory.add_goal(goal)


def add_project(project):
    memory.add_project(project)


def add_task(task):
    memory.add_task(task)


def add_conversation(user, aris):
    memory.add_conversation(user, aris)


def get_profile():
    return memory.get_profile()


def get_preferences():
    return memory.get_preferences()


def get_knowledge():
    return memory.get_knowledge()


def get_memory():
    return memory.get_memory()