import random


class SuggestionEngine:

    def suggest(self, command):

        command = command.lower().strip()

        if "tired" in command:
            return random.choice([
                "You have been working for a while Sir. I recommend taking a short break.",
                "A five minute break may help you focus better.",
                "Please don't forget to stay hydrated Sir."
            ])

        elif "hungry" in command:
            return random.choice([
                "You should eat something healthy before continuing your work.",
                "A healthy meal will help you stay focused."
            ])

        elif "bored" in command:
            return random.choice([
                "Would you like to continue developing ARIS?",
                "We could listen to some music or continue learning something new."
            ])

        elif "sad" in command:
            return random.choice([
                "I am here with you Sir. Tomorrow is another opportunity.",
                "Every difficult day eventually passes. Keep moving forward."
            ])

        elif "happy" in command:
            return random.choice([
                "That is wonderful to hear Sir.",
                "I am glad everything is going well."
            ])

        elif "exam" in command:
            return random.choice([
                "I recommend revising important topics instead of learning new ones today.",
                "Stay calm and revise your strongest topics first."
            ])

        return None


suggestion_engine = SuggestionEngine()


def suggestion(command):
    return suggestion_engine.suggest(command)