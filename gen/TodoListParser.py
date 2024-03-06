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
        4,1,10,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,4,4,35,8,4,11,4,12,4,36,1,4,1,4,1,4,0,0,5,0,2,
        4,6,8,0,0,39,0,10,1,0,0,0,2,14,1,0,0,0,4,19,1,0,0,0,6,24,1,0,0,0,
        8,34,1,0,0,0,10,11,5,1,0,0,11,12,5,7,0,0,12,13,5,2,0,0,13,1,1,0,
        0,0,14,15,5,3,0,0,15,16,5,7,0,0,16,17,5,8,0,0,17,18,5,2,0,0,18,3,
        1,0,0,0,19,20,5,4,0,0,20,21,5,7,0,0,21,22,5,9,0,0,22,23,5,2,0,0,
        23,5,1,0,0,0,24,25,5,5,0,0,25,26,5,7,0,0,26,27,5,6,0,0,27,28,5,7,
        0,0,28,29,5,2,0,0,29,7,1,0,0,0,30,35,3,0,0,0,31,35,3,2,1,0,32,35,
        3,4,2,0,33,35,3,6,3,0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,
        34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,38,1,
        0,0,0,38,39,5,0,0,1,39,9,1,0,0,0,2,34,36
    ]

class TodoListParser ( Parser ):

    grammarFileName = "TodoList.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'task'", "';'", "'priority'", "'deadline'", 
                     "'depends'", "'on'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NUMBER", 
                      "DATE", "WS" ]

    RULE_task = 0
    RULE_priority = 1
    RULE_deadline = 2
    RULE_dependency = 3
    RULE_file = 4

    ruleNames =  [ "task", "priority", "deadline", "dependency", "file" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    STRING=7
    NUMBER=8
    DATE=9
    WS=10

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
            self.state = 10
            self.match(TodoListParser.T__0)
            self.state = 11
            self.match(TodoListParser.STRING)
            self.state = 12
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
            self.state = 14
            self.match(TodoListParser.T__2)
            self.state = 15
            self.match(TodoListParser.STRING)
            self.state = 16
            self.match(TodoListParser.NUMBER)
            self.state = 17
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
            self.state = 19
            self.match(TodoListParser.T__3)
            self.state = 20
            self.match(TodoListParser.STRING)
            self.state = 21
            self.match(TodoListParser.DATE)
            self.state = 22
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
            self.state = 24
            self.match(TodoListParser.T__4)
            self.state = 25
            self.match(TodoListParser.STRING)
            self.state = 26
            self.match(TodoListParser.T__5)
            self.state = 27
            self.match(TodoListParser.STRING)
            self.state = 28
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


        def dependency(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TodoListParser.DependencyContext)
            else:
                return self.getTypedRuleContext(TodoListParser.DependencyContext,i)


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
        self.enterRule(localctx, 8, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 30
                    self.task()
                    pass
                elif token in [3]:
                    self.state = 31
                    self.priority()
                    pass
                elif token in [4]:
                    self.state = 32
                    self.deadline()
                    pass
                elif token in [5]:
                    self.state = 33
                    self.dependency()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 58) != 0)):
                    break

            self.state = 38
            self.match(TodoListParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





