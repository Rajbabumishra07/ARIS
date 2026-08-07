"""
ARIS V18 Smart File Operations
Author : Raj Babu Mishra
"""

import os
import shutil

from system.file_index import file_index
from system.file_alias import normalize_location
from system.path_utils import get_base


class FileOperations:

    def __init__(self):
        pass

    # ---------------- Reload ---------------- #

    def reload(self):
        file_index.reload()

    # ---------------- Exists ---------------- #

    def exists(self, name):
        return file_index.exists(name)

    # ---------------- Search ---------------- #

    def search(self, name):
        return file_index.find(name)

    # ---------------- Open ---------------- #

    def open(self, name):

        path = file_index.find(name)

        if path is None:
            return f"File {name} not found."

        try:
            os.startfile(path)
            return f"Opening {name}."

        except Exception as e:
            print("File Open Error:", e)
            return "Unable to open file."

    # ---------------- Create ---------------- #

    def create(self, name, location="desktop"):

        location = normalize_location(location)
        base = get_base(location)

        if base is None:
            return "Location not found."

        path = os.path.join(base, name)

        try:

            if os.path.exists(path):
                return f"File {name} already exists."

            with open(path, "w", encoding="utf-8"):
                pass

            file_index.add(path)

            return f"File {name} created successfully."

        except Exception as e:
            print("File Create Error:", e)
            return "Unable to create file."

    # ---------------- Rename ---------------- #

    def rename(self, old_name, new_name):

        source = file_index.find(old_name)

        if source is None:
            return f"File {old_name} not found."

        destination = os.path.join(
            os.path.dirname(source),
            new_name
        )

        try:

            if os.path.exists(destination):
                return f"File {new_name} already exists."

            os.rename(source, destination)

            file_index.rename(old_name, destination)

            return f"File {old_name} renamed to {new_name}."

        except Exception as e:
            print("File Rename Error:", e)
            return "Unable to rename file."

    # ---------------- Delete ---------------- #

    def delete(self, name):

        path = file_index.find(name)

        if path is None:
            return f"File {name} not found."

        try:

            os.remove(path)

            file_index.remove(name)

            return f"File {name} deleted successfully."

        except Exception as e:
            print("File Delete Error:", e)
            return "Unable to delete file."

    # ---------------- Move ---------------- #

    def move(self, name, destination):

        source = file_index.find(name)

        if source is None:
            return f"File {name} not found."

        destination = normalize_location(destination)

        dest = get_base(destination)

        if dest is None:
            return f"Destination {destination} not found."

        target = os.path.join(dest, os.path.basename(source))

        try:

            if os.path.exists(target):
                return f"File {name} already exists in {destination}."

            shutil.move(source, target)

            file_index.rename(name, target)

            return f"File {name} moved to {destination.title()}."

        except Exception as e:
            print("File Move Error:", e)
            return "Unable to move file."

    # ---------------- Copy ---------------- #

    def copy(self, name, destination):

        source = file_index.find(name)

        if source is None:
            return f"File {name} not found."

        destination = normalize_location(destination)

        dest = get_base(destination)

        if dest is None:
            return f"Destination {destination} not found."

        target = os.path.join(dest, os.path.basename(source))

        try:

            if os.path.exists(target):
                return f"File {name} already exists in {destination}."

            shutil.copy2(source, target)

            file_index.add(target)

            return f"File {name} copied to {destination.title()}."

        except Exception as e:
            print("File Copy Error:", e)
            return "Unable to copy file."


file_operations = FileOperations()