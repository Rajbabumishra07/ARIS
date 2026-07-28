"""
ARIS V17.3 Smart Folder Database
Author : Raj Babu Mishra
"""

import os
from pathlib import Path


def load_folders():

    home = Path.home()

    folders = {

        "desktop": str(home / "Desktop"),

        "downloads": str(home / "Downloads"),

        "documents": str(home / "Documents"),

        "pictures": str(home / "Pictures"),

        "music": str(home / "Music"),

        "videos": str(home / "Videos"),

        "onedrive": str(home / "OneDrive"),

        "C:": "C:\\",

        "D:": "D:\\",

        "E:": "E:\\",

        "F:": "F:\\"

    }

    # Remove folders that don't exist

    valid = {}

    for name, path in folders.items():

        if os.path.exists(path):

            valid[name] = path

    return valid