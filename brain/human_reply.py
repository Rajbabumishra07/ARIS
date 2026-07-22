import random


class HumanReply:

    def reply(self, intent):

        replies = {

            "GREETING": [
                "नमस्ते सर। आपका स्वागत है।",
                "हैलो सर। मैं तैयार हूँ।",
                "नमस्ते सर। आज क्या करना है?"
            ],

            "OPEN_BROWSER": [
                "जी सर। ब्राउज़र खोल रहा हूँ।",
                "अभी खोलता हूँ सर।",
                "ठीक है सर।"
            ],

            "OPEN_VSCODE": [
                "VS Code खोल रहा हूँ सर।",
                "जी सर, कोडिंग शुरू करते हैं।"
            ],

            "PLAY_MEDIA": [
                "अभी चलाता हूँ सर।",
                "ठीक है सर, शुरू कर रहा हूँ।"
            ],

            "GET_TIME": [
                "अभी समय बता रहा हूँ सर।"
            ],

            "UNKNOWN": [
                "मुझे पूरी तरह समझ नहीं आया सर।",
                "क्या आप एक बार फिर बोलेंगे?",
                "मैं सीख रहा हूँ सर, कृपया दोबारा बताइए।"
            ]

        }

        if intent in replies:
            return random.choice(replies[intent])

        return "जी सर।"


human_reply = HumanReply()