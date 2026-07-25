"""
ARIS V16 Core Command Executor
Author : Raj Babu Mishra
"""

from system.apps import open_app
from system.browser import browser_command
from system.files import open_folder
from system.screenshot import take_screenshot

from system.app_manager import open_application
from system.website_manager import open_website
from system.system_manager import execute_system
from system.media_manager import play_media
from system.app_launcher import launch

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