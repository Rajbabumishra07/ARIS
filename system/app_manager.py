"""
ARIS V17 Stable App Manager
Author : Raj Babu Mishra
"""

import os
import json
import subprocess


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

                # Absolute executable path
                if os.path.isabs(exe):

                    os.startfile(exe)

                else:

                    subprocess.Popen(
                        exe,
                        shell=False
                    )

                return f"Opening {app.title()}."

            except Exception as e:

                print("App Manager Error:", e)

                return f"Unable to open {app.title()}."

    return None