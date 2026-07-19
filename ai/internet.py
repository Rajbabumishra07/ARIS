def detect_intent(command):

    command = command.lower().strip()

    if command.startswith("play "):
        return "play"

    if command.startswith("search "):
        return "search"

    if command.startswith("google "):
        return "google"

    if command.startswith("youtube "):
        return "youtube"

    if command.startswith("wiki "):
        return "wiki"

    if command.startswith("calculate "):
        return "calculate"

    if command.startswith("open "):
        return "open"

    return "normal"