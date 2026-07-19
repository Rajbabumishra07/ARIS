ALIASES = {

    "open": [

        "open",
        "khol",
        "khol do",
        "start",
        "launch",
        "chalu karo",
        "chalao"

    ],

    "play": [

        "play",
        "laga do",
        "chala do",
        "sunao",
        "sunao",
        "music",
        "gaana"

    ],

    "close": [

        "close",
        "band",
        "band karo",
        "shutdown"

    ]

}


def normalize(command):

    text = command.lower()

    for real, words in ALIASES.items():

        for word in words:

            if word in text:

                text = text.replace(word, real)

    return text.strip()