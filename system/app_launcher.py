"""
ARIS V16.5 Smart App Launcher
Author : Raj Babu Mishra
"""

import os
import subprocess

from system.app_database import load_apps
from system.app_alias import normalize_app


def launch(app):

    app = normalize_app(app)

    apps = load_apps()

    if app not in apps:
        return None

    target = apps[app]

    try:

        # ---------------- Windows URI ---------------- #

        if target.startswith("ms-settings:"):

            os.startfile(target)

            return "Opening Settings."

        if target.startswith("microsoft.windows.camera:"):

            os.startfile(target)

            return "Opening Camera."

        if target.startswith("ms-photos:"):

            os.startfile(target)

            return "Opening Photos."

        if target.startswith("ms-windows-store:"):

            os.startfile(target)

            return "Opening Microsoft Store."

        # ---------------- Executable Path ---------------- #

        if os.path.isabs(target):

            os.startfile(target)

            return f"Opening {app.title()}."

        # ---------------- Executable Name ---------------- #

        subprocess.Popen(
            target,
            shell=False
        )

        return f"Opening {app.title()}."

    except Exception as e:

        print("Launcher Error:", e)

        return None