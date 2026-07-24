"""
ARIS V15 Core Engine
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


class Engine:

    def __init__(self):

        self.memory = Memory()

        self.last_command = ""
        self.last_intent = ""
        self.last_response = ""

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

        # Background Engines
        planner.create_plan(text)
        decision.decide(text)
        reasoning.think(text)
        router.route(text)

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

            result = self.memory.search("name")

            if result:

                self.last_response = (
                    f"Sir, your name is {result[0]}."
                )

            else:

                self.last_response = (
                    "Sir, I don't know your name yet."
                )

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

                self.last_response = (
                    "Sir, I couldn't find anything."
                )

            return self.last_response

        # ---------------- Exit ---------------- #

        if intent == "exit":

            return "exit"

        # ---------------- Execute ---------------- #

        response = execute(text)

        if response:

            self.last_response = response

            return response

        # ---------------- Unknown ---------------- #

        self.last_response = (
            "Sir, I didn't understand that.\n"
            "Could you please say it differently?"
        )

        return self.last_response


engine = Engine()