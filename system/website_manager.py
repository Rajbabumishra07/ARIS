import json
import os
import webbrowser

WEB_DB = "database/websites.json"


def load_sites():

    if not os.path.exists(WEB_DB):
        return {}

    with open(WEB_DB, "r", encoding="utf-8") as f:
        return json.load(f)


def open_website(command):

    command = command.lower().strip()

    sites = load_sites()

    for site, url in sites.items():

        if site in command:

            webbrowser.open(url)

            return f"Opening {site}"

    return None