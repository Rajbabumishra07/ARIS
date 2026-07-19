import os
import json

APP_FILE = "database/apps.json"


def load_apps():

    if not os.path.exists(APP_FILE):
        return {}

    with open(APP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)