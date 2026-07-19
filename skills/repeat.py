from brain.context import context


def repeat_last():

    if context.song():
        return f"play {context.song()}"

    if context.app():
        return f"open {context.app()}"

    if context.topic():
        return context.topic()

    return None