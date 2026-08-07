"""
ARIS V18 Smart File Index
Author : Raj Babu Mishra
"""

import json
import os

from system.file_database import load_locations


CACHE_DIR = "cache"
CACHE_FILE = os.path.join(CACHE_DIR, "file_index.json")


class FileIndex:

    def __init__(self):

        self.index = {}
        self.loaded = False

    # ---------------- Cache ---------------- #

    def _load_cache(self):

        if not os.path.exists(CACHE_FILE):
            return False

        try:

            with open(CACHE_FILE, "r", encoding="utf-8") as f:

                self.index = json.load(f)

            return True

        except Exception:

            self.index = {}

            return False

    def _save_cache(self):

        os.makedirs(CACHE_DIR, exist_ok=True)

        with open(CACHE_FILE, "w", encoding="utf-8") as f:

            json.dump(
                self.index,
                f,
                indent=2,
                ensure_ascii=False
            )

    # ---------------- Build ---------------- #

    def build(self):

        self.index.clear()

        locations = load_locations()

        for base in locations.values():

            if not os.path.isdir(base):
                continue

            try:

                for root, _, files in os.walk(base):

                    for file in files:

                        key = file.lower()

                        if key not in self.index:

                            self.index[key] = os.path.join(root, file)

            except Exception:

                pass

        self._save_cache()

        self.loaded = True

    # ---------------- Ensure ---------------- #

    def ensure_loaded(self):

        if self.loaded:
            return

        if self._load_cache():

            self.loaded = True

            return

        self.build()

    # ---------------- Find ---------------- #

    def find(self, name):

        self.ensure_loaded()

        return self.index.get(name.lower())

    # ---------------- Exists ---------------- #

    def exists(self, name):

        self.ensure_loaded()

        return name.lower() in self.index

    # ---------------- Update ---------------- #

    def add(self, path):

        self.ensure_loaded()

        name = os.path.basename(path).lower()

        self.index[name] = path

        self._save_cache()

    def remove(self, name):

        self.ensure_loaded()

        self.index.pop(name.lower(), None)

        self._save_cache()

    def rename(self, old_name, new_path):

        self.ensure_loaded()

        self.index.pop(old_name.lower(), None)

        self.index[os.path.basename(new_path).lower()] = new_path

        self._save_cache()

    # ---------------- Reload ---------------- #

    def reload(self):

        self.loaded = False


file_index = FileIndex()