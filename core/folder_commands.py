"""
ARIS V17.7 Folder Command Router
Author : Raj Babu Mishra
"""

from system.folder_operations import folder_operations


def execute_folder(command):

    command = command.lower().strip()

    # ---------------- Create ---------------- #

    if command.startswith("create folder "):

        name = command.replace("create folder ", "").strip()

        if not name:
            return "Please tell me the folder name."

        return folder_operations.create(name)

    if command.startswith("make folder "):

        name = command.replace("make folder ", "").strip()

        if not name:
            return "Please tell me the folder name."

        return folder_operations.create(name)

    # ---------------- Rename ---------------- #

    if command.startswith("rename folder "):

        text = command.replace("rename folder ", "").strip()

        if " to " not in text:
            return "Please tell me the new folder name."

        old_name, new_name = text.split(" to ", 1)

        return folder_operations.rename(
            old_name.strip(),
            new_name.strip()
        )

    # ---------------- Delete ---------------- #

    if command.startswith("delete folder "):

        name = command.replace("delete folder ", "").strip()

        return folder_operations.delete(name)

"""
ARIS V17.7 Folder Command Router
Author : Raj Babu Mishra
"""

from system.folder_operations import folder_operations


def execute_folder(command):

    command = command.lower().strip()

    # ---------------- Create ---------------- #

    if command.startswith("create folder "):

        name = command.replace("create folder ", "").strip()

        if not name:
            return "Please tell me the folder name."

        return folder_operations.create(name)

    if command.startswith("make folder "):

        name = command.replace("make folder ", "").strip()

        if not name:
            return "Please tell me the folder name."

        return folder_operations.create(name)

    # ---------------- Rename ---------------- #

    if command.startswith("rename folder "):

        text = command.replace("rename folder ", "").strip()

        if " to " not in text:
            return "Please tell me the new folder name."

        old_name, new_name = text.split(" to ", 1)

        return folder_operations.rename(
            old_name.strip(),
            new_name.strip()
        )

    # ---------------- Delete ---------------- #

    if command.startswith("delete folder "):

        name = command.replace("delete folder ", "").strip()

        return folder_operations.delete(name)

    # ---------------- Open ---------------- #

    if command.startswith("open folder "):

        name = command.replace("open folder ", "").strip()

        return folder_operations.open(name)

    # ---------------- Move ---------------- #

    if command.startswith("move folder "):

        text = command.replace("move folder ", "").strip()

        if " to " not in text:
            return "Please tell me the destination."

        name, destination = text.split(" to ", 1)

        return folder_operations.move(
            name.strip(),
            destination.strip()
        )

    # ---------------- Copy ---------------- #

    if command.startswith("copy folder "):

        text = command.replace("copy folder ", "").strip()

        if " to " not in text:
            return "Please tell me the destination."

        name, destination = text.split(" to ", 1)

        return folder_operations.copy(
            name.strip(),
            destination.strip()
        )

    return None

    # ---------------- Move ---------------- #

    if command.startswith("move folder "):

        text = command.replace("move folder ", "").strip()

        if " to " not in text:
            return "Please tell me the destination."

        name, destination = text.split(" to ", 1)

        return folder_operations.move(
            name.strip(),
            destination.strip()
        )

    # ---------------- Copy ---------------- #

    if command.startswith("copy folder "):

        text = command.replace("copy folder ", "").strip()

        if " to " not in text:
            return "Please tell me the destination."

        name, destination = text.split(" to ", 1)

        return folder_operations.copy(
            name.strip(),
            destination.strip()
        )

    return None