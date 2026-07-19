import random


EMOTION = {

    "neutral": [

        "Ji, Akshat Sir.",

        "Main sun raha hoon, Sir.",

        "Command receive ho gaya, Sir."

    ],

    "thinking": [

        "Ek moment, Sir.",

        "Main analyse kar raha hoon.",

        "Is command ko process kar raha hoon."

    ],

    "success": [

        "Task complete, Sir.",

        "Command execute ho gaya.",

        "Ho gaya, Sir."

    ],

    "warning": [

        "Sir, isme thoda risk hai.",

        "Recommend karunga ki pehle check kar lein.",

        "Kripya dhyan rakhiye, Sir."

    ],

    "error": [

        "Sir, ye command complete nahi ho saki.",

        "Ek problem aa gayi hai.",

        "Main ek aur tareeka try kar sakta hoon."

    ]

}


def emotion(name):

    if name not in EMOTION:

        return ""

    return random.choice(EMOTION[name])