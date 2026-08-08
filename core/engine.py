"""
ARIS V17.9 Core Engine
Author : Raj Babu Mishra

P1.1 Context Upgrade
"""

from brain.nlu import nlu
from brain.context import context
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

    # =====================================================
    # PROCESS COMMAND
    # =====================================================

    def process(self, command):

        command = str(command).strip()

        if not command:
            return None

        # -------------------------------------------------
        # Resolve follow-up BEFORE remembering it
        # -------------------------------------------------

        resolved_command = context.resolve(command)

        if not resolved_command:
            return None

        # -------------------------------------------------
        # Normalize
        # -------------------------------------------------

        text = nlu.normalize(resolved_command)

        # -------------------------------------------------
        # Speech Recovery
        # -------------------------------------------------

        text = speech_recovery(text)

        # -------------------------------------------------
        # Command Recovery
        # -------------------------------------------------

        text = command_recovery.recover(text)

        if not text:
            return None

        # -------------------------------------------------
        # NLU
        # -------------------------------------------------

        intent = nlu.intent(text)
        entities = nlu.entities(text)

        # -------------------------------------------------
        # Context Update
        #
        # IMPORTANT:
        # Remember the resolved command, not "again".
        # -------------------------------------------------

        subject = (
            entities.get("query")
            or entities.get("subject")
            or ""
        )

        app = (
            entities.get("app")
            or ""
        )

        context.remember(
            text,
            intent=intent or "",
            subject=subject,
            app=app
        )

        context.update(
            intent=intent or "",
            subject=subject,
            app=app
        )

        self.last_command = text
        self.last_intent = intent or ""

        # -------------------------------------------------
        # Greeting
        # -------------------------------------------------

        if intent == "greeting":

            response = "Hello Sir. Welcome back."

            context.set_response(response)

            self.last_response = response

            return response

        # -------------------------------------------------
        # Ask ARIS Name
        # -------------------------------------------------

        if intent == "ask_name":

            response = (
                f"{aris.greeting}\n"
                f"My name is {aris.name}."
            )

            context.set_response(response)

            self.last_response = response

            return response

        # -------------------------------------------------
        # Ask User Name
        # -------------------------------------------------

        if intent == "ask_my_name":

            profile = memory.get_profile()

            name = profile.get(
                "name",
                ""
            ).strip()

            if name:

                response = (
                    f"Sir, your name is {name}."
                )

            else:

                response = (
                    "Sir, I don't know your name yet."
                )

            context.set_response(response)

            self.last_response = response

            return response

        # -------------------------------------------------
        # Favorite Color
        # -------------------------------------------------

        if intent == "ask_favorite_color":

            preferences = memory.get_preferences()

            color = preferences.get(
                "favorite_color",
                ""
            ).strip()

            if color:

                response = (
                    f"Sir, your favorite color is {color}."
                )

            else:

                response = (
                    "Sir, I don't know your favorite color yet."
                )

            context.set_response(response)

            self.last_response = response

            return response

        # -------------------------------------------------
        # Remember
        # -------------------------------------------------

        if intent == "remember":

            query = entities.get(
                "query",
                ""
            ).strip()

            if not query:

                response = (
                    "Sir, what should I remember?"
                )

                context.set_response(response)

                self.last_response = response

                return response

            memory.remember(query)

            response = (
                "Sir, I have remembered it."
            )

            context.set_response(response)

            self.last_response = response

            return response

        # -------------------------------------------------
        # Search Memory
        # -------------------------------------------------

        if intent == "search":

            keyword = entities.get(
                "query",
                ""
            ).strip()

            if not keyword:

                response = (
                    "Sir, what should I search?"
                )

                context.set_response(response)

                self.last_response = response

                return response

            result = memory.search(keyword)

            if result:

                response = "\n".join(result)

            else:

                response = (
                    "Sir, I couldn't find anything."
                )

            context.set_response(response)

            self.last_response = response

            return response

        # -------------------------------------------------
        # Exit
        # -------------------------------------------------

        if intent == "exit":

            context.set_response("exit")

            self.last_response = "exit"

            return "exit"

        # =================================================
        # SINGLE COMMAND ROUTER
        # =================================================

        response = execute(text)

        if response:

            context.set_response(response)

            self.last_response = response

            return response

        # -------------------------------------------------
        # Planner
        # -------------------------------------------------

        try:

            plan = planner.create_plan(text)

            if plan:

                step = planner.next_step(plan)

                if step:

                    context.set_response(step)

                    self.last_response = step

                    return step

        except Exception:

            pass

        # -------------------------------------------------
        # Decision
        # -------------------------------------------------

        try:

            decision_result = decision.decide(text)

            if decision_result:

                context.set_response(
                    decision_result
                )

                self.last_response = (
                    decision_result
                )

                return decision_result

        except Exception:

            pass

        # -------------------------------------------------
        # Reasoning
        # -------------------------------------------------

        try:

            reasoning_result = reasoning.think(text)

            if reasoning_result:

                context.set_response(
                    reasoning_result
                )

                self.last_response = (
                    reasoning_result
                )

                return reasoning_result

        except Exception:

            pass

        # -------------------------------------------------
        # Unknown
        # -------------------------------------------------

        response = (
            "Sir, I didn't understand that.\n"
            "Could you please say it differently?"
        )

        context.set_response(response)

        self.last_response = response

        return response


engine = Engine()