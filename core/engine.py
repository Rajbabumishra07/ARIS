"""
ARIS V18.0 Stable Core Engine
Author : Raj Babu Mishra
"""

from brain.nlu import nlu
from brain.context import context
from brain.router import router
from brain.reasoning import reasoning
from brain.decision import decision
from brain.planner import planner
from brain.command_recovery import command_recovery
from brain.speech_recovery import speech_recovery

from core.memory import memory
from core.commands import execute
from core.identity import aris


class Engine:

    def __init__(self):

        self.memory = memory

        self.last_command = ""
        self.last_intent = ""
        self.last_response = ""

        # V18 Pipeline State

        self.last_plan = None
        self.last_reasoning = None
        self.last_decision = None
        self.last_route = None

    # ------------------------------------------------ #

    def process(self, command):

        command = command.strip()

        if not command:
            return None

        # ---------------- Context ---------------- #

        context.remember(command)

        command = context.resolve(command)

        # ---------------- NLU ---------------- #

        text = nlu.normalize(command)

        # ---------------- Speech Recovery ---------------- #

        text = speech_recovery(text)

        # ---------------- Command Recovery ---------------- #

        text = command_recovery.recover(text)

        intent = nlu.intent(text)

        entities = nlu.entities(text)

        self.last_command = text
        self.last_intent = intent

        # ---------------- Planner ---------------- #

        plan = planner.create_plan(text)
        self.last_plan = plan

        # ---------------- Decision ---------------- #

        decision_result = decision.decide(text)
        self.last_decision = decision_result

        # ---------------- Reasoning ---------------- #

        reasoning_result = reasoning.think(text)
        self.last_reasoning = reasoning_result

        # ---------------- Router ---------------- #

        route_result = router.route(text)
        self.last_route = route_result

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

        # ---------------- Creator ---------------- #

        if intent == "ask_creator":

            self.last_response = aris.creator_info()

            return self.last_response

        # ---------------- Owner ---------------- #

        if intent == "ask_owner":

            self.last_response = aris.owner_info()

            return self.last_response

        # ---------------- Version ---------------- #

        if intent == "ask_version":

            self.last_response = aris.version_info()

            return self.last_response

        # ---------------- Identity ---------------- #

        if intent == "ask_identity":

            self.last_response = aris.introduce()

            return self.last_response

        # ---------------- Purpose ---------------- #

        if intent == "ask_purpose":

            self.last_response = aris.purpose_info()

            return self.last_response

        # ---------------- Full Form ---------------- #

        if intent == "ask_full_form":

            self.last_response = aris.full_form_info()

            return self.last_response

        # ---------------- Ask User Name ---------------- #

        if intent == "ask_my_name":

            profile = self.memory.get_profile()

            name = profile.get("name", "").strip()

            if name:

                self.last_response = (
                    f"Sir, your name is {name}."
                )

            else:

                self.last_response = (
                    "Sir, I don't know your name yet."
                )

            return self.last_response

        # ---------------- Favorite Color ---------------- #

        if intent == "ask_favorite_color":

            pref = self.memory.get_preferences()

            color = pref.get(
                "favorite_color",
                ""
            ).strip()

            if color:

                self.last_response = (
                    f"Sir, your favorite color is {color}."
                )

            else:

                self.last_response = (
                    "Sir, I don't know your favorite color yet."
                )

            return self.last_response

        # ---------------- Remember ---------------- #

        if intent == "remember":

            query = entities.get("query", "").strip()

            if not query:

                return "Sir, what should I remember?"

            self.memory.remember(query)

            self.last_response = (
                "Sir, I have remembered it."
            )

            return self.last_response

        # ---------------- Search ---------------- #

        if intent == "search":

            keyword = entities.get("query", "").strip()

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

        # ---------------- Window & App Commands ---------------- #

        if intent in (
            "open",
            "close",
            "minimize",
            "maximize",
            "restore",
            "switch"
        ):

            response = execute(text)

            if response:

                self.last_response = response

                return response

        # ---------------- Exit ---------------- #

        if intent == "exit":

            return "exit"

        # ---------------- Execute ---------------- #

        response = execute(text)

        if response:

            self.last_response = response

            return response

            # ---------------- Planner ---------------- #

        planner_intents = {
            "plan",
            "planning",
            "goal"
        }

        if intent in planner_intents:

            step = planner.next_step(self.last_plan)

            if step:

                self.last_response = step

                return step

        # ---------------- Context Reply ---------------- #

        try:

            previous = context.last_response()

            if previous:

                self.last_response = previous

                return previous

        except Exception:

            pass

        # ---------------- Unknown ---------------- #

        self.last_response = (
            "Sir, I didn't understand that.\n"
            "Could you please say it differently?"
        )

        return self.last_response


engine = Engine()