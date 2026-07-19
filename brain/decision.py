from brain.thinking import brain


class DecisionEngine:

    def decide(self, command):

        data = brain.analyse(command)

        decision = {
            "execute": True,
            "confirm": False,
            "emotion": "neutral",
            "suggestion": None,
            "priority": data["priority"],
            "type": data["type"]
        }

        if data["confirm"]:
            decision["confirm"] = True
            decision["emotion"] = "warning"
            decision["suggestion"] = data["suggestion"]
            return decision

        if data["type"] == "browser":
            decision["emotion"] = "thinking"

        elif data["type"] == "coding":
            decision["emotion"] = "thinking"

        elif data["type"] == "media":
            decision["emotion"] = "neutral"

        return decision


decision_engine = DecisionEngine()