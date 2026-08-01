import webbrowser
from urllib.parse import quote


def browser_command(command):

    command = command.lower().strip()

    # ---------- Google Search ----------

    if command.startswith("search "):

        query = command[7:].strip()

        if query:
            webbrowser.open(
                f"https://www.google.com/search?q={quote(query)}"
            )
            return f"Searching Google for {query}"

        return None

    if command.startswith("google "):

        query = command[7:].strip()

        if query:
            webbrowser.open(
                f"https://www.google.com/search?q={quote(query)}"
            )
            return f"Searching Google for {query}"

        return None

    # ---------- YouTube Search ----------

    if command.startswith("youtube "):

        query = command[8:].strip()

        if query:
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote(query)}"
            )
            return f"Searching YouTube for {query}"

        return None

    if command.startswith("play "):

        song = command[5:].strip()

        if song:
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote(song)}"
            )
            return f"Playing {song}"

        return None

    # ---------- Open Website ----------

    websites = {
        "open youtube": "https://youtube.com",
        "open google": "https://google.com",
        "open gmail": "https://mail.google.com",
        "open github": "https://github.com",
        "open chatgpt": "https://chatgpt.com",
        "open wikipedia": "https://wikipedia.org",
        "browser": None,
        "open browser": None
    }

    if command in websites:

        if websites[command] is None:
            return None

        webbrowser.open(websites[command])

        return f"Opening {command.replace('open ', '').title()}"

    return None