"""
ARIS V13 - FollowUp Engine
"""

from brain.context import context
from brain.nlu import nlu


class FollowUp:

    def resolve(self, command):

        text = nlu.normalize(command)

        last = context.get_last()

        if not last:
            return None

        # Repeat previous command
        if text in [
            "again",
            "repeat",
            "dobara",
            "fir",
            "phir"
        ]:
            return last

        # Follow-up search
        if text.startswith("search "):

            query = text.replace("search", "", 1).strip()

            if query:
                return f"search {query}"

        return None


followup = FollowUp()