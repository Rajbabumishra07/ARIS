"""
ARIS V11 - Advisor Engine
"""

class Advisor:

    def suggest(self, command: str):

        text = command.lower()

        if "delete" in text:
            return "सर, किसी भी महत्वपूर्ण फ़ाइल को हटाने से पहले उसका बैकअप बना लेना बेहतर रहेगा।"

        if "format" in text:
            return "सर, फ़ॉर्मेट करने से पहले आवश्यक डेटा सुरक्षित कर लें।"

        if "install" in text:
            return "सर, केवल विश्वसनीय स्रोत से ही सॉफ़्टवेयर इंस्टॉल करें।"

        if "shutdown" in text:
            return "सर, क्या आपने अपना सारा काम सेव कर लिया है?"

        return None


advisor = Advisor()