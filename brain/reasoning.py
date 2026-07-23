"""
ARIS V12 - Reasoning Engine
"""

class ReasoningEngine:

    def think(self, command):

        text = command.lower().strip()

        # Greetings
        if text in [
            "hello",
            "hi",
            "hey",
            "namaste",
            "good morning",
            "good afternoon",
            "good evening"
        ]:
            return None

        # Advice
        if any(word in text for word in [
            "should",
            "advice",
            "suggest",
            "recommend",
            "kya karu",
            "kya karna chahiye"
        ]):

            return (
                "सर, मैं पहले परिस्थिति का विश्लेषण करूँगा, "
                "फिर आपको सबसे अच्छा सुझाव दूँगा।"
            )

        # Comparison
        if any(word in text for word in [
            "better",
            "difference",
            "compare",
            "vs",
            "or"
        ]):

            return (
                "सर, मैं दोनों विकल्पों की तुलना करके निर्णय दूँगा।"
            )

        return None


reasoning = ReasoningEngine()