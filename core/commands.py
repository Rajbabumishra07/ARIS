"""
ARIS V17.9 Core Command Executor
Author : Raj Babu Mishra

P1.3 Step 2
Core Router Deduplication
Context-aware Routing
Lazy System Imports
"""

from brain.action_memory import action_memory

from core.file_commands import execute_file
from core.folder_commands import execute_folder


# =========================================================
# COMMAND PREFIXES
# =========================================================

OPEN_COMMANDS = (
    "open ",
    "launch ",
    "start ",
    "run ",
)


def _is_open_command(command):
    return command.startswith(OPEN_COMMANDS)


def _get_target(command):
    return command.split(" ", 1)[1].strip()


# =========================================================
# COMMAND EXECUTOR
# =========================================================

def execute(command):

    print("🔧 Executing command:", command)

    if not command:
        return None

    command = str(command).lower().strip()

    if not command:
        return None

    # =====================================================
    # ACTION MEMORY
    # =====================================================

    if _is_open_command(command):

        target = _get_target(command)

        if target:

            action_memory.remember(
                "open",
                target
            )

    elif command.startswith("play "):

        target = _get_target(command)

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
    # CONTEXT-AWARE FILE OPEN
    # =====================================================

    if command.startswith("open "):

        target = command[5:].strip()

        if target:

            file_extensions = (
                ".txt",
                ".py",
                ".pdf",
                ".doc",
                ".docx",
                ".xls",
                ".xlsx",
                ".ppt",
                ".pptx",
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".bmp",
                ".webp",
                ".mp3",
                ".wav",
                ".mp4",
                ".mkv",
                ".csv",
                ".json",
                ".xml",
                ".html",
                ".css",
                ".js",
                ".zip",
            )

            if target.lower().endswith(file_extensions):

                result = execute_file(
                    f"open file {target}"
                )

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

    if _is_open_command(command):

        from system.app_launcher import launch

        app = _get_target(command)

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
    # LEGACY APPS
    # =====================================================

    from system.apps import open_app

    result = open_app(command)

    if result is not None:
        return result

    # =====================================================
    # FILE MANAGER
    # =====================================================

    if _is_open_command(command):

        from system.file_manager import file_manager

        target = _get_target(command)

        if target:

            response = file_manager.open(target)

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