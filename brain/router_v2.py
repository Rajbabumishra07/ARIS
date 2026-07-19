from brain.decision import decision_engine
from brain.suggestions import suggestion_engine
from brain.emotion import emotion


class BrainRouter:

    def process(self, command):

        # Step 1 : Decision

        decision = decision_engine.decide(command)

        if decision["confirm"]:

            return {

                "execute": False,

                "reply": decision["suggestion"],

                "emotion": "warning"

            }

        # Step 2 : Suggestion

        suggestion = suggestion_engine.suggest(command)

        # Step 3 : Emotion

        reply = emotion(decision["emotion"])

        return {

            "execute": True,

            "reply": reply,

            "emotion": decision["emotion"],

            "suggestion": suggestion

        }


router = BrainRouter()