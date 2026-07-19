from voice.voice_engine import get_command
from core.brain import process_command
from voice.speak import speak

print("=" * 50)
print("🎤 ARIS Voice Mode")
print("=" * 50)

while True:

    command = get_command()

    if not command:
        continue

    result = process_command(command)

    if result == "exit":
        speak("Goodbye")
        print("Goodbye")
        break

    print(result)
    speak(result)