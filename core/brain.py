"""
ARIS V18 Brain Router
Author : Raj Babu Mishra
"""

import time

_engine = None


def _get_engine():

    global _engine

    if _engine is None:

        t = time.perf_counter()

        from core.engine import engine

        print(
            f"⚡ Engine Import : {time.perf_counter()-t:.2f}s"
        )

        _engine = engine

    return _engine


def process_command(command):

    if not command:
        return None

    return _get_engine().process(command)