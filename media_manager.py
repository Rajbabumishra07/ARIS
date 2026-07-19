import webbrowser
import urllib.parse


def play_media(command):

    command = command.lower().strip()

    if not command.startswith("play "):
        return None

    query = command.replace("play", "", 1).strip()

    if not query:
        return "Akshat Sir, kya play karna hai?"

    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(query)
    )

    webbrowser.open(url)

    return f"Playing {query}, Akshat Sir."