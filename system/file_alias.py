"""
ARIS V17.7 File Alias
Author : Raj Babu Mishra
"""

ALIASES = {

    "desktop": "desktop",

    "desk top": "desktop",

    "deskjob": "desktop",

    "desk job": "desktop",

    "documents": "documents",

    "document": "documents",

    "docs": "documents",

    "downloads": "downloads",

    "download": "downloads",

    "pictures": "pictures",

    "picture": "pictures",

    "photos": "pictures",

    "photo": "pictures",

    "music": "music",

    "songs": "music",

    "videos": "videos",

    "video": "videos",

    "onedrive": "onedrive"

}


def normalize_location(name):

    return ALIASES.get(name.lower().strip(), name.lower().strip())