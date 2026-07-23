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

        print("🧠 Intent :", intent)

        # Planner
        plan = planner.create_plan(text)

        if plan:
            print("📋 Plan :", plan)

        # Decision
        info = decision.decide(text)

        if info.get("warning"):
            print("⚠", info["warning"])

        # Reasoning
        reasoning.think(text)

        # Router
        route = router.route(text)

        print("📌", route)
        # ---------------- Greeting ---------------- #

        if intent == "greeting":
            self.last_response = (
                "Hello Sir. Welcome back."
            )
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

            data = self.memory.search("my name")

            if data:
                self.last_response = f"Sir, {data[-1]}"
            else:
                self.last_response = (
                    "Sir, I don't know your name yet."
                )

            return self.last_response

        # ---------------- Remember ---------------- #

        if intent == "remember":

            text = entities.get("query")

            if not text:
                return "Sir, what should I remember?"

            self.memory.remember(text)

            self.last_response = (
                "Sir, I have remembered it."
            )

            return self.last_response

        # ---------------- Search ---------------- #

        if intent == "search":

            keyword = entities.get("query")

            result = self.memory.search(keyword)

            if result:

                self.last_response = "\n".join(result)

            else:

                self.last_response = (
                    "Sir, nothing found."
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

        # ---------------- Planner Response ---------------- #

        next_step = planner.next_step(plan)

        if next_step:

            self.last_response = next_step

            return next_step

        # ---------------- Unknown ---------------- #

        self.last_response = (
            "सर, मैं इसे अभी पूरी तरह नहीं समझ पाया। "
            "कृपया इसे दूसरे तरीके से कहें।"
        )

        return self.last_response


engine = Engine()