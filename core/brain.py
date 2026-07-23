"""
ARIS V14 - Brain Router
"""

from core.engine import engine


def process_command(command):
    """
    Router Only
    """

    if not command:
        return None

    return engine.process(command)