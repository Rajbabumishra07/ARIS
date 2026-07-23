"""
ARIS V13 Core Engine
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

memory = Memory()


class Engine:

    def process(self, command):

        command = command.strip()

        if not command:
            return None

        # Context
        context.remember(command)
        command = context.resolve(command)

        # NLU
        command = nlu.normalize(command)
        intent = nlu.intent(command)

        print("🧠 Intent:", intent)

        # Greeting
        if intent == "greeting":
            return aris.greeting

        # Remember
        if intent == "remember":

            text = command.replace("remember", "").strip()

            memory.remember(text)

            return "जी सर। मैंने इसे याद रख लिया है।"

        # Search
        if intent == "search":

            keyword = command.replace("search", "").strip()

            data = memory.search(keyword)

            if data:
                return "\n".join(data)

            return "सर, मुझे इससे संबंधित कुछ याद नहीं है।"

        # Name
        if intent == "ask_name":

            data = memory.search("my name")

            if data:
                return f"सर, {data[-1]}"

            return "सर, मुझे आपका नाम याद नहीं है।"

        # Decision
        result = decision.decide(command)

        if result["warning"]:
            print("⚠", result["warning"])

        # Reasoning
        reasoning.think(command)

        # Router
        route = router.route(command)

        print("📌", route)

        # Execute
        response = execute(command)

        if response:
            return response

        return "सर, मैं अभी सीख रहा हूँ। कृपया इसे दूसरे तरीके से कहें।"


engine = Engine()