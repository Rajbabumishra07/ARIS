import pyautogui

def take_screenshot(command):

    if command == "take screenshot":

        image = pyautogui.screenshot()

        image.save("Screenshot.png")

        return "Screenshot saved."

    return None