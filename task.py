class Task:
    def __init__(self, name, priority=None, deadline=None, dependencies=None):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.dependencies = dependencies if dependencies is not None else []

    def __repr__(self):
        return f"Task(name={self.name}, priority={self.priority}, deadline={self.deadline}, dependencies={len(self.dependencies)})"
