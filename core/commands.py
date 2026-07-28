"""
ARIS V16 Core Command Executor
Author : Raj Babu Mishra
"""

from system.apps import open_app
from system.browser import browser_command
from system.files import open_folder
from system.file_manager import file_manager
from system.folder_operations import folder_operations
from system.screenshot import take_screenshot
from core.file_commands import execute_file

from system.app_manager import open_application
from system.website_manager import open_website
from system.system_manager import execute_system
from system.media_manager import play_media
from system.app_launcher import launch
from system.window_manager import window

from brain.action_memory import action_memory


def execute(command):

    print("🔧 Executing command:", command)

    command = command.lower().strip()

    # ---------------- Action Memory ---------------- #

    if (
        command.startswith("open ")
        or command.startswith("launch ")
        or command.startswith("start ")
        or command.startswith("run ")
    ):

        target = command.split(" ", 1)[1].strip()

        action_memory.remember("open", target)

    elif command.startswith("play "):

        target = command.split(" ", 1)[1].strip()

        action_memory.remember("play", target)

        # ---------------- Window Manager ---------------- #

    if command.startswith("minimize "):

        app = command.replace("minimize ", "").strip()

        if window.minimize(app):

            return f"Minimized {app.title()}."

        return f"I couldn't find {app.title()}."


    if command.startswith("maximize "):

        app = command.replace("maximize ", "").strip()

        if window.maximize(app):

            return f"Maximized {app.title()}."

        return f"I couldn't find {app.title()}."


    if command.startswith("restore "):

        app = command.replace("restore ", "").strip()

        if window.restore(app):

            return f"Restored {app.title()}."

        return f"I couldn't find {app.title()}."


    if command.startswith("switch to "):

        app = command.replace("switch to ", "").strip()

        if window.activate(app):

            return f"Switched to {app.title()}."

        return f"I couldn't find {app.title()}."

     # ---------------- Folder Operations ---------------- #

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

    # ---------------- File Commands ---------------- #

    result = execute_file(command)

    if result is not None:
        return result

    # ---------------- Smart Launcher ---------------- #

    if (
        command.startswith("open ")
        or command.startswith("launch ")
        or command.startswith("start ")
        or command.startswith("run ")
    ):

        app = command.split(" ", 1)[1].strip()

        print("🚀 Launching:", app)

        result = launch(app)

        if result is not None:
            return result

    # ---------------- App Manager ---------------- #

    result = open_application(command)

    if result is not None:
        return result

    # ---------------- Website ---------------- #

    result = open_website(command)

    if result is not None:
        return result
        # ---------------- Media ---------------- #

    result = play_media(command)

    if result is not None:
        return result

    # ---------------- System ---------------- #

    result = execute_system(command)

    if result is not None:
        return result

    # ---------------- Legacy Apps ---------------- #

    result = open_app(command)

    if result is not None:
        return result

    # ---------------- File Manager ---------------- #

    if (
       command.startswith("open ")
       or command.startswith("launch ")
       or command.startswith("start ")
       or command.startswith("run ")
    ):

      folder = command.split(" ", 1)[1].strip()

      response = file_manager.open(folder)

    # ---------------- Browser ---------------- #

    result = browser_command(command)

    if result is not None:
        return result

    # ---------------- Files ---------------- #

    result = open_folder(command)

    if result is not None:
        return result

    # ---------------- Screenshot ---------------- #

    result = take_screenshot(command)

    if result is not None:
        return result

    # ---------------- Nothing Matched ---------------- #

    return None