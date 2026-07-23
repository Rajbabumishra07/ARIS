"""
ARIS V14 Decision Engine
Author : Raj Babu Mishra
"""


class DecisionEngine:

    def __init__(self):

        self.pending_confirmation = None

    # -------------------------------- #

    def decide(self, command):

        text = command.lower().strip()

        decision = {
            "allow": True,
            "warning": None,
            "reason": None,
            "confirm": False
        }

        dangerous = {

            "shutdown":
                "यह कंप्यूटर बंद कर देगा।",

            "restart":
                "यह कंप्यूटर पुनः चालू करेगा।",

            "delete":
                "यह डेटा मिटा सकता है।",

            "remove":
                "यह महत्वपूर्ण फ़ाइल हटा सकता है।",

            "format":
                "यह स्टोरेज को पूरी तरह साफ़ कर सकता है।",

            "factory reset":
                "यह सिस्टम को फ़ैक्टरी स्थिति में ले जाएगा।",

            "reset":
                "यह सिस्टम सेटिंग्स बदल सकता है।"

        }

        for keyword, message in dangerous.items():

            if keyword in text:

                decision["allow"] = False
                decision["confirm"] = True
                decision["reason"] = keyword
                decision["warning"] = message

                self.pending_confirmation = text

                return decision

        return decision

    # -------------------------------- #

    def waiting(self):

        return self.pending_confirmation is not None

    # -------------------------------- #

    def get_pending(self):

        return self.pending_confirmation

    # -------------------------------- #

    def confirm(self):

        command = self.pending_confirmation

        self.pending_confirmation = None

        return command

    # -------------------------------- #

    def cancel(self):

        self.pending_confirmation = None


decision = DecisionEngine()