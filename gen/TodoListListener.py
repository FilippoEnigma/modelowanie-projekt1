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


    # Enter a parse tree produced by TodoListParser#tag.
    def enterTag(self, ctx:TodoListParser.TagContext):
        pass

    # Exit a parse tree produced by TodoListParser#tag.
    def exitTag(self, ctx:TodoListParser.TagContext):
        pass


    # Enter a parse tree produced by TodoListParser#status.
    def enterStatus(self, ctx:TodoListParser.StatusContext):
        pass

    # Exit a parse tree produced by TodoListParser#status.
    def exitStatus(self, ctx:TodoListParser.StatusContext):
        pass


    # Enter a parse tree produced by TodoListParser#note.
    def enterNote(self, ctx:TodoListParser.NoteContext):
        pass

    # Exit a parse tree produced by TodoListParser#note.
    def exitNote(self, ctx:TodoListParser.NoteContext):
        pass


    # Enter a parse tree produced by TodoListParser#groupDeadline.
    def enterGroupDeadline(self, ctx:TodoListParser.GroupDeadlineContext):
        pass

    # Exit a parse tree produced by TodoListParser#groupDeadline.
    def exitGroupDeadline(self, ctx:TodoListParser.GroupDeadlineContext):
        pass


    # Enter a parse tree produced by TodoListParser#start.
    def enterStart(self, ctx:TodoListParser.StartContext):
        pass

    # Exit a parse tree produced by TodoListParser#start.
    def exitStart(self, ctx:TodoListParser.StartContext):
        pass


    # Enter a parse tree produced by TodoListParser#duration.
    def enterDuration(self, ctx:TodoListParser.DurationContext):
        pass

    # Exit a parse tree produced by TodoListParser#duration.
    def exitDuration(self, ctx:TodoListParser.DurationContext):
        pass


    # Enter a parse tree produced by TodoListParser#resource.
    def enterResource(self, ctx:TodoListParser.ResourceContext):
        pass

    # Exit a parse tree produced by TodoListParser#resource.
    def exitResource(self, ctx:TodoListParser.ResourceContext):
        pass


    # Enter a parse tree produced by TodoListParser#file.
    def enterFile(self, ctx:TodoListParser.FileContext):
        pass

    # Exit a parse tree produced by TodoListParser#file.
    def exitFile(self, ctx:TodoListParser.FileContext):
        pass



del TodoListParser