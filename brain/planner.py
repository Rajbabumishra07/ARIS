"""
ARIS V14 Planner Engine
Author : Raj Babu Mishra
"""

from datetime import datetime


class Planner:

    def __init__(self):

        self.active_plan = None

    # -------------------------------- #

    def create_plan(self, goal):

        goal = goal.strip().lower()

        plans = {

            "python": [
                "Learn Basics",
                "Practice Daily",
                "Build Small Projects",
                "Build Advanced Projects",
                "Master Python"
            ],

            "aris": [
                "Analyze Request",
                "Understand Intent",
                "Reason About Request",
                "Choose Best Action",
                "Execute",
                "Verify Result",
                "Learn From Experience"
            ],

            "study": [
                "Read Theory",
                "Prepare Notes",
                "Solve Questions",
                "Revise",
                "Take Test"
            ]
        }

        steps = plans.get(goal)

        if steps is None:

            steps = [
                "Understand Goal",
                "Break Into Steps",
                "Execute",
                "Verify",
                "Complete"
            ]

        self.active_plan = {

            "goal": goal,
            "created": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "steps": steps,
            "completed": 0

        }

        return self.active_plan

    # -------------------------------- #

    def current_plan(self):

        return self.active_plan

    # -------------------------------- #

    def next_step(self, plan=None):

        if plan is None:
            plan = self.active_plan

        if not plan:
            return None

        index = plan["completed"]

        if index >= len(plan["steps"]):
            return "Plan Completed"

        return plan["steps"][index]

    # -------------------------------- #

    def complete_step(self, plan=None):

        if plan is None:
            plan = self.active_plan

        if not plan:
            return None

        if plan["completed"] < len(plan["steps"]):
            plan["completed"] += 1

        return plan

    # -------------------------------- #

    def reset(self):

        self.active_plan = None


planner = Planner()