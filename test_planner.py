from brain.planner import planner

plan = planner.create_plan("ARIS")

print(plan)

print(planner.next_step(plan))