import json
import os

DB_FILE = "database/memory.json"


def load_memory():

    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(data):

    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def remember(key, value):

    data = load_memory()

    data[key] = value

    save_memory(data)


def recall(key):

    data = load_memory()

    return data.get(key)


def recall_all():

    return load_memory()