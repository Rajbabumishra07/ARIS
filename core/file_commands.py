"""
ARIS V17.7 File Command Router
Author : Raj Babu Mishra
"""

from system.file_operations import file_operations


def execute_file(command):

    command = command.lower().strip()

    # ---------------- Create ---------------- #

    if command.startswith("create file "):

        name = command.replace("create file ", "").strip()

        return file_operations.create(name)

    if command.startswith("make file "):

        name = command.replace("make file ", "").strip()

        return file_operations.create(name)

    # ---------------- Rename ---------------- #

    if command.startswith("rename file "):

        text = command.replace("rename file ", "").strip()

        if " to " not in text:
            return "Please tell me the new file name."

        old_name, new_name = text.split(" to ", 1)

        return file_operations.rename(
            old_name.strip(),
            new_name.strip()
        )

    # ---------------- Delete ---------------- #

    if command.startswith("delete file "):

        name = command.replace("delete file ", "").strip()

        return file_operations.delete(name)

    # ---------------- Open ---------------- #

    if command.startswith("open file "):

        name = command.replace("open file ", "").strip()

        return file_operations.open(name)

    # ---------------- Move ---------------- #

    if command.startswith("move file "):

        text = command.replace("move file ", "").strip()

        if " to " not in text:
            return "Please tell me the destination."

        name, destination = text.split(" to ", 1)

        return file_operations.move(
            name.strip(),
            destination.strip()
        )

    # ---------------- Copy ---------------- #

    if command.startswith("copy file "):

        text = command.replace("copy file ", "").strip()

        if " to " not in text:
            return "Please tell me the destination."

        name, destination = text.split(" to ", 1)

        return file_operations.copy(
            name.strip(),
            destination.strip()
        )

    return None