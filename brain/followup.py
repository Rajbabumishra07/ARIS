from brain.context import context
from brain.nlp import nlp


class FollowUp:

    def resolve(self, command):

        text = nlp.normalize(command)

        # YouTube
        if "youtube" in text and context.app() == "chrome":
            return "open youtube"

        # Google
        if "google" in text and context.app() == "chrome":
            return "open google"

        # Repeat Song
        if ("again" in text or "dobara" in text) and context.song():
            return f"play {context.song()}"

        # Search in current app
        if "search" in text and context.app():

            query = text.replace("search", "").strip()

            if query:
                return f"search {query}"

        return None


followup = FollowUp()
