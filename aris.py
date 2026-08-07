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

print(f"⚡ Core Loaded : {time.perf_counter()-BOOT:.2f}s")

t = time.perf_counter()

start_listening()

print(f"⚡ Full Startup : {time.perf_counter()-t:.2f}s")