"""
ARIS V13 Decision Engine
"""

class DecisionEngine:

    def decide(self, command, reasoning=None):

        text = command.lower().strip()

        decision = {

            "allow": True,
            "warning": None,
            "reason": None

        }

        dangerous = [

            "shutdown",
            "restart",
            "format",
            "delete",
            "remove",
            "reset",
            "factory reset"

        ]

        for word in dangerous:

            if word in text:

                decision["warning"] = (
                    "यह आदेश आपके सिस्टम में महत्वपूर्ण परिवर्तन कर सकता है।"
                )

                decision["reason"] = word

                break

        return decision


decision = DecisionEngine()