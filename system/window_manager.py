"""
ARIS V17.1 Window Manager
Author : Raj Babu Mishra
"""

import pygetwindow as gw


class WindowManager:

    def find(self, title):

        title = title.lower()

        windows = gw.getAllTitles()

        for win in windows:

            if not win.strip():
                continue

            if title in win.lower():

                return gw.getWindowsWithTitle(win)[0]

        return None

    # ---------------- Minimize ---------------- #

    def minimize(self, title):

        win = self.find(title)

        if not win:
            return False

        win.minimize()

        return True

    # ---------------- Maximize ---------------- #

    def maximize(self, title):

        win = self.find(title)

        if not win:
            return False

        win.maximize()

        return True

    # ---------------- Restore ---------------- #

    def restore(self, title):

        win = self.find(title)

        if not win:
            return False

        win.restore()

        return True

    # ---------------- Activate ---------------- #

    def activate(self, title):

        win = self.find(title)

        if not win:
            return False

        win.activate()

        return True


window = WindowManager()