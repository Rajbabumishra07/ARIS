"""
ARIS V17.3 Smart Folder Alias
Author : Raj Babu Mishra
"""

ALIASES = {

    # Desktop
    "desktop": "desktop",
    "my desktop": "desktop",

    # Downloads
    "downloads": "downloads",
    "download": "downloads",
    "my downloads": "downloads",

    # Documents
    "documents": "documents",
    "document": "documents",
    "docs": "documents",
    "my documents": "documents",

    # Pictures
    "pictures": "pictures",
    "picture": "pictures",
    "photos": "pictures",
    "images": "pictures",

    # Music
    "music": "music",
    "songs": "music",

    # Videos
    "videos": "videos",
    "video": "videos",
    "movies": "videos",

    # Drives
    "c drive": "C:",
    "d drive": "D:",
    "e drive": "E:",
    "f drive": "F:",

    # Common
    "this pc": "this_pc",
    "computer": "this_pc",

    "recycle bin": "recycle_bin",
    "bin": "recycle_bin",

    "onedrive": "onedrive"
}


def normalize_folder(name):

    name = name.lower().strip()

    return ALIASES.get(name, name)