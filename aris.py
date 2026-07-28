"""
ARIS Launcher
Author : Raj Babu Mishra
"""

import time

BOOT = time.perf_counter()

from voice.listener import start_listening

print("=" * 50)
print("🤖 ARIS V17.8")
print("=" * 50)

print(f"⚡ Boot : {time.perf_counter()-BOOT:.2f} sec")

start_listening()