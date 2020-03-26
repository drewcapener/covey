class Matrix:
    def __init__(self):
        self.urgent_important = []
        self.urgent_nimportant = []
        self.nurgent_important = []
        self.nurgent_nimportant = []

    def add_urgent_important(self, task):
        self.urgent_important.append(task)

    def add_urgent_nimportant(self, task):
        self.urgent_nimportant.append(task)

    def add_nurgent_important(self, task):
        self.urgent_nimportant.append(task)

    def add_nurgent_nimportant(self, task):
        self.urgent_nimportant.append(task)

    def remove_urgent_important(self, task):
        self.urgent_important.remove(task)

    def remove_urgent_nimportant(self, task):
        self.urgent_nimportant.remove(task)

    def remove_nurgent_important(self, task):
        self.urgent_nimportant.remove(task)

    def remove_nurgent_nimportant(self, task):
        self.urgent_nimportant.remove(task)

    def get_urgent_important(self, task):
        self.urgent_important.remove(task)

    def get_urgent_nimportant(self, task):
        self.urgent_nimportant.remove(task)

    def get_nurgent_important(self, task):
        self.urgent_nimportant.remove(task)

    def get_nurgent_nimportant(self, task):
        self.urgent_nimportant.remove(task)

