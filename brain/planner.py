"""
ARIS V13 Planner Engine
"""

from datetime import datetime


class Planner:

    def create_plan(self, goal):

        goal = goal.lower().strip()

        plan = []

        if "python" in goal:

            plan = [
                "Python Basics",
                "Functions",
                "OOP",
                "File Handling",
                "Projects"
            ]

        elif "aris" in goal:

            plan = [
                "Analyze Request",
                "Select Engine",
                "Execute Task",
                "Verify Result",
                "Learn From Result"
            ]

        elif "study" in goal:

            plan = [
                "Read Theory",
                "Make Notes",
                "Practice Questions",
                "Revision",
                "Mock Test"
            ]

        else:

            plan = [
                "Understand Goal",
                "Break Into Steps",
                "Execute Step",
                "Verify",
                "Finish"
            ]

        return {
            "goal": goal,
            "created": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "steps": plan,
            "completed": 0
        }

    def next_step(self, plan):

        completed = plan["completed"]

        if completed >= len(plan["steps"]):
            return "Plan Completed"

        return plan["steps"][completed]

    def complete_step(self, plan):

        if plan["completed"] < len(plan["steps"]):
            plan["completed"] += 1

        return plan


planner = Planner()