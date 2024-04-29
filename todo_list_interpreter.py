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
        task_name = ctx.STRING().getText().strip('"')
        priority = int(ctx.NUMBER().getText())
        self.task_list.set_priority(task_name, priority)

    def exitDeadline(self, ctx: TodoListParser.DeadlineContext):
        task_name = ctx.STRING().getText().strip('"')
        deadline_token = ctx.DATE()
        if deadline_token is not None:
            deadline = deadline_token.getText()
            self.task_list.set_deadline(task_name, deadline)
        else:
            print(f"Error parsing deadline for task: {task_name}")

    def exitDependency(self, ctx:TodoListParser.DependencyContext):
        task_name = ctx.STRING(0).getText().strip('"')
        dependency_name = ctx.STRING(1).getText().strip('"')
        self.task_list.add_dependency(task_name, dependency_name)

    def exitTag(self, ctx: TodoListParser.TagContext):
        task_name = ctx.STRING(0).getText().strip('"')
        tag = ctx.STRING(1).getText().strip('"')
        if task_name in self.task_list.tasks:
            self.task_list.tasks[task_name].add_tag(tag)
        else:
            print(f"Warning: Task named '{task_name}' not found when adding tag '{tag}'.")

    def exitStatus(self, ctx):
        task_name = ctx.STRING().getText().strip('"')
        status = ctx.STATUS().getText()
        if task_name in self.task_list.tasks:
            self.task_list.tasks[task_name].set_status(status)
        else:
            print(f"Warning: Task named '{task_name}' not found when setting status '{status}'.")

    def exitNote(self, ctx: TodoListParser.NoteContext):
        task_name = ctx.STRING(0).getText().strip('"')
        note_content = ctx.STRING(1).getText().strip('"')
        if task_name in self.task_list.tasks:
            self.task_list.tasks[task_name].add_note(note_content)
        else:
            print(f"Warning: Task named '{task_name}' not found when adding note '{note_content}'.")

    def exitGroupDeadline(self, ctx: TodoListParser.GroupDeadlineContext):
        deadline = ctx.DATE().getText()
        task_names = [string.getText().strip('"') for string in ctx.STRING()]
        for task_name in task_names:
            if task_name in self.task_list.tasks:
                self.task_list.set_deadline(task_name, deadline)
            else:
                print(f"Warning: Task named '{task_name}' not found when setting group deadline '{deadline}'.")

    def exitStart(self, ctx: TodoListParser.StartContext):
        task_name = ctx.STRING().getText().strip('"')
        start_date = ctx.DATE().getText()
        if task_name in self.task_list.tasks:
            self.task_list.tasks[task_name].start_date = start_date
        else:
            print(f"Warning: Task named '{task_name}' not found when setting start date '{start_date}'.")

    def exitDuration(self, ctx: TodoListParser.DurationContext):
        task_name = ctx.STRING().getText().strip('"')
        duration = int(ctx.NUMBER().getText())
        if task_name in self.task_list.tasks:
            self.task_list.tasks[task_name].duration = duration
        else:
            print(f"Warning: Task named '{task_name}' not found when setting duration.")

    def exitResource(self, ctx: TodoListParser.ResourceContext):
        task_name = ctx.STRING(0).getText().strip('"')
        resources = [resource.getText().strip('"') for resource in ctx.STRING()[1:]]
        if task_name in self.task_list.tasks:
            self.task_list.tasks[task_name].resources.extend(resources)
        else:
            print(f"Warning: Task named '{task_name}' not found when setting resources.")


