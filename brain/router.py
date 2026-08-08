"""
ARIS V17.9 Brain Router
Compatibility / Classification Router

P1.3 Router Merge

Responsibilities:
    - Normalize command
    - Extract NLU information
    - Return routing information
    - Keep legacy route() imports compatible

IMPORTANT:
    This router does NOT execute commands.
    Actual command execution remains in core.commands.
"""

from brain.nlu import nlu


class Router:

    def route(self, command):

        if not command:
            return {
                "intent": None,
                "subject": "",
                "command": "",
                "entities": {}
            }

        # =================================================
        # NORMALIZE
        # =================================================

        text = str(command).strip()

        if not text:
            return {
                "intent": None,
                "subject": "",
                "command": "",
                "entities": {}
            }

        text = nlu.normalize(text)

        # =================================================
        # NLU
        # =================================================

        try:

            data = nlu.entities(text)

        except Exception:

            data = {}

        if not isinstance(data, dict):
            data = {}

        # =================================================
        # INTENT
        # =================================================

        intent = data.get("intent")

        # =================================================
        # SUBJECT
        # =================================================

        subject = (
            data.get("query")
            or data.get("subject")
            or data.get("app")
            or ""
        )

        if not subject:
            subject = text

        # =================================================
        # UNIFIED RESULT
        # =================================================

        return {
            "intent": intent,
            "subject": subject,
            "command": text,
            "entities": data
        }


# =========================================================
# SINGLE ROUTER INSTANCE
# =========================================================

router = Router()


# =========================================================
# LEGACY COMPATIBILITY API
#
# Existing modules may still use:
#
#     from brain.router import route
#
# Keep this wrapper during P1.3 migration.
# =========================================================

def route(command):

    return router.route(command)