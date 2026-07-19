import datetime

from memory.memory import save_memory, read_memory
from memory.memory_core import memory

from core.smart_commands import smart_command
from core.commands import execute

from brain.logger import log
from brain.router_v2 import router

from brain.context import context
from brain.action_memory import action_memory

from brain.aliases import normalize
 

def process_command(command):

    command = normalize(command)

    log(command)

    if not command:
        return "Please say a command."

    # ---------------- AI Brain ---------------- #

    ai = router.process(command)

    # ---------------- Smart Commands ---------------- #
    
    result = smart_command(command)
    

    if result:

        memory.add_conversation(command, result)

        return result

    # ---------------- Execute ---------------- #

    if ai["execute"]:

        result = execute(command)

        if result:

            memory.add_conversation(command, result)

            return result

    # ---------------- Greetings ---------------- #

    if command in [

        "hello",
        "hi",
        "hey"

    ]:

        reply = "Good to see you, Akshat Sir."

        memory.add_conversation(command, reply)

        return reply

    # ---------------- Time ---------------- #

    elif command in [

        "time",
        "what is the time"

    ]:

        now = datetime.datetime.now()

        reply = "Current Time: " + now.strftime("%I:%M %p")

        memory.add_conversation(command, reply)

        return reply