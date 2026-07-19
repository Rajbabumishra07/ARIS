from rapidfuzz import process, fuzz

COMMANDS = [

    "open chrome",
    "open vscode",
    "open calculator",
    "open notepad",
    "open paint",
    "open cmd",

    "google",
    "youtube",
    "gmail",
    "github",

    "play",
    "search",
    "wiki",

    "time",
    "date",

    "weather",
    "news",
    "translate",

    "what is my name",
    "my name is",
    "what do you remember",

    "hello",
    "hi",
    "hey"
]


def match_command(command):

    command = command.lower().strip()

    # Exact match
    if command in COMMANDS:
        return command

    match = process.extractOne(
        command,
        COMMANDS,
        scorer=fuzz.ratio
    )

    # Only accept very high confidence matches
    if match and match[1] >= 95:
        return match[0]

    return None