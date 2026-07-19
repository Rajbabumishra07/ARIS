REPLACE = {

    # Wake Word
    "airis": "aris",
    "arris": "aris",
    "iris": "aris",
    "hey iris": "hey aris",
    "hi aris": "hey aris",

    # VS Code
    "best code": "vs code",
    "vscoat": "vs code",
    "visual code": "visual studio code",
    "visual studio": "visual studio code",

    # Chrome
    "chrom": "chrome",
    "krom": "chrome",
    "crome": "chrome",

    # Google
    "gogle": "google",
    "googal": "google",

    # YouTube
    "utube": "youtube",
    "you tube": "youtube",

    # Hanuman Chalisa
    "hanuman challenge": "hanuman chalisa",
    "hanuman chalisha": "hanuman chalisa",
    "hanuman chalisa ji": "hanuman chalisa",

    # Commands
    "google kholo": "google",
    "youtube kholo": "youtube",
    "chrome kholo": "open chrome",
    "code kholo": "open vscode",
    "vs code kholo": "open vscode",

    "time batao": "time",
    "samay batao": "time",
    "date batao": "date",
    "aaj ki date": "date"
}


def correct(text):

    text = text.lower().strip()

    for old, new in REPLACE.items():
        text = text.replace(old, new)

    return text