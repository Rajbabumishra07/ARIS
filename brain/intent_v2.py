from brain.aliases import normalize


class IntentEngine:

    def detect(self, command):

        command = normalize(command)

        # Browser
        if any(x in command for x in [
            "chrome",
            "browser",
            "google"
        ]):
            return "OPEN_BROWSER"

        # VS Code
        elif any(x in command for x in [
            "vscode",
            "vs code",
            "code"
        ]):
            return "OPEN_VSCODE"

        # Music
        elif any(x in command for x in [
            "play",
            "song",
            "music",
            "hanuman chalisa"
        ]):
            return "PLAY_MEDIA"

        # Time
        elif "time" in command:
            return "GET_TIME"

        # Date
        elif "date" in command:
            return "GET_DATE"

        # Greeting
        elif any(x in command for x in [
            "hello",
            "hi",
            "hey",
            "namaste"
        ]):
            return "GREETING"

        # Exit
        elif any(x in command for x in [
            "exit",
            "quit",
            "stop",
            "band"
        ]):
            return "EXIT"

        return "UNKNOWN"


intent_engine = IntentEngine()