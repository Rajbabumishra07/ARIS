import difflib
from brain.command_matcher import match_command

ALIASES = {

    "chrome kholo": "open chrome",
    "browser kholo": "open chrome",

    "vs code": "open vscode",
    "visual studio code": "open vscode",

    "google kholo": "google",

    "youtube kholo": "youtube",

    "hanuman chalisa chalao": "play hanuman chalisa",

    "gaana chalao": "play",

    "mera naam kya hai": "what is my name",

    "time batao": "time",

    "date batao": "date"
}


def normalize_command(command):

    command = command.lower().strip()

    command = command.replace("?", "")
    command = command.replace(".", "")
    command = command.replace(",", "")

    for old, new in ALIASES.items():
        command = command.replace(old, new)

    matched = match_command(command)

    if matched:
        return matched

    return command