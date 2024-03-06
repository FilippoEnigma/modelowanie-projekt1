from antlr4 import *
from TodoListLexer import TodoListLexer
from TodoListParser import TodoListParser
from TodoListListener import TodoListListener
from task_list import TaskList
from task import Task


class TodoListInterpreter(TodoListListener):
    def __init__(self):
        self.task_list = TaskList()

    def exitTask(self, ctx:TodoListParser.TaskContext):
        task_name = ctx.STRING().getText().strip('"')
        self.task_list.add_task(Task(name=task_name))

    def exitPriority(self, ctx:TodoListParser.PriorityContext):
        task_name = ctx.STRING(0).getText().strip('"')
        priority = int(ctx.NUMBER().getText())
        self.task_list.set_priority(task_name, priority)

    def exitDeadline(self, ctx:TodoListParser.DeadlineContext):
        task_name = ctx.STRING().getText().strip('"')
        deadline = ctx.DATE().getText()
        self.task_list.set_deadline(task_name, deadline)

    def exitDependency(self, ctx:TodoListParser.DependencyContext):
        task_name = ctx.STRING(0).getText().strip('"')
        dependency_name = ctx.STRING(1).getText().strip('"')
        self.task_list.add_dependency(task_name, dependency_name)
