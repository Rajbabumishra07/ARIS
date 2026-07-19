import random


class ThinkingEngine:

    def __init__(self):
        self.last_task = None

    def analyse(self, command):

        command = command.lower().strip()

        self.last_task = command

        result = {
            "command": command,
            "type": "normal",
            "priority": 1,
            "suggestion": None,
            "confirm": False
        }

        # Dangerous Commands

        dangerous = [
            "delete",
            "format",
            "shutdown",
            "restart",
            "reset",
            "remove"
        ]

        for word in dangerous:

            if word in command:

                result["type"] = "danger"

                result["priority"] = 10

                result["confirm"] = True

                result["suggestion"] = (
                    "Sir, ye action system ko affect kar sakta hai."
                )

                return result

        # Browser

        if "chrome" in command or "browser" in command:

            result["type"] = "browser"

            result["priority"] = 5

        # Coding

        elif "code" in command or "python" in command:

            result["type"] = "coding"

            result["priority"] = 6

        # Music

        elif "play" in command:

            result["type"] = "media"

            result["priority"] = 4

        return result


brain = ThinkingEngine()