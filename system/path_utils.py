"""
ARIS V17 Path Utilities
Author : Raj Babu Mishra
"""

import os

from system.folder_database import load_folders
from system.folder_alias import normalize_folder


def get_base(location="desktop"):

    folders = load_folders()

    location = normalize_folder(location)

    return folders.get(location)


def get_path(name, location="desktop"):

    base = get_base(location)

    if base is None:
        return None

    return os.path.join(base, name)