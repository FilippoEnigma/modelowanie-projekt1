# Generated from TodoList.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,86,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,4,6,60,8,6,
        11,6,12,6,61,1,6,1,6,1,7,4,7,67,8,7,11,7,12,7,68,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,4,9,81,8,9,11,9,12,9,82,1,9,1,9,0,0,10,1,
        1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,2,4,0,32,32,48,57,
        65,90,97,122,3,0,9,10,13,13,32,32,88,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,26,1,0,0,0,5,28,1,
        0,0,0,7,37,1,0,0,0,9,46,1,0,0,0,11,54,1,0,0,0,13,57,1,0,0,0,15,66,
        1,0,0,0,17,70,1,0,0,0,19,80,1,0,0,0,21,22,5,116,0,0,22,23,5,97,0,
        0,23,24,5,115,0,0,24,25,5,107,0,0,25,2,1,0,0,0,26,27,5,59,0,0,27,
        4,1,0,0,0,28,29,5,112,0,0,29,30,5,114,0,0,30,31,5,105,0,0,31,32,
        5,111,0,0,32,33,5,114,0,0,33,34,5,105,0,0,34,35,5,116,0,0,35,36,
        5,121,0,0,36,6,1,0,0,0,37,38,5,100,0,0,38,39,5,101,0,0,39,40,5,97,
        0,0,40,41,5,100,0,0,41,42,5,108,0,0,42,43,5,105,0,0,43,44,5,110,
        0,0,44,45,5,101,0,0,45,8,1,0,0,0,46,47,5,100,0,0,47,48,5,101,0,0,
        48,49,5,112,0,0,49,50,5,101,0,0,50,51,5,110,0,0,51,52,5,100,0,0,
        52,53,5,115,0,0,53,10,1,0,0,0,54,55,5,111,0,0,55,56,5,110,0,0,56,
        12,1,0,0,0,57,59,5,34,0,0,58,60,7,0,0,0,59,58,1,0,0,0,60,61,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,34,0,0,64,
        14,1,0,0,0,65,67,2,48,57,0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,
        0,0,68,69,1,0,0,0,69,16,1,0,0,0,70,71,2,48,57,0,71,72,6,8,0,0,72,
        73,5,45,0,0,73,74,2,48,57,0,74,75,6,8,1,0,75,76,5,45,0,0,76,77,2,
        48,57,0,77,78,6,8,2,0,78,18,1,0,0,0,79,81,7,1,0,0,80,79,1,0,0,0,
        81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,6,
        9,3,0,85,20,1,0,0,0,4,0,61,68,82,4,1,8,0,1,8,1,1,8,2,6,0,0
    ]

class TodoListLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    STRING = 7
    NUMBER = 8
    DATE = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'task'", "';'", "'priority'", "'deadline'", "'depends'", "'on'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "NUMBER", "DATE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "STRING", 
                  "NUMBER", "DATE", "WS" ]

    grammarFileName = "TodoList.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.DATE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def DATE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            2
     

        if actionIndex == 1:
            2
     

        if actionIndex == 2:
            4
     

