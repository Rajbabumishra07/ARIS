"""
ARIS V13 - Brain Entry
"""

from core.engine import engine


def process_command(command):
    return engine.process(command)