class ActionMemory:

    def __init__(self):

        self.last_action = ""
        self.last_target = ""

    def remember(self, action, target):

        self.last_action = action
        self.last_target = target

    def action(self):
        return self.last_action

    def target(self):
        return self.last_target


action_memory = ActionMemory()