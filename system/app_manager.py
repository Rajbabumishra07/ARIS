import json
import os


APP_DB = "database/apps.json"


def load_apps():

    if not os.path.exists(APP_DB):
        return {}

    with open(APP_DB, "r", encoding="utf-8") as f:
        return json.load(f)


def open_application(command):

    command = command.lower().strip()

    apps = load_apps()

    for app, exe in apps.items():

        if app in command:

            try:

                os.system(f"start {exe}")

                return f"Opening {app}"

            except:

                return f"Unable to open {app}"

    return None