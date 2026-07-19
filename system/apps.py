import json
import os
import subprocess

APP_DB = "database/apps.json"


def load_apps():

    if not os.path.exists(APP_DB):
        return {}

    try:
        with open(APP_DB, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def run_app(exe):

    try:

        if exe.startswith("start "):
            os.system(exe)
        else:
            subprocess.Popen(exe, shell=True)

        return True

    except:

        try:
            os.system(f"start {exe}")
            return True
        except:
            return False


def open_app(command):

    command = command.lower().strip()

    apps = load_apps()

    # Exact Match
    if command in apps:

        if run_app(apps[command]):
            return f"Opening {command.title()}"

    # Partial Match
    for app_name, exe in apps.items():

        if app_name in command:

            if run_app(exe):
                return f"Opening {app_name.title()}"

    # VS Code aliases
    if (
        "vs code" in command
        or "vscode" in command
        or "visual studio code" in command
    ):

        if run_app("code"):
            return "Opening VS Code."

    return None