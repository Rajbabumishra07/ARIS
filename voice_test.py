from voice.voice_engine import get_command
from core.brain import process_command
from voice.speak import speak
import time

print("=" * 50)
print("🎤 ARIS Voice Mode")
print("=" * 50)

while True:

    command = get_command()

    if not command:
        continue

    print("You:", command)

    result = process_command(command)

    if result == "exit":
        speak("Goodbye Raj.")
        print("Goodbye Raj.")
        break

    if result:
        print("ARIS:", result)

        # Microphone ko thodi der rok do
        time.sleep(0.5)

        speak(result)

        # ARIS apni hi voice dobara na sune
        time.sleep(2.5)