import random


def conversation(command):

    command = str(command)
    command = command.lower().strip()
    command = " ".join(command.split())

    greetings = [
        "hello",
        "hi",
        "hey"
    ]

    if command in greetings:
        return random.choice([
            "Hello Raj Babu Mishra Sir. How can I help you today?",
            "Welcome back Sir. What would you like to do?",
            "Good to see you Sir."
        ])

    elif "how are you" in command:
        return random.choice([
            "I am doing great Sir.",
            "Everything is working perfectly Sir.",
            "I am always ready to help you."
        ])

    elif "what are you doing" in command:
        return random.choice([
            "I am waiting for your next command.",
            "Thinking how I can help you better.",
            "Monitoring and ready to assist you."
        ])

    elif "thank you" in command or "thanks" in command:
        return random.choice([
            "You are welcome Sir.",
            "Always happy to help.",
            "My pleasure Sir."
        ])

    elif "good morning" in command:
        return "Good morning Sir. I hope you have an amazing day."

    elif "good night" in command:
        return "Good night Sir. Have a wonderful sleep."

    return None