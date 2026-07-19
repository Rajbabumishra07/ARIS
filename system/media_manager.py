import json
import os
import webbrowser

MEDIA_DB = "database/media_commands.json"


def play_media(command):

    command = command.lower()

    if not os.path.exists(MEDIA_DB):
        return None

    with open(MEDIA_DB, "r", encoding="utf-8") as f:

        songs = json.load(f)

    for key, value in songs.items():

        if key in command:

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={value}"
            )

            return f"Playing {value}"

    return None