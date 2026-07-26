"""
ARIS V16.5 Smart App Alias Engine
Author : Raj Babu Mishra
"""

ALIASES = {

    # Chrome
    "chrome": "chrome",
    "browser": "chrome",
    "google chrome": "chrome",
    "chrome browser": "chrome",

    # VS Code
    "vscode": "vscode",
    "vs code": "vscode",
    "visual studio": "vscode",
    "visual studio code": "vscode",
    "code": "vscode",

    # Calculator
    "calculator": "calculator",
    "calc": "calculator",

    # Notepad
    "notepad": "notepad",
    "note pad": "notepad",

    # Paint
    "paint": "paint",
    "ms paint": "paint",

    # Explorer
    "explorer": "explorer",
    "file explorer": "explorer",

    # Settings
    "settings": "settings",
    "setting": "settings",

    # Camera
    "camera": "camera",
    "cam": "camera",

    # Photos
    "photos": "photos",
    "photo": "photos",

    # CMD
    "cmd": "cmd",
    "command prompt": "cmd",

    # PowerShell
    "powershell": "powershell",
    "power shell": "powershell",

    # Task Manager
    "task manager": "task manager",

    # Control Panel
    "control panel": "control panel"
}


def normalize_app(name):

    name = name.lower().strip()

    if name in ALIASES:
        return ALIASES[name]

    return name