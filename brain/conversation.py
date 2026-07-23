"""
ARIS V12 - Conversation Engine
"""

from datetime import datetime
import random


class ConversationEngine:

    def greeting(self):

        hour = datetime.now().hour

        if 5 <= hour < 12:

            greetings = [
                "Good Morning, Sir. आशा है आपका दिन शानदार रहेगा।",
                "सुप्रभात सर। मैं आपकी सहायता के लिए तैयार हूँ।",
                "Good Morning, Sir. आज हम क्या शुरू करें?"
            ]

        elif 12 <= hour < 17:

            greetings = [
                "Good Afternoon, Sir.",
                "नमस्कार सर। मैं आपकी सहायता के लिए तैयार हूँ।",
                "Good Afternoon, Sir. आज का अगला कार्य क्या है?"
            ]

        elif 17 <= hour < 22:

            greetings = [
                "Good Evening, Sir.",
                "शुभ संध्या सर। Welcome back.",
                "Good Evening, Sir. मैं आपकी प्रतीक्षा कर रहा था।"
            ]

        else:

            greetings = [
                "Hello Sir. इतनी रात में भी मैं आपके साथ हूँ।",
                "Welcome back, Sir.",
                "Hello Sir. मैं तैयार हूँ।"
            ]

        return random.choice(greetings)

    def unknown(self):

        replies = [

            "सर, मैं आपकी बात पूरी तरह नहीं समझ पाया। कृपया थोड़ा अलग तरीके से कहें।",

            "मुझे लगता है मैं आपका आशय पूरी तरह नहीं समझ सका। क्या आप इसे दोबारा बताएँगे?",

            "सर, मैं सीख रहा हूँ। कृपया इसे थोड़ा और स्पष्ट करें।",

            "मैं समझना चाहता हूँ कि आप वास्तव में क्या करना चाहते हैं।"

        ]

        return random.choice(replies)

    def thinking(self):

        replies = [

            "एक क्षण सर, मैं सोच रहा हूँ।",

            "जी सर, मैं इसका विश्लेषण कर रहा हूँ।",

            "सर, मैं सबसे उपयुक्त उत्तर खोज रहा हूँ।"

        ]

        return random.choice(replies)


conversation = ConversationEngine()