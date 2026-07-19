from voice.state import WAKE_WORDS

def is_wake_word(command):

    command = command.lower().strip()

    for word in WAKE_WORDS:
        if word in command:
            return True

    return False