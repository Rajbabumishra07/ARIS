class ConversationContext:

    def __init__(self):

        self.last_command = ""
        self.last_topic = ""
        self.last_app = ""
        self.last_song = ""

    def update(self, command):

        self.last_command = command

        text = command.lower()

        if any(x in text for x in [
            "chrome",
            "browser",
            "google"
        ]):
            self.last_app = "chrome"

        elif any(x in text for x in [
            "vs code",
            "vscode",
            "code"
        ]):
            self.last_app = "vscode"

        elif any(x in text for x in [
            "hanuman chalisa",
            "song",
            "music",
            "bhajan"
        ]):
            self.last_topic = text
            self.last_song = text

    def app(self):
        return self.last_app

    def topic(self):
        return self.last_topic

    def song(self):
        return self.last_song


context = ConversationContext()