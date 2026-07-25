"""
ARIS V16.2 Smart App Launcher
Author : Raj Babu Mishra
"""

import os
import subprocess

from system.app_database import load_apps


def launch(app):

    app = app.lower().strip()

    apps = load_apps()

    if app not in apps:
        return None

    target = apps[app]

    try:

        # Windows URI Commands
        if target.startswith("start "):

            os.system(target)

            return f"Opening {app.title()}."

        # Full Path
        if os.path.isabs(target):

            os.startfile(target)

            return f"Opening {app.title()}."

        # Executable Name
        subprocess.Popen(
            [target],
            shell=False
        )

        return f"Opening {app.title()}."

    except Exception as e:

        print("Launcher Error:", e)

        return None