import json
import os

OWNER_FILE = "data/owner.json"

def get_owner():
    if os.path.exists(OWNER_FILE):
        with open(OWNER_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("name", "Unknown")
    
    return "Unknown"


def creator_info():
    owner = get_owner()

    return f"My creator is {owner}."


def aris_info():
    return {
        "name": "ARIS",
        "creator": get_owner(),
        "version": "2.0"
    }