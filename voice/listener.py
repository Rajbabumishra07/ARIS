from voice.voice_engine import get_command
from voice.wake_word import is_wake_word
from voice.voice_commands import special_voice_command

from core.brain import process_command
from voice.speak import speak

from brain.nlp import nlp
from brain.followup import followup
from brain.multi_command import multi

sleep_mode = False


def start_listening():

    global sleep_mode

    print("🎤 ARIS Voice System Started")

    while True:

        command = get_command()

        if not command:
            continue

        command = nlp.normalize(command)

        print("👤 You:", command)

        # ---------------- Exit ---------------- #

        if command in [
            "exit",
            "quit",
            "stop",
            "close",
            "stop listening",
            "band ho jao",
            "so jao",
        ]:

            speak("Good night, Akshat Sir.")
            print("ARIS Offline")
            break

        # ---------------- Special Commands ---------------- #

        action = special_voice_command(command)

        if action == "sleep":

            sleep_mode = True

            speak("Sleep mode activated, Sir.")

            continue

        # ---------------- Sleep Mode ---------------- #

        if sleep_mode:

            if is_wake_word(command):

                sleep_mode = False

                speak("Yes, Akshat Sir.")

            continue

        # ---------------- Wake Word ---------------- #

        if is_wake_word(command):

            speak("Ji, Akshat Sir.")

            continue

        # ---------------- Follow Up ---------------- #

        resolved = followup.resolve(command)

        if resolved:

            command = resolved

            print("🤖 ARIS (FollowUp):", command)

        # ---------------- Multi Command ---------------- #

        commands = multi.split(command)

        for cmd in commands:

            cmd = cmd.strip()

            if not cmd:
                continue

            result = process_command(cmd)

            if result == "exit":

                speak("Goodbye")

                print("Voice Mode Closed")

                return

            if result:

                print("🤖 ARIS:", result)

                speak(result)