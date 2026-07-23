"""
ARIS V12 - Router Engine
"""

from brain.intent import intent


class Router:

    def route(self, command):

        current_intent = intent.detect(command)

        subject = intent.extract_subject(command)

        return {

            "intent": current_intent,
            "subject": subject,
            "command": command

        }


router = Router()