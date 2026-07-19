import os

def open_folder(command):

    command = command.lower()

    if command == "open downloads":
        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
        return "Opening Downloads."

    elif command == "open documents":
        os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
        return "Opening Documents."

    elif command == "open desktop":
        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))
        return "Opening Desktop."

    elif command == "open pictures":
        os.startfile(os.path.join(os.path.expanduser("~"), "Pictures"))
        return "Opening Pictures."

    return None