"""
ARIS V17.9 Context Engine
Author : Raj Babu Mishra

P1.2 Context Upgrade
"""

from collections import deque


class ContextEngine:

    def __init__(self):

        self.history = deque(maxlen=50)

        self.last_command = ""
        self.last_intent = ""
        self.last_subject = ""
        self.last_app = ""
        self.last_response = ""

    # =====================================================
    # REMEMBER
    # =====================================================

    def remember(
        self,
        command,
        intent="",
        subject="",
        app=""
    ):

        command = str(command).strip()

        if not command:
            return

        # -------------------------------------------------
        # Extract useful target from file/folder commands
        # -------------------------------------------------

        extracted_subject = self._extract_target(command)

        if extracted_subject:
            subject = extracted_subject

        entry = {
            "command": command,
            "intent": intent,
            "subject": subject,
            "app": app
        }

        self.history.append(entry)

        self.last_command = command

        if intent:
            self.last_intent = intent

        if subject:
            self.last_subject = subject

        if app:
            self.last_app = app

    # =====================================================
    # TARGET EXTRACTION
    # =====================================================

    def _extract_target(self, command):

        text = command.lower().strip()

        prefixes = (
            "open file ",
            "open folder ",
            "create file ",
            "create folder ",
            "make file ",
            "make folder ",
            "delete file ",
            "delete folder ",
            "rename file ",
            "rename folder ",
            "copy file ",
            "copy folder ",
            "move file ",
            "move folder "
        )

        for prefix in prefixes:

            if text.startswith(prefix):

                target = text[len(prefix):].strip()

                # For rename/copy/move:
                # keep the source object, not destination.

                if " to " in target:

                    target = target.split(
                        " to ",
                        1
                    )[0].strip()

                if target:

                    return target

        return ""

    # =====================================================
    # UPDATE
    # =====================================================

    def update(
        self,
        intent="",
        subject="",
        app=""
    ):

        if intent:
            self.last_intent = intent

        if subject:
            self.last_subject = subject

        if app:
            self.last_app = app

    # =====================================================
    # RESOLVE FOLLOW-UP
    # =====================================================

    def resolve(self, command):

        text = str(command).lower().strip()

        if not text:
            return ""

        # -------------------------------------------------
        # AGAIN / REPEAT
        # -------------------------------------------------

        if text in (
            "again",
            "repeat",
            "dobara",
            "phir",
            "fir",
            "once more",
            "do it again"
        ):

            return self.last_command

        # -------------------------------------------------
        # IT / THIS / THAT
        #
        # Only resolve when a real previous target exists.
        # -------------------------------------------------

        target_words = {
            "it",
            "this",
            "that",
            "isko",
            "usko",
            "isko",
            "vo",
            "woh",
            "wah"
        }

        words = text.split()

        if len(words) == 2 and words[1] in target_words:

            prefix = words[0]

            if self.last_subject:

                return (
                    f"{prefix} {self.last_subject}"
                )

        # -------------------------------------------------
        # Exact standalone reference
        # -------------------------------------------------

        if text in target_words:

            if self.last_subject:

                return self.last_subject

            return text

        # -------------------------------------------------
        # Normal command
        # -------------------------------------------------

        return text

    # =====================================================
    # RESPONSE
    # =====================================================

    def set_response(self, response):

        self.last_response = (
            str(response).strip()
            if response is not None
            else ""
        )

    def response(self):

        return self.last_response

    def last_response_text(self):

        return self.last_response

    def get_response(self):

        return self.last_response

    # =====================================================
    # HISTORY
    # =====================================================

    def previous(self):

        if len(self.history) < 2:
            return None

        return list(self.history)[-2]

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def recent(self, count=5):

        if count <= 0:
            return []

        return list(self.history)[-count:]

    # =====================================================
    # CURRENT CONTEXT
    # =====================================================

    def current(self):

        return {
            "command": self.last_command,
            "intent": self.last_intent,
            "subject": self.last_subject,
            "app": self.last_app,
            "response": self.last_response
        }

    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):

        self.history.clear()

        self.last_command = ""
        self.last_intent = ""
        self.last_subject = ""
        self.last_app = ""
        self.last_response = ""


context = ContextEngine()