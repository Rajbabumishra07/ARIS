"""
ARIS V17.6 Smart Folder Operations
Author : Raj Babu Mishra
"""

import os
import shutil

from system.folder_database import load_folders
from system.folder_alias import normalize_folder
from system.folder_index import folder_index
from system.path_utils import get_path, get_base


class FolderOperations:

    def __init__(self):

        self.reload()

    # ---------------- Reload ---------------- #

    def reload(self):

        self.folders = load_folders()

        folder_index.reload()

    # ---------------- Exists ---------------- #

    def exists(self, name):

        return folder_index.exists(name)

    # ---------------- Search ---------------- #

    def search(self, name):

        path = folder_index.find(name)

        if path is None:

            return None

        return path

    # ---------------- Open ---------------- #

    def open(self, name):

        path = folder_index.find(name)

        if path is None:

            return f"Folder {name} not found."

        try:

            os.startfile(path)

            return f"Opening folder {name}."

        except Exception as e:

            print("Folder Open Error:", e)

            return "Unable to open folder."

            # ---------------- Create ---------------- #

    def create(self, name, location="desktop"):

        location = normalize_folder(location)

        base = get_base(location)

        if base is None:
            return "Location not found."

        path = os.path.join(base, name)

        try:

            if os.path.exists(path):
                return f"Folder {name} already exists."

            os.makedirs(path)

            folder_index.reload()

            return f"Folder {name} created successfully."

        except Exception as e:

            print("Folder Create Error:", e)

            return "Unable to create folder."

    # ---------------- Rename ---------------- #

    def rename(self, old_name, new_name):

        source = folder_index.find(old_name)

        if source is None:
            return f"Folder {old_name} not found."

        destination = os.path.join(
            os.path.dirname(source),
            new_name
        )

        try:

            if os.path.exists(destination):
                return f"Folder {new_name} already exists."

            os.rename(source, destination)

            folder_index.reload()

            return f"Folder {old_name} renamed to {new_name}."

        except Exception as e:

            print("Folder Rename Error:", e)

            return "Unable to rename folder."

    # ---------------- Delete ---------------- #

    def delete(self, name):

        path = folder_index.find(name)

        if path is None:
            return f"Folder {name} not found."

        try:

            if os.listdir(path):
                return f"Folder {name} is not empty."

            os.rmdir(path)

            folder_index.reload()

            return f"Folder {name} deleted successfully."

        except Exception as e:

            print("Folder Delete Error:", e)

            return "Unable to delete folder."

            # ---------------- Move ---------------- #

    def move(self, name, destination):

        source = folder_index.find(name)

        if source is None:
            return f"Folder {name} not found."

        destination = normalize_folder(destination)

        dest = get_base(destination)

        if dest is None:
            return f"Destination {destination} not found."

        target = os.path.join(dest, os.path.basename(source))

        try:

            if os.path.exists(target):
                return f"Folder {name} already exists in {destination}."

            shutil.move(source, target)

            folder_index.reload()

            return f"Folder {name} moved to {destination.title()}."

        except Exception as e:

            print("Folder Move Error:", e)

            return "Unable to move folder."

    # ---------------- Copy ---------------- #

    def copy(self, name, destination):

        source = folder_index.find(name)

        if source is None:
            return f"Folder {name} not found."

        destination = normalize_folder(destination)

        dest = get_base(destination)

        if dest is None:
            return f"Destination {destination} not found."

        target = os.path.join(dest, os.path.basename(source))

        try:

            if os.path.exists(target):
                return f"Folder {name} already exists in {destination}."

            shutil.copytree(source, target)

            folder_index.reload()

            return f"Folder {name} copied to {destination.title()}."

        except Exception as e:

            print("Folder Copy Error:", e)

            return "Unable to copy folder."


folder_operations = FolderOperations()