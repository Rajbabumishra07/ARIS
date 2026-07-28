"""
ARIS V17.3 Smart File Manager
Author : Raj Babu Mishra
"""

import os

from system.folder_database import load_folders
from system.folder_alias import normalize_folder


class FileManager:

    def __init__(self):

        self.reload()

    # ---------------- Reload ---------------- #

    def reload(self):

        self.folders = load_folders()

    # ---------------- Exists ---------------- #

    def exists(self, folder):

        folder = normalize_folder(folder)

        return folder in self.folders

    # ---------------- Path ---------------- #

    def path(self, folder):

        folder = normalize_folder(folder)

        return self.folders.get(folder)

    # ---------------- Open ---------------- #

    def open(self, folder):

        folder = normalize_folder(folder)

        if folder not in self.folders:

            return None

        path = self.folders[folder]

        try:

            os.startfile(path)

            if folder.endswith(":"):

                return f"Opening {folder} Drive."

            return f"Opening {folder.title()}."

        except Exception as e:

            print("File Manager Error:", e)

            return None


file_manager = FileManager()