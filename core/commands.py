"""
ARIS V18 Core Command Executor
Author : Raj Babu Mishra

P0.2.2
Single Command Router
Lazy System Imports
"""

from brain.action_memory import action_memory

from core.file_commands import execute_file
from core.folder_commands import execute_folder


# =========================================================
# COMMAND EXECUTOR
# =========================================================

def execute(command):

    print("🔧 Executing command:", command)

    if not command:
        return None

    command = command.lower().strip()

    if not command:
        return None

    # =====================================================
    # ACTION MEMORY
    # =====================================================

    if (
        command.startswith("open ")
        or command.startswith("launch ")
        or command.startswith("start ")
        or command.startswith("run ")
    ):

        target = command.split(" ", 1)[1].strip()

        if target:
            action_memory.remember(
                "open",
                target
            )

    elif command.startswith("play "):

        target = command.split(" ", 1)[1].strip()

        if target:
            action_memory.remember(
                "play",
                target
            )

    # =====================================================
    # WINDOW MANAGER
    # =====================================================

    if command.startswith("minimize "):

        from system.window_manager import window

        app = command.replace(
            "minimize ",
            "",
            1
        ).strip()

        if not app:
            return "Please tell me which window to minimize."

        if window.minimize(app):
            return f"Minimized {app.title()}."

        return f"I couldn't find {app.title()}."

    # -----------------------------------------------------

    if command.startswith("maximize "):

        from system.window_manager import window

        app = command.replace(
            "maximize ",
            "",
            1
        ).strip()

        if not app:
            return "Please tell me which window to maximize."

        if window.maximize(app):
            return f"Maximized {app.title()}."

        return f"I couldn't find {app.title()}."

    # -----------------------------------------------------

    if command.startswith("restore "):

        from system.window_manager import window

        app = command.replace(
            "restore ",
            "",
            1
        ).strip()

        if not app:
            return "Please tell me which window to restore."

        if window.restore(app):
            return f"Restored {app.title()}."

        return f"I couldn't find {app.title()}."

    # -----------------------------------------------------

    if command.startswith("switch to "):

        from system.window_manager import window

        app = command.replace(
            "switch to ",
            "",
            1
        ).strip()

        if not app:
            return "Please tell me which window to switch to."

        if window.activate(app):
            return f"Switched to {app.title()}."

        return f"I couldn't find {app.title()}."

    # =====================================================
    # FILE ROUTER
    # =====================================================

    result = execute_file(command)

    if result is not None:
        return result

    # =====================================================
    # FOLDER ROUTER
    # =====================================================

    result = execute_folder(command)

    if result is not None:
        return result

    # =====================================================
    # SMART APP LAUNCHER
    # =====================================================

    if (
        command.startswith("open ")
        or command.startswith("launch ")
        or command.startswith("start ")
        or command.startswith("run ")
    ):

        from system.app_launcher import launch

        app = command.split(
            " ",
            1
        )[1].strip()

        if app:

            print("🚀 Launching:", app)

            result = launch(app)

            if result is not None:
                return result

    # =====================================================
    # APP MANAGER
    # =====================================================

    from system.app_manager import open_application

    result = open_application(command)

    if result is not None:
        return result

    # =====================================================
    # WEBSITE MANAGER
    # =====================================================

    from system.website_manager import open_website

    result = open_website(command)

    if result is not None:
        return result

    # =====================================================
    # MEDIA MANAGER
    # =====================================================

    from system.media_manager import play_media

    result = play_media(command)

    if result is not None:
        return result

    # =====================================================
    # SYSTEM MANAGER
    # =====================================================

    from system.system_manager import execute_system

    result = execute_system(command)

    if result is not None:
        return result

    # =====================================================
    # LEGACY APP ROUTER
    # =====================================================

    from system.apps import open_app

    result = open_app(command)

    if result is not None:
        return result

    # =====================================================
    # FILE MANAGER
    # =====================================================

    if (
        command.startswith("open ")
        or command.startswith("launch ")
        or command.startswith("start ")
        or command.startswith("run ")
    ):

        from system.file_manager import file_manager

        folder = command.split(
            " ",
            1
        )[1].strip()

        if folder:

            response = file_manager.open(folder)

            if response is not None:
                return response

    # =====================================================
    # BROWSER
    # =====================================================

    from system.browser import browser_command

    result = browser_command(command)

    if result is not None:
        return result

    # =====================================================
    # LEGACY FILE/FOLDER OPEN
    # =====================================================

    from system.files import open_folder

    result = open_folder(command)

    if result is not None:
        return result

    # =====================================================
    # SCREENSHOT
    # =====================================================

    from system.screenshot import take_screenshot

    result = take_screenshot(command)

    if result is not None:
        return result

    # =====================================================
    # NOTHING MATCHED
    # =====================================================

    return None