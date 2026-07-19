from core.brain import process_command
from core.identity import creator_info
from voice.speak import speak

print("=" * 50)
print("🤖 Welcome to ARIS AI Assistant")
print("=" * 50)

print(creator_info())

name = input("Enter your name: ").strip()

while True:

    command = input(f"\n{name}, Tell me your command: ").strip()

    if not command:
        continue

    result = process_command(command)

    if result == "exit":
        speak("Goodbye " + name)
        print("Goodbye", name)
        break

    if result:
        print(result)
        speak(result)