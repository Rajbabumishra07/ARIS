"""
ARIS V18 Smart Command Recovery
Author : Raj Babu Mishra
"""

from difflib import get_close_matches

from brain.entities import entities


class CommandRecovery:

    COMMAND_ALIASES = {
        "creat": "create",
        "crete": "create",
        "creat file": "create file",
        "creat folder": "create folder",

        "renam": "rename",
        "delate": "delete",
        "delet": "delete",

        "opn": "open",
        "oppen": "open",
    }

    PROTECTED_COMMANDS = {
        "create file",
        "make file",
        "delete file",
        "rename file",
        "copy file",
        "move file",
        "open file",

        "create folder",
        "make folder",
        "delete folder",
        "rename folder",
        "copy folder",
        "move folder",
        "open folder",
    }

    def _fix_command(self, command):

        command = command.lower().strip()

        # Exact multi-word corrections first
        for wrong, correct in sorted(
            self.COMMAND_ALIASES.items(),
            key=lambda x: len(x[0]),
            reverse=True
        ):

            if command.startswith(wrong + " "):

                command = (
                    correct
                    + command[len(wrong):]
                )

        return command

    def recover(self, command):

        command = self._fix_command(command)

        words = command.split()

        if len(words) < 2:
            return command

        # -------------------------------------------------
        # File/folder commands:
        # DO NOT fuzzy-match the target.
        # -------------------------------------------------

        command_prefix = " ".join(words[:2])

        if command_prefix in self.PROTECTED_COMMANDS:

            return command

        # -------------------------------------------------
        # Normal command recovery
        # -------------------------------------------------

        action = words[0]
        target = " ".join(words[1:])

        if entities.exists(target):

            return f"{action} {entities.normalize(target)}"

        apps = entities.get_all_apps()

        match = get_close_matches(
            target,
            apps,
            n=1,
            cutoff=0.55
        )

        if match:

            return f"{action} {match[0]}"

        return command


command_recovery = CommandRecovery()