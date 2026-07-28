"""
ARIS V17.8 Index Cache
Author : Raj Babu Mishra
"""

import json
import os


CACHE_DIR = "cache"

os.makedirs(CACHE_DIR, exist_ok=True)


def save_cache(name, data):

    path = os.path.join(CACHE_DIR, f"{name}.json")

    with open(path, "w", encoding="utf-8") as f:

        json.dump(data, f)


def load_cache(name):

    path = os.path.join(CACHE_DIR, f"{name}.json")

    if not os.path.exists(path):

        return None

    try:

        with open(path, "r", encoding="utf-8") as f:

            return json.load(f)

    except:

        return None