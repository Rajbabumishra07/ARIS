"""
ARIS V14 Core Engine
Author : Raj Babu Mishra
"""

from brain.nlu import nlu
from brain.router import router
from brain.context import context
from brain.reasoning import reasoning
from brain.decision import decision
from brain.planner import planner

from core.memory import Memory
from core.commands import execute
from core.identity import aris

DEBUG = False


class Engine:

    def __init__(self):

        self.memory = Memory()

        self.last_command = ""

        self.last_intent = ""

        self.last_response = ""

    def log(self, *args):

        if DEBUG:
            print(*args)

    # ---------------- Main ---------------- #

    def process(self, command):

        command = command.strip()

        if not command:
            return None

        # Context

        context.remember(command)

        command = context.resolve(command)

        # NLU

        text = nlu.normalize(command)

        intent = nlu.intent(text)

        entities = nlu.entities(text)

        self.last_command = text

        self.last_intent = intent

        self.log("🧠 Intent :", intent)

        # Planner

        plan = planner.create_plan(text)

        self.log("📋 Plan :", plan)

        # Decision

        info = decision.decide(text)

        if info.get("warning"):
            self.log("⚠", info["warning"])

        # Reasoning

        reasoning.think(text)

        # Router

        route = router.route(text)

        self.log("📌", route)
        # ---------------- Greeting ---------------- #

        if intent == "greeting":

            self.last_response = "Hello Sir. Welcome back."

            return self.last_response

        # ---------------- Ask ARIS Name ---------------- #

        if intent == "ask_name":

            self.last_response = (
                f"{aris.greeting}\n"
                f"My name is {aris.name}."
            )

            return self.last_response

        # ---------------- Ask User Name ---------------- #

        if intent == "ask_my_name":

            result = self.memory.search("my name")

            if result:

                self.last_response = result[-1]

            else:

                self.last_response = "Sir, I don't know your name yet."

            return self.last_response

        # ---------------- Remember ---------------- #

        if intent == "remember":

            value = entities.get("query")

            if not value:

                return "Sir, what should I remember?"

            self.memory.remember(value)

            self.last_response = "Sir, I have remembered it."

            return self.last_response

        # ---------------- Search ---------------- #

        if intent == "search":

            keyword = entities.get("query")

            if not keyword:

                return "Sir, what should I search?"

            result = self.memory.search(keyword)

            if result:

                self.last_response = "\n".join(result)

            else:

                self.last_response = "Sir, nothing found."

            return self.last_response
            # ---------------- Exit ---------------- #

        if intent == "exit":

            return "exit"

        # ---------------- Execute ---------------- #

        response = execute(text)

        if response:

            self.last_response = response

            return response

        # ---------------- Again ---------------- #

        if intent == "again":

            if self.last_response:

                return self.last_response

            return "Sir, there is nothing to repeat."

        # ---------------- Unknown ---------------- #

        self.last_response = (
            "Sir, I didn't understand that.\n"
            "Could you please say it differently?"
        )

        return self.last_response


engine = Engine()