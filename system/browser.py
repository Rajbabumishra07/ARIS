import webbrowser
from urllib.parse import quote


def browser_command(command):

    command = command.lower().strip()

    # ---------- Google ----------

    if command.startswith("search "):

        query = command.replace("search", "", 1).strip()

        webbrowser.open(
            f"https://www.google.com/search?q={quote(query)}"
        )

        return f"Searching Google for {query}"

    if command.startswith("google "):

        query = command.replace("google", "", 1).strip()

        webbrowser.open(
            f"https://www.google.com/search?q={quote(query)}"
        )

        return f"Searching Google for {query}"

    # ---------- YouTube ----------

    if command.startswith("youtube "):

        query = command.replace("youtube", "", 1).strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={quote(query)}"
        )

        return f"Searching YouTube for {query}"

    if command.startswith("play "):

        song = command.replace("play", "", 1).strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={quote(song)}"
        )

        return f"Playing {song}"

    # ---------- Websites ----------

    websites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "gmail": "https://mail.google.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
        "wikipedia": "https://wikipedia.org"
    }

    if command in websites:

        webbrowser.open(websites[command])

        return f"Opening {command.title()}"

    return None