# Generated from TodoList.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TodoListParser import TodoListParser
else:
    from TodoListParser import TodoListParser

# This class defines a complete listener for a parse tree produced by TodoListParser.
class TodoListListener(ParseTreeListener):

    # Enter a parse tree produced by TodoListParser#task.
    def enterTask(self, ctx:TodoListParser.TaskContext):
        pass

    # Exit a parse tree produced by TodoListParser#task.
    def exitTask(self, ctx:TodoListParser.TaskContext):
        pass


    # Enter a parse tree produced by TodoListParser#priority.
    def enterPriority(self, ctx:TodoListParser.PriorityContext):
        pass

    # Exit a parse tree produced by TodoListParser#priority.
    def exitPriority(self, ctx:TodoListParser.PriorityContext):
        pass


    # Enter a parse tree produced by TodoListParser#deadline.
    def enterDeadline(self, ctx:TodoListParser.DeadlineContext):
        pass

    # Exit a parse tree produced by TodoListParser#deadline.
    def exitDeadline(self, ctx:TodoListParser.DeadlineContext):
        pass


    # Enter a parse tree produced by TodoListParser#dependency.
    def enterDependency(self, ctx:TodoListParser.DependencyContext):
        pass

    # Exit a parse tree produced by TodoListParser#dependency.
    def exitDependency(self, ctx:TodoListParser.DependencyContext):
        pass


    # Enter a parse tree produced by TodoListParser#file.
    def enterFile(self, ctx:TodoListParser.FileContext):
        pass

    # Exit a parse tree produced by TodoListParser#file.
    def exitFile(self, ctx:TodoListParser.FileContext):
        pass



del TodoListParser