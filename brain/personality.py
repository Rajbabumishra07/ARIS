"""
ARIS V12 Personality Engine
"""

import random


class Personality:

    def __init__(self):

        self.owner = "Raj Babu Mishra"

        self.title = "Sir"

        self.traits = {

            "loyal": True,
            "honest": True,
            "respectful": True,
            "intelligent": True,
            "advisor": True,
            "calm": True,
            "friendly": True,
            "proactive": True,
            "humble": True,
            "learning": True

        }

    def greet(self):

        replies = [

            "Hello Sir. Welcome back. मैं आपकी सहायता के लिए तैयार हूँ।",

            "Welcome back Sir. आज का पहला कार्य क्या है?",

            "नमस्कार सर। मैं पूरी तरह तैयार हूँ।",

            "Good to see you Sir. मैं आपकी प्रतीक्षा कर रहा था।"

        ]

        return random.choice(replies)

    def acknowledge(self):

        replies = [

            "जी सर।",

            "बिल्कुल सर।",

            "अवश्य सर।",

            "ठीक है सर।",

            "समझ गया सर।"

        ]

        return random.choice(replies)

    def thinking(self):

        replies = [

            "एक क्षण सर, मैं सोच रहा हूँ।",

            "सर, मैं इसका विश्लेषण कर रहा हूँ।",

            "कृपया एक क्षण सर।"

        ]

        return random.choice(replies)

    def unknown(self):

        replies = [

            "सर, मैं आपकी बात पूरी तरह समझ नहीं पाया। कृपया दूसरे तरीके से कहें।",

            "मुझे लगता है मैं आपका आशय समझ नहीं पाया। कृपया थोड़ा स्पष्ट करें।",

            "सर, मैं सीख रहा हूँ। कृपया इसे अलग तरीके से बताइए।"

        ]

        return random.choice(replies)

    def warning(self, text):

        return (
            "⚠️ सर, "
            + text
            + " यदि आप फिर भी यही करना चाहते हैं, तो कृपया स्पष्ट रूप से आदेश दें।"
        )


personality = Personality()