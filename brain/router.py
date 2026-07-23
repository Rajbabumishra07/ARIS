"""
ARIS V14 - Router Engine
"""

from brain.nlu import nlu


class Router:

    def route(self, command):

        text = nlu.normalize(command)

        data = nlu.entities(text)

        return {
            "intent": data["intent"],
            "subject": data.get("query") or data.get("app") or text,
            "command": text
        }


router = Router()