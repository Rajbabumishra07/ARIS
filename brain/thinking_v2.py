class ThinkingV2:

    def analyse(self, command):

        text = nlp.normalize(command)

        data = {
            "intent": "unknown",
            "priority": 1,
            "danger": False,
            "confirm": False,
            "confidence": 0
        }

        # ---------- Browser ----------

        if any(x in text for x in [
            "chrome",
            "google",
            "browser"
        ]):

            data["intent"] = "browser"
            data["confidence"] = 95

        # ---------- VS Code ----------

        elif any(x in text for x in [
            "vs code",
            "vscode",
            "code"
        ]):

            data["intent"] = "coding"
            data["confidence"] = 95

        # ---------- Music ----------

        elif any(x in text for x in [
            "play",
            "song",
            "music",
            "hanuman chalisa",
            "bhajan"
        ]):

            data["intent"] = "media"
            data["confidence"] = 95

        # ---------- Shutdown ----------

        elif any(x in text for x in [
            "shutdown",
            "restart",
            "format",
            "delete"
        ]):

            data["intent"] = "system"
            data["danger"] = True
            data["confirm"] = True
            data["priority"] = 10

        return data


thinking_v2 = ThinkingV2()