"""
ARIS V17 Entity Manager
Author : Raj Babu Mishra
"""

from system.app_database import load_apps
from system.app_alias import normalize_app


class EntityManager:

    def __init__(self):
        self.reload()

    # ---------------- Reload ---------------- #

    def reload(self):

        self.apps = load_apps()

    # ---------------- All Apps ---------------- #

    def get_all_apps(self):

        return list(self.apps.keys())

    # ---------------- Normalize ---------------- #

    def normalize(self, name):

        return normalize_app(name)

    # ---------------- Exists ---------------- #

    def exists(self, name):

        name = normalize_app(name)

        return name in self.apps

    # ---------------- Is App ---------------- #

    def is_app(self, name):

        return self.exists(name)

    # ---------------- Executable ---------------- #

    def executable(self, name):

        name = normalize_app(name)

        return self.apps.get(name)

    # ---------------- Get Target ---------------- #

    def get(self, name):

        return self.executable(name)

    # ---------------- Search ---------------- #

    def search(self, text):

        text = normalize_app(text.lower().strip())

        matches = []

        for app in self.apps.keys():

            if text in app:

                matches.append(app)

        return matches


entities = EntityManager()