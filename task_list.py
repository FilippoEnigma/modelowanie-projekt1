from task import Task

class TaskList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task.name in self.tasks:
            raise ValueError("Task with the same name already exists.")
        self.tasks[task.name] = task

    def set_priority(self, task_name, priority):
        if task_name not in self.tasks:
            raise ValueError("Task not found.")
        self.tasks[task_name].priority = priority

    def set_deadline(self, task_name, deadline):
        if task_name not in self.tasks:
            raise ValueError("Task not found.")
        self.tasks[task_name].deadline = deadline

    def add_dependency(self, task_name, dependency_name):
        if task_name not in self.tasks or dependency_name not in self.tasks:
            raise ValueError("Task not found.")
        self.tasks[task_name].dependencies.append(dependency_name)

    def set_deadline(self, task_name, deadline):
        if task_name in self.tasks:
            self.tasks[task_name].deadline = deadline
        else:
            raise ValueError(f"Task named '{task_name}' not found.")

    def __repr__(self):
        return "\n".join(str(task) for task in self.tasks.values())
