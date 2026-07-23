"""
ARIS V14 - FollowUp Engine
Author : Raj Babu Mishra
"""

from brain.context import context
from brain.nlu import nlu


class FollowUp:

    def resolve(self, command):

        text = nlu.normalize(command)

        # ---------------- Repeat ---------------- #

        if text in (
            "again",
            "repeat",
            "dobara",
            "phir",
            "fir",
            "once more"
        ):

            return context.last_command

        # ---------------- Search ---------------- #

        if text.startswith("search "):

            query = text[7:].strip()

            if query:
                return f"search {query}"

        # ---------------- Pronouns ---------------- #

        if any(word in text.split() for word in (
            "it",
            "this",
            "that",
            "him",
            "her",
            "usko",
            "vo",
            "wah"
        )):

            return context.resolve(text)

        return None


followup = FollowUp()