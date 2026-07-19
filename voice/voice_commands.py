def special_voice_command(command):

    command = command.lower()

    if command in [
        "sleep",
        "go to sleep",
        "so jao",
        "band ho jao"
    ]:
        return "sleep"

    if command in [
        "wake up",
        "hello aris",
        "hey aris"
    ]:
        return "wake"

    return None