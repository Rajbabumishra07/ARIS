"""
ARIS V17.9 Stable Core Engine
Author : Raj Babu Mishra

P1.4
Information Command Routing
Context-aware Execution
"""

from datetime import datetime

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

    # =================================================
    # INFORMATION COMMANDS
    # =================================================

    def _information_command(self, text):

        command = text.lower().strip()

        # ---------------- Time ----------------

        if command in (
            "time",
            "what is the time",
            "what is time",
            "current time",
            "tell me the time"
        ):

            return datetime.now().strftime("%I:%M %p")

        # ---------------- Date ----------------

        if command in (
            "date",
            "today date",
            "today's date",
            "what is the date",
            "what is today's date"
        ):

            return datetime.now().strftime("%d-%m-%Y")

        # ---------------- Month ----------------

        if command in (
            "month",
            "current month",
            "what month is this",
            "which month is this"
        ):

            return datetime.now().strftime("%B")

        # ---------------- Year ----------------

        if command in (
            "year",
            "current year",
            "what year is this",
            "which year is this"
        ):

            return datetime.now().strftime("%Y")

        # ---------------- Calendar ----------------

        if command in (
            "calendar",
            "calender",
            "show calendar",
            "show calender"
        ):

            return datetime.now().strftime("%B %Y")

        # ---------------- Weather ----------------

        if command in (
            "weather",
            "current weather",
            "what is the weather",
            "what's the weather"
        ):

            return "Weather module will be added soon."

        return None

    # =================================================
    # MAIN PROCESSOR
    # =================================================

    def process(self, command):

        command = command.strip()

        if not command:
            return None

        # =================================================
        # CONTEXT
        # =================================================

        context.remember(command)

        command = context.resolve(command)

        # =================================================
        # NLU
        # =================================================

        text = nlu.normalize(command)

        # =================================================
        # SPEECH RECOVERY
        # =================================================

        text = speech_recovery(text)

        # =================================================
        # COMMAND RECOVERY
        # =================================================

        text = command_recovery.recover(text)

        intent = nlu.intent(text)

        entities = nlu.entities(text)

        self.last_command = text
        self.last_intent = intent

        # =================================================
        # INFORMATION COMMANDS
        #
        # IMPORTANT:
        # These commands must be handled BEFORE
        # core.commands.execute().
        # =================================================

        information = self._information_command(text)

        if information is not None:

            self.last_response = information

            return information

        # =================================================
        # PLANNER
        # =================================================

        plan = planner.create_plan(text)

        # =================================================
        # DECISION
        # =================================================

        decision.decide(text)

        # =================================================
        # REASONING
        # =================================================

        reasoning.think(text)

        # =================================================
        # ROUTER
        # =================================================

        router.route(text)

        # =================================================
        # GREETING
        # =================================================

        if intent == "greeting":

            self.last_response = (
                "Hello Sir. Welcome back."
            )

            return self.last_response

        # =================================================
        # ASK ARIS NAME
        # =================================================

        if intent == "ask_name":

            self.last_response = (
                f"{aris.greeting}\n"
                f"My name is {aris.name}."
            )

            return self.last_response

        # =================================================
        # ASK USER NAME
        # =================================================

        if intent == "ask_my_name":

            profile = self.memory.get_profile()

            name = profile.get(
                "name",
                ""
            ).strip()

            if name:

                self.last_response = (
                    f"Sir, your name is {name}."
                )

            else:

                self.last_response = (
                    "Sir, I don't know your name yet."
                )

            return self.last_response

        # =================================================
        # FAVORITE COLOR
        # =================================================

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

        # =================================================
        # REMEMBER
        # =================================================

        if intent == "remember":

            query = entities.get(
                "query",
                ""
            ).strip()

            if not query:

                return "Sir, what should I remember?"

            self.memory.remember(query)

            self.last_response = (
                "Sir, I have remembered it."
            )

            return self.last_response

        # =================================================
        # SEARCH
        # =================================================

        if intent == "search":

            keyword = entities.get(
                "query",
                ""
            ).strip()

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

        # =================================================
        # WINDOW / APP COMMANDS
        # =================================================

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

        # =================================================
        # EXIT
        # =================================================

        if intent == "exit":

            return "exit"

        # =================================================
        # GENERAL CORE EXECUTION
        # =================================================

        response = execute(text)

        if response:

            self.last_response = response

            return response

        # =================================================
        # PLANNER FALLBACK
        # =================================================

        if plan:

            step = planner.next_step(plan)

            if step:

                self.last_response = step

                return step

        # =================================================
        # CONTEXT REPLY
        # =================================================

        try:

            previous = context.last_response()

            if previous:

                self.last_response = previous

                return previous

        except Exception:

            pass

        # =================================================
        # UNKNOWN
        # =================================================

        self.last_response = (
            "Sir, I didn't understand that.\n"
            "Could you please say it differently?"
        )

        return self.last_response


engine = Engine()