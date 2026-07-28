"""
ARIS V17.6 Folder Index
Author : Raj Babu Mishra
"""

import os

from system.folder_database import load_folders


class FolderIndex:

    def __init__(self):

        self.index = {}

    # ---------------- Build ---------------- #

    def build(self):

        self.index.clear()

        folders = load_folders()

        for base in folders.values():

            if not os.path.exists(base):
                continue

            try:

                for root, dirs, files in os.walk(base):

                    for d in dirs:

                        name = d.lower()

                        if name not in self.index:

                            self.index[name] = os.path.join(root, d)

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


folder_index = FolderIndex()