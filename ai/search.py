import webbrowser


def internet_search(command):

    command = command.lower().strip()

    if command.startswith("search "):

        query = command.replace("search", "", 1)
        query = query.replace("on google", "").strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching Google for {query}"

    elif command.startswith("google "):

        query = command.replace("google", "", 1).strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching Google for {query}"

    elif command.startswith("youtube "):

        query = command.replace("youtube", "", 1).strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )

        return f"Searching YouTube for {query}"

    elif command == "gmail":

        webbrowser.open("https://mail.google.com")

        return "Opening Gmail."

    elif command == "github":

        webbrowser.open("https://github.com")

        return "Opening GitHub."

    return None