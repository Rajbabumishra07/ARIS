class BrainThinking:

    def analyse(self, command):

        command = command.lower().strip()

        data = {
            "type": "general",
            "priority": 1,
            "confirm": False,
            "suggestion": None
        }

        # -------- Browser --------

        browser_words = [
            "chrome",
            "browser",
            "google",
            "internet",
            "web"
        ]

        # -------- Coding --------

        coding_words = [
            "code",
            "coding",
            "vscode",
            "visual studio",
            "python",
            "project"
        ]

        # -------- Music --------

        media_words = [
            "play",
            "song",
            "music",
            "bhajan",
            "hanuman chalisa",
            "youtube",
            "video",
            "gaana"
        ]

        # -------- Browser --------

        if any(word in command for word in browser_words):

            data["type"] = "browser"

        # -------- Coding --------

        elif any(word in command for word in coding_words):

            data["type"] = "coding"

        # -------- Media --------

        elif any(word in command for word in media_words):

            data["type"] = "media"

        # -------- Dangerous --------

        if any(word in command for word in [
            "delete",
            "format",
            "shutdown",
            "factory reset"
        ]):

            data["confirm"] = True
            data["priority"] = 5
            data["suggestion"] = (
                "Akshat Sir, ye command risky hai. Kya confirm karte hain?"
            )

        return data


brain = BrainThinking()