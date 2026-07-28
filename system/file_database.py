"""
ARIS V17.7 File Database
Author : Raj Babu Mishra
"""

import os


def load_locations():

    home = os.path.expanduser("~")

    return {

        "desktop": os.path.join(home, "Desktop"),

        "documents": os.path.join(home, "Documents"),

        "downloads": os.path.join(home, "Downloads"),

        "pictures": os.path.join(home, "Pictures"),

        "music": os.path.join(home, "Music"),

        "videos": os.path.join(home, "Videos"),

        "onedrive": os.path.join(home, "OneDrive"),

        "c:": "C:\\",

        "d:": "D:\\"

    }