# Generated from TodoList.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,4,7,63,8,7,11,7,12,7,64,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,4,10,82,8,10,11,10,12,10,83,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,4,11,99,
        8,11,11,11,12,11,100,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,
        18,20,22,0,0,105,0,24,1,0,0,0,2,28,1,0,0,0,4,33,1,0,0,0,6,38,1,0,
        0,0,8,44,1,0,0,0,10,49,1,0,0,0,12,54,1,0,0,0,14,59,1,0,0,0,16,68,
        1,0,0,0,18,73,1,0,0,0,20,78,1,0,0,0,22,98,1,0,0,0,24,25,5,1,0,0,
        25,26,5,14,0,0,26,27,5,2,0,0,27,1,1,0,0,0,28,29,5,3,0,0,29,30,5,
        14,0,0,30,31,5,15,0,0,31,32,5,2,0,0,32,3,1,0,0,0,33,34,5,4,0,0,34,
        35,5,14,0,0,35,36,5,16,0,0,36,37,5,2,0,0,37,5,1,0,0,0,38,39,5,5,
        0,0,39,40,5,14,0,0,40,41,5,6,0,0,41,42,5,14,0,0,42,43,5,2,0,0,43,
        7,1,0,0,0,44,45,5,7,0,0,45,46,5,14,0,0,46,47,5,14,0,0,47,48,5,2,
        0,0,48,9,1,0,0,0,49,50,5,8,0,0,50,51,5,14,0,0,51,52,5,18,0,0,52,
        53,5,2,0,0,53,11,1,0,0,0,54,55,5,9,0,0,55,56,5,14,0,0,56,57,5,14,
        0,0,57,58,5,2,0,0,58,13,1,0,0,0,59,60,5,10,0,0,60,62,5,16,0,0,61,
        63,5,14,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,
        0,0,65,66,1,0,0,0,66,67,5,2,0,0,67,15,1,0,0,0,68,69,5,11,0,0,69,
        70,5,14,0,0,70,71,5,16,0,0,71,72,5,2,0,0,72,17,1,0,0,0,73,74,5,12,
        0,0,74,75,5,14,0,0,75,76,5,15,0,0,76,77,5,2,0,0,77,19,1,0,0,0,78,
        79,5,13,0,0,79,81,5,14,0,0,80,82,5,14,0,0,81,80,1,0,0,0,82,83,1,
        0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,2,0,0,86,
        21,1,0,0,0,87,99,3,0,0,0,88,99,3,2,1,0,89,99,3,4,2,0,90,99,3,16,
        8,0,91,99,3,18,9,0,92,99,3,6,3,0,93,99,3,8,4,0,94,99,3,10,5,0,95,
        99,3,12,6,0,96,99,3,14,7,0,97,99,3,20,10,0,98,87,1,0,0,0,98,88,1,
        0,0,0,98,89,1,0,0,0,98,90,1,0,0,0,98,91,1,0,0,0,98,92,1,0,0,0,98,
        93,1,0,0,0,98,94,1,0,0,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,
        0,99,100,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,
        102,103,5,0,0,1,103,23,1,0,0,0,4,64,83,98,100
    ]

