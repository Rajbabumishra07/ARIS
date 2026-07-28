"""
ARIS V17.7 Smart File Index
Author : Raj Babu Mishra
"""

import os

from system.file_database import load_locations


class FileIndex:

    def __init__(self):

        self.index = {}

    # ---------------- Build ---------------- #

    def build(self):

        self.index.clear()

        locations = load_locations()

        for base in locations.values():

            if not os.path.exists(base):
                continue

            try:

                for root, dirs, files in os.walk(base):

                    for file in files:

                        name = file.lower()

                        if name not in self.index:

                            self.index[name] = os.path.join(root, file)

            except Exception:

                pass

    # ---------------- Find ---------------- #

    def find(self, name):

        return self.index.get(name.lower())

    # ---------------- Exists ---------------- #

    def exists(self, name):

        return name.lower() in self.index

    # ---------------- Reload ---------------- #

    def reload(self):

        self.build()


file_index = FileIndex()