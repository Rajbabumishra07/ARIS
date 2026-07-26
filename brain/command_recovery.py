"""
ARIS V17 Smart Command Recovery
Author : Raj Babu Mishra
"""

from difflib import get_close_matches

from brain.entities import entities


class CommandRecovery:

    def recover(self, command):

        words = command.lower().strip().split()

        if len(words) < 2:
            return command

        action = words[0]
        target = " ".join(words[1:])

        # Exact match
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