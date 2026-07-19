import random

def chat(command):

    command = command.lower().strip()

    responses = {

        "who are you":
        "I am ARIS, your personal AI assistant.",

        "who made you":
        "I was created by Raj Babu Mishra.",

        "how are you":
        random.choice([
            "I am fine.",
            "Doing great.",
            "Always ready to help."
        ]),

        "what can you do":
        "I can open applications, search the internet, answer questions, remember things, control your computer and much more.",

        "thank you":
        "You're welcome.",

        "thanks":
        "My pleasure.",

        "good night":
        "Good night. Have a great sleep.",

        "good morning":
        "Good morning. Have a wonderful day."
    }

    return responses.get(command)