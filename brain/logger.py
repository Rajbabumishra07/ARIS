from datetime import datetime

def log(command):
    with open("logs/commands.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {command}\n")