import time

t = time.perf_counter()
from voice.voice_engine import get_command
print(f"voice_engine      : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from voice.wake_word import is_wake_word
print(f"wake_word         : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from voice.voice_commands import special_voice_command
print(f"voice_commands    : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from core.brain import process_command
print(f"core.brain        : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from voice.speak import speak
print(f"speak             : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from brain.nlu import nlu
print(f"nlu               : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from brain.followup import followup
print(f"followup          : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from brain.multi_command import multi
print(f"multi             : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from brain.context import context
print(f"context           : {time.perf_counter()-t:.2f}s")

t = time.perf_counter()
from brain.speech_cleaner import speech_cleaner
print(f"speech_cleaner    : {time.perf_counter()-t:.2f}s")


sleep_mode = False


def start_listening():

    global sleep_mode

    print("🎤 ARIS Voice System Started")

    while True:

        command = get_command()

        if not command:
            continue

        # -------- Speech Cleaning -------- #

        command = speech_cleaner.clean(command)

        command = nlu.normalize(command)

        if command in {
            "",
            "the",
            "a",
            "an",
            "uh",
            "um",
            "hmm",
            "huh",
            "okay"
        }:
            continue

        print("👤 You:", command)

        # -------- Exit -------- #

        if command in {
            "exit",
            "quit",
            "stop",
            "close",
            "goodbye",
            "stop listening",
            "band ho jao",
            "so jao"
        }:

            speak("Good night, Sir.")

            print("ARIS Offline")

            break

        # -------- Special Voice Commands -------- #

        action = special_voice_command(command)

        if action == "sleep":

            sleep_mode = True

            speak("Sleep mode activated, Sir.")

            continue

        # -------- Sleep Mode -------- #

        if sleep_mode:

            if is_wake_word(command):

                sleep_mode = False

                speak("Yes Sir.")

            continue

        # -------- Wake Word -------- #

        if is_wake_word(command):

            speak("Hello Sir.")

            continue

        # -------- Follow Up -------- #

        resolved = followup.resolve(command)

        if resolved:

            command = resolved

            print("🤖 ARIS (FollowUp):", command)

        # -------- Multi Commands -------- #

        commands = multi.split(command)

        for cmd in commands:

            cmd = cmd.strip()

            if not cmd:
                continue

            result = process_command(cmd)

            context.set_response(result)

            if result == "exit":

                speak("Goodbye Sir.")

                print("ARIS Offline")

                return

            if result:

                print("🤖 ARIS:", result)

                speak(result)