class TodoListParser ( Parser ):

    grammarFileName = "TodoList.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'task'", "';'", "'priority'", "'deadline'", 
                     "'dependency'", "'on'", "'tag'", "'status'", "'note'", 
                     "'groupDeadline'", "'start'", "'duration'", "'resource'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "DATE", 
                      "WS", "STATUS" ]

    RULE_task = 0
    RULE_priority = 1
    RULE_deadline = 2
    RULE_dependency = 3
    RULE_tag = 4
    RULE_status = 5
    RULE_note = 6
    RULE_groupDeadline = 7
    RULE_start = 8
    RULE_duration = 9
    RULE_resource = 10
    RULE_file = 11

    ruleNames =  [ "task", "priority", "deadline", "dependency", "tag", 
                   "status", "note", "groupDeadline", "start", "duration", 
                   "resource", "file" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    STRING=14
    NUMBER=15
    DATE=16
    WS=17
    STATUS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TaskContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TodoListParser.STRING, 0)

        def getRuleIndex(self):
            return TodoListParser.RULE_task

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask" ):
                listener.enterTask(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask" ):
                listener.exitTask(self)




    def task(self):

        localctx = TodoListParser.TaskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_task)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(TodoListParser.T__0)
            self.state = 25
            self.match(TodoListParser.STRING)
            self.state = 26
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PriorityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TodoListParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(TodoListParser.NUMBER, 0)

        def getRuleIndex(self):
            return TodoListParser.RULE_priority

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPriority" ):
                listener.enterPriority(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPriority" ):
                listener.exitPriority(self)




    def priority(self):

        localctx = TodoListParser.PriorityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_priority)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(TodoListParser.T__2)
            self.state = 29
            self.match(TodoListParser.STRING)
            self.state = 30
            self.match(TodoListParser.NUMBER)
            self.state = 31
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeadlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TodoListParser.STRING, 0)

        def DATE(self):
            return self.getToken(TodoListParser.DATE, 0)

        def getRuleIndex(self):
            return TodoListParser.RULE_deadline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeadline" ):
                listener.enterDeadline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeadline" ):
                listener.exitDeadline(self)




    def deadline(self):

        localctx = TodoListParser.DeadlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_deadline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(TodoListParser.T__3)
            self.state = 34
            self.match(TodoListParser.STRING)
            self.state = 35
            self.match(TodoListParser.DATE)
            self.state = 36
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DependencyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TodoListParser.STRING)
            else:
                return self.getToken(TodoListParser.STRING, i)

        def getRuleIndex(self):
            return TodoListParser.RULE_dependency

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDependency" ):
                listener.enterDependency(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDependency" ):
                listener.exitDependency(self)




    def dependency(self):

        localctx = TodoListParser.DependencyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dependency)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(TodoListParser.T__4)
            self.state = 39
            self.match(TodoListParser.STRING)
            self.state = 40
            self.match(TodoListParser.T__5)
            self.state = 41
            self.match(TodoListParser.STRING)
            self.state = 42
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TodoListParser.STRING)
            else:
                return self.getToken(TodoListParser.STRING, i)

        def getRuleIndex(self):
            return TodoListParser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)




    def tag(self):

        localctx = TodoListParser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(TodoListParser.T__6)
            self.state = 45
            self.match(TodoListParser.STRING)
            self.state = 46
            self.match(TodoListParser.STRING)
            self.state = 47
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TodoListParser.STRING, 0)

        def STATUS(self):
            return self.getToken(TodoListParser.STATUS, 0)

        def getRuleIndex(self):
            return TodoListParser.RULE_status

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatus" ):
                listener.enterStatus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatus" ):
                listener.exitStatus(self)




    def status(self):

        localctx = TodoListParser.StatusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_status)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(TodoListParser.T__7)
            self.state = 50
            self.match(TodoListParser.STRING)
            self.state = 51
            self.match(TodoListParser.STATUS)
            self.state = 52
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TodoListParser.STRING)
            else:
                return self.getToken(TodoListParser.STRING, i)

        def getRuleIndex(self):
            return TodoListParser.RULE_note

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNote" ):
                listener.enterNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNote" ):
                listener.exitNote(self)




    def note(self):

        localctx = TodoListParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(TodoListParser.T__8)
            self.state = 55
            self.match(TodoListParser.STRING)
            self.state = 56
            self.match(TodoListParser.STRING)
            self.state = 57
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupDeadlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(TodoListParser.DATE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TodoListParser.STRING)
            else:
                return self.getToken(TodoListParser.STRING, i)

        def getRuleIndex(self):
            return TodoListParser.RULE_groupDeadline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupDeadline" ):
                listener.enterGroupDeadline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupDeadline" ):
                listener.exitGroupDeadline(self)




    def groupDeadline(self):

        localctx = TodoListParser.GroupDeadlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_groupDeadline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(TodoListParser.T__9)
            self.state = 60
            self.match(TodoListParser.DATE)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.match(TodoListParser.STRING)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 66
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TodoListParser.STRING, 0)

        def DATE(self):
            return self.getToken(TodoListParser.DATE, 0)

        def getRuleIndex(self):
            return TodoListParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = TodoListParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(TodoListParser.T__10)
            self.state = 69
            self.match(TodoListParser.STRING)
            self.state = 70
            self.match(TodoListParser.DATE)
            self.state = 71
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TodoListParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(TodoListParser.NUMBER, 0)

        def getRuleIndex(self):
            return TodoListParser.RULE_duration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDuration" ):
                listener.enterDuration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDuration" ):
                listener.exitDuration(self)




    def duration(self):

        localctx = TodoListParser.DurationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_duration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(TodoListParser.T__11)
            self.state = 74
            self.match(TodoListParser.STRING)
            self.state = 75
            self.match(TodoListParser.NUMBER)
            self.state = 76
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TodoListParser.STRING)
            else:
                return self.getToken(TodoListParser.STRING, i)

        def getRuleIndex(self):
            return TodoListParser.RULE_resource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource" ):
                listener.enterResource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource" ):
                listener.exitResource(self)




    def resource(self):

        localctx = TodoListParser.ResourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_resource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(TodoListParser.T__12)
            self.state = 79
            self.match(TodoListParser.STRING)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.match(TodoListParser.STRING)
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

            self.state = 85
            self.match(TodoListParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TodoListParser.EOF, 0)

        def task(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.TaskContext)
            else:
                return self.getTypedRuleContext(TodoListParser.TaskContext,i)


        def priority(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.PriorityContext)
            else:
                return self.getTypedRuleContext(TodoListParser.PriorityContext,i)


        def deadline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.DeadlineContext)
            else:
                return self.getTypedRuleContext(TodoListParser.DeadlineContext,i)


        def start(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.StartContext)
            else:
                return self.getTypedRuleContext(TodoListParser.StartContext,i)


        def duration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.DurationContext)
            else:
                return self.getTypedRuleContext(TodoListParser.DurationContext,i)


        def dependency(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.DependencyContext)
            else:
                return self.getTypedRuleContext(TodoListParser.DependencyContext,i)


        def tag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.TagContext)
            else:
                return self.getTypedRuleContext(TodoListParser.TagContext,i)


        def status(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.StatusContext)
            else:
                return self.getTypedRuleContext(TodoListParser.StatusContext,i)


        def note(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.NoteContext)
            else:
                return self.getTypedRuleContext(TodoListParser.NoteContext,i)


        def groupDeadline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.GroupDeadlineContext)
            else:
                return self.getTypedRuleContext(TodoListParser.GroupDeadlineContext,i)


        def resource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.ResourceContext)
            else:
                return self.getTypedRuleContext(TodoListParser.ResourceContext,i)


        def getRuleIndex(self):
            return TodoListParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file_(self):

        localctx = TodoListParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 87
                    self.task()
                    pass
                elif token in [3]:
                    self.state = 88
                    self.priority()
                    pass
                elif token in [4]:
                    self.state = 89
                    self.deadline()
                    pass
                elif token in [11]:
                    self.state = 90
                    self.start()
                    pass
                elif token in [12]:
                    self.state = 91
                    self.duration()
                    pass
                elif token in [5]:
                    self.state = 92
                    self.dependency()
                    pass
                elif token in [7]:
                    self.state = 93
                    self.tag()
                    pass
                elif token in [8]:
                    self.state = 94
                    self.status()
                    pass
                elif token in [9]:
                    self.state = 95
                    self.note()
                    pass
                elif token in [10]:
                    self.state = 96
                    self.groupDeadline()
                    pass
                elif token in [13]:
                    self.state = 97
                    self.resource()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16314) != 0)):
                    break

            self.state = 102
            self.match(TodoListParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





