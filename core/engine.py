"""
ARIS V18 AI BRAIN CORE ENGINE
Author : Raj Babu Mishra

P2.1
Central AI Brain Integration

Purpose:
- Central AI Brain orchestration
- Existing ARIS intelligence preserved
- Information commands
- Weather
- Context
- NLU
- Existing Smart Command Engine
- Existing Core Command Engine
- Planner / Reasoning / Decision
- Safe fallback

IMPORTANT:
This file does NOT remove the existing ARIS command system.
The AI Brain sits above the existing capabilities.
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

from ai.weather import get_weather

# =========================================================
# CENTRAL AI BRAIN
# =========================================================

from brain.ai_brain import ai_brain


class Engine:

    def __init__(self):

        self.memory = memory

        self.last_command = ""
        self.last_intent = ""
        self.last_response = ""

    # =========================================================
    # INFORMATION COMMANDS
    # =========================================================

    def _information_command(self, text):

        command = str(text).lower().strip()

        if not command:
            return None

        # =====================================================
        # TIME
        # =====================================================

        if command in (
            "time",
            "what is the time",
            "what is time",
            "current time",
            "tell me the time",
            "what time is it"
        ):

            return datetime.now().strftime("%I:%M %p")

        # =====================================================
        # DATE
        # =====================================================

        if command in (
            "date",
            "today date",
            "today's date",
            "what is the date",
            "what is today's date",
            "what's the date",
            "whats the date"
        ):

            return datetime.now().strftime("%d-%m-%Y")

        # =====================================================
        # MONTH
        # =====================================================

        if command in (
            "month",
            "current month",
            "what month is this",
            "which month is this",
            "what is the current month"
        ):

            return datetime.now().strftime("%B")

        # =====================================================
        # YEAR
        # =====================================================

        if command in (
            "year",
            "current year",
            "what year is this",
            "which year is this",
            "what is the current year"
        ):

            return datetime.now().strftime("%Y")

        # =====================================================
        # CALENDAR
        # =====================================================

        if command in (
            "calendar",
            "calender",
            "show calendar",
            "show calender",
            "current calendar",
            "this month calendar"
        ):

            return datetime.now().strftime("%B %Y")

        # =====================================================
        # WEATHER
        # =====================================================

        default_weather_commands = (
            "weather",
            "current weather",
            "what is the weather",
            "what's the weather",
            "whats the weather",
            "tell me the weather",
            "tell me weather",
            "what is weather",
            "what's weather"
        )

        if command in default_weather_commands:

            return get_weather("Prayagraj")

        # =====================================================
        # WEATHER CITY
        # =====================================================

        weather_prefixes = (
            "weather ",
            "current weather ",
            "what is the weather in ",
            "what is weather in ",
            "what's the weather in ",
            "what's weather in ",
            "whats the weather in ",
            "tell me the weather in ",
            "what is the weather at ",
            "weather at ",
            "weather for "
        )

        for prefix in weather_prefixes:

            if command.startswith(prefix):

                city = command[len(prefix):].strip()

                if city:

                    return get_weather(city)

        return None

    # =========================================================
    # AI BRAIN
    # =========================================================

    def _ai_brain(self, text):
        """
        Central AI Brain entry point.

        The existing ARIS systems remain untouched.
        If the Brain understands the request, its response
        is returned.

        If it cannot handle the request, None is returned
        and the old Engine pipeline continues.
        """

        if not text:
            return None

        try:

            result = ai_brain.process(text)

            if result:

                return result

        except Exception as error:

            # Brain failure must NEVER crash ARIS.
            print(
                f"[AI BRAIN FALLBACK] {error}"
            )

        return None

    # =========================================================
    # MAIN PROCESSOR
    # =========================================================

    def process(self, command):

        if command is None:

            return None

        command = str(command).strip()

        if not command:

            return None

        # =====================================================
        # CONTEXT
        # =====================================================

        try:

            context.remember(command)

            command = context.resolve(command)

        except Exception:

            pass

        # =====================================================
        # NLU
        # =====================================================

        text = nlu.normalize(command)

        # =====================================================
        # SPEECH RECOVERY
        # =====================================================

        try:

            text = speech_recovery(text)

        except Exception:

            pass

        # =====================================================
        # COMMAND RECOVERY
        # =====================================================

        try:

            text = command_recovery.recover(text)

        except Exception:

            pass

        # =====================================================
        # NLU RESULT
        # =====================================================

        intent = nlu.intent(text)

        entities = nlu.entities(text)

        self.last_command = text
        self.last_intent = intent

        # =====================================================
        # INFORMATION COMMANDS
        #
        # Keep deterministic information commands first.
        # =====================================================

        information = self._information_command(text)

        if information is not None:

            self.last_response = information

            return information

        # =====================================================
        # CENTRAL AI BRAIN
        #
        # From this point ARIS gives the central Brain the
        # first opportunity to understand the request.
        #
        # Existing systems are NOT removed.
        # =====================================================

        brain_response = self._ai_brain(text)

        if brain_response:

            self.last_response = brain_response

            return brain_response

        # =====================================================
        # PLANNER
        # =====================================================

        try:

            plan = planner.create_plan(text)

        except Exception:

            plan = None

        # =====================================================
        # DECISION
        # =====================================================

        try:

            decision.decide(text)

        except Exception:

            pass

        # =====================================================
        # REASONING
        # =====================================================

        try:

            reasoning.think(text)

        except Exception:

            pass

        # =====================================================
        # ROUTER
        # =====================================================

        try:

            router.route(text)

        except Exception:

            pass

        # =====================================================
        # GREETING
        # =====================================================

        if intent == "greeting":

            self.last_response = (
                "Hello Sir. Welcome back."
            )

            return self.last_response

        # =====================================================
        # ASK ARIS NAME
        # =====================================================

        if intent == "ask_name":

            self.last_response = (
                f"{aris.greeting}\n"
                f"My name is {aris.name}."
            )

            return self.last_response

        # =====================================================
        # ASK USER NAME
        # =====================================================

        if intent == "ask_my_name":

            try:

                profile = self.memory.get_profile()

                name = profile.get(
                    "name",
                    ""
                ).strip()

            except Exception:

                name = ""

            if name:

                self.last_response = (
                    f"Sir, your name is {name}."
                )

            else:

                self.last_response = (
                    "Sir, I don't know your name yet."
                )

            return self.last_response

        # =====================================================
        # ASK CREATOR
        # =====================================================

        if intent == "ask_creator":

            self.last_response = (
                "I was created by Raj Babu Mishra."
            )

            return self.last_response

        # =====================================================
        # FAVORITE COLOR
        # =====================================================

        if intent == "ask_favorite_color":

            try:

                preferences = (
                    self.memory.get_preferences()
                )

                color = preferences.get(
                    "favorite_color",
                    ""
                ).strip()

            except Exception:

                color = ""

            if color:

                self.last_response = (
                    f"Sir, your favorite color is {color}."
                )

            else:

                self.last_response = (
                    "Sir, I don't know your "
                    "favorite color yet."
                )

            return self.last_response

        # =====================================================
        # REMEMBER
        # =====================================================

        if intent == "remember":

            query = entities.get(
                "query",
                ""
            ).strip()

            if not query:

                self.last_response = (
                    "Sir, what should I remember?"
                )

                return self.last_response

            try:

                self.memory.remember(query)

            except Exception:

                pass

            self.last_response = (
                "Sir, I have remembered it."
            )

            return self.last_response

        # =====================================================
        # SEARCH
        # =====================================================

        if intent == "search":

            keyword = entities.get(
                "query",
                ""
            ).strip()

            if not keyword:

                self.last_response = (
                    "Sir, what should I search?"
                )

                return self.last_response

            try:

                result = self.memory.search(
                    keyword
                )

            except Exception:

                result = None

            if result:

                self.last_response = (
                    "\n".join(result)
                )

                return self.last_response

        # =====================================================
        # WINDOW / APP COMMANDS
        #
        # Existing command system remains active.
        # =====================================================

        if intent in (
            "open",
            "close",
            "minimize",
            "maximize",
            "restore",
            "switch"
        ):

            try:

                response = execute(text)

            except Exception:

                response = None

            if response:

                self.last_response = response

                return response

        # =====================================================
        # EXIT
        # =====================================================

        if intent == "exit":

            return "exit"

        # =====================================================
        # GENERAL CORE EXECUTION
        # =====================================================

        try:

            response = execute(text)

        except Exception:

            response = None

        if response:

            self.last_response = response

            return response

        # =====================================================
        # PLANNER FALLBACK
        # =====================================================

        if plan:

            try:

                step = planner.next_step(plan)

            except Exception:

                step = None

            if step:

                self.last_response = step

                return step

        # =====================================================
        # CONTEXT REPLY
        # =====================================================

        try:

            previous = context.last_response()

            if previous:

                self.last_response = previous

                return previous

        except Exception:

            pass

        # =====================================================
        # FINAL UNKNOWN
        # =====================================================

        self.last_response = (
            "Sir, I didn't understand that.\n"
            "Could you please say it differently?"
        )

        return self.last_response


# =========================================================
# SINGLETON
# =========================================================

engine = Engine()