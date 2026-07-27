"""
ARIS V17.1 Close Application Engine
Author : Raj Babu Mishra
"""

import psutil

from brain.entities import entities


PROCESS_NAMES = {

    "chrome": [
        "chrome.exe"
    ],

    "vscode": [
        "Code.exe"
    ],

    "calculator": [
        "CalculatorApp.exe",
        "calc.exe"
    ],

    "camera": [
        "WindowsCamera.exe"
    ],

    "paint": [
        "mspaint.exe"
    ],

    "notepad": [
        "notepad.exe"
    ],

    "explorer": [
        "explorer.exe"
    ],

    "cmd": [
        "cmd.exe"
    ],

    "powershell": [
        "powershell.exe",
        "pwsh.exe"
    ]

}


def close(app):

    app = entities.normalize(app)

    if app not in PROCESS_NAMES:
        return None

    targets = [x.lower() for x in PROCESS_NAMES[app]]

    closed = False

    for process in psutil.process_iter(["name"]):

        try:

            name = process.info["name"]

            if not name:
                continue

            if name.lower() in targets:

                process.terminate()

                closed = True

        except Exception:
            pass

    if closed:
        return f"Closing {app.title()}."

    return f"{app.title()} is not running."