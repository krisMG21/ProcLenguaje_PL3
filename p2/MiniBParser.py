# Generated from MiniB.g4 by ANTLR 4.13.2
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
        4,1,39,225,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,4,0,37,8,0,11,0,12,0,38,5,
        0,41,8,0,10,0,12,0,44,9,0,1,0,3,0,47,8,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,85,
        8,6,10,6,12,6,88,9,6,1,6,1,6,1,6,1,6,1,6,5,6,95,8,6,10,6,12,6,98,
        9,6,3,6,100,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        5,7,114,8,7,10,7,12,7,117,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,127,8,8,10,8,12,8,130,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,139,
        8,9,10,9,12,9,142,9,9,1,9,1,9,1,9,1,10,1,10,3,10,149,8,10,1,11,1,
        11,3,11,153,8,11,1,12,1,12,1,12,1,12,1,12,3,12,160,8,12,1,13,1,13,
        1,13,1,13,1,13,3,13,167,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,3,14,177,8,14,1,14,1,14,1,14,1,14,5,14,183,8,14,10,14,12,14,
        186,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,197,8,
        15,1,15,1,15,1,15,1,15,5,15,203,8,15,10,15,12,15,206,9,15,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,3,16,223,8,16,1,16,0,2,28,30,17,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,0,0,244,0,42,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,0,6,
        66,1,0,0,0,8,70,1,0,0,0,10,73,1,0,0,0,12,77,1,0,0,0,14,103,1,0,0,
        0,16,120,1,0,0,0,18,133,1,0,0,0,20,148,1,0,0,0,22,152,1,0,0,0,24,
        159,1,0,0,0,26,166,1,0,0,0,28,176,1,0,0,0,30,196,1,0,0,0,32,222,
        1,0,0,0,34,36,3,2,1,0,35,37,5,37,0,0,36,35,1,0,0,0,37,38,1,0,0,0,
        38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,34,1,0,0,0,41,44,1,
        0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,45,
        47,3,2,1,0,46,45,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,5,0,0,
        1,49,1,1,0,0,0,50,60,3,4,2,0,51,60,3,6,3,0,52,60,3,8,4,0,53,60,3,
        10,5,0,54,60,3,12,6,0,55,60,3,14,7,0,56,60,3,16,8,0,57,60,3,18,9,
        0,58,60,3,20,10,0,59,50,1,0,0,0,59,51,1,0,0,0,59,52,1,0,0,0,59,53,
        1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,59,56,1,0,0,0,59,57,1,0,0,0,
        59,58,1,0,0,0,60,3,1,0,0,0,61,62,5,15,0,0,62,63,5,34,0,0,63,64,5,
        1,0,0,64,65,3,30,15,0,65,5,1,0,0,0,66,67,5,34,0,0,67,68,5,1,0,0,
        68,69,3,30,15,0,69,7,1,0,0,0,70,71,5,16,0,0,71,72,3,30,15,0,72,9,
        1,0,0,0,73,74,5,17,0,0,74,75,5,36,0,0,75,76,5,34,0,0,76,11,1,0,0,
        0,77,78,5,18,0,0,78,79,3,28,14,0,79,80,5,29,0,0,80,86,5,37,0,0,81,
        82,3,2,1,0,82,83,5,37,0,0,83,85,1,0,0,0,84,81,1,0,0,0,85,88,1,0,
        0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,99,1,0,0,0,88,86,1,0,0,0,89,90,
        5,19,0,0,90,96,5,37,0,0,91,92,3,2,1,0,92,93,5,37,0,0,93,95,1,0,0,
        0,94,91,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,100,
        1,0,0,0,98,96,1,0,0,0,99,89,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,
        0,101,102,5,28,0,0,102,13,1,0,0,0,103,104,5,20,0,0,104,105,5,34,
        0,0,105,106,5,1,0,0,106,107,3,30,15,0,107,108,5,21,0,0,108,109,3,
        30,15,0,109,115,5,37,0,0,110,111,3,2,1,0,111,112,5,37,0,0,112,114,
        1,0,0,0,113,110,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,
        1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,5,22,0,0,119,15,
        1,0,0,0,120,121,5,23,0,0,121,122,3,28,14,0,122,128,5,37,0,0,123,
        124,3,2,1,0,124,125,5,37,0,0,125,127,1,0,0,0,126,123,1,0,0,0,127,
        130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,
        128,1,0,0,0,131,132,5,28,0,0,132,17,1,0,0,0,133,134,5,24,0,0,134,
        140,5,37,0,0,135,136,3,2,1,0,136,137,5,37,0,0,137,139,1,0,0,0,138,
        135,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,
        143,1,0,0,0,142,140,1,0,0,0,143,144,5,25,0,0,144,145,3,28,14,0,145,
        19,1,0,0,0,146,149,5,26,0,0,147,149,5,27,0,0,148,146,1,0,0,0,148,
        147,1,0,0,0,149,21,1,0,0,0,150,153,5,13,0,0,151,153,5,14,0,0,152,
        150,1,0,0,0,152,151,1,0,0,0,153,23,1,0,0,0,154,160,5,2,0,0,155,160,
        5,3,0,0,156,160,5,4,0,0,157,160,5,5,0,0,158,160,5,1,0,0,159,154,
        1,0,0,0,159,155,1,0,0,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,
        1,0,0,0,160,25,1,0,0,0,161,167,5,6,0,0,162,167,5,7,0,0,163,167,5,
        8,0,0,164,167,5,9,0,0,165,167,5,30,0,0,166,161,1,0,0,0,166,162,1,
        0,0,0,166,163,1,0,0,0,166,164,1,0,0,0,166,165,1,0,0,0,167,27,1,0,
        0,0,168,169,6,14,-1,0,169,170,3,30,15,0,170,171,3,24,12,0,171,172,
        3,30,15,0,172,177,1,0,0,0,173,174,5,12,0,0,174,177,3,28,14,3,175,
        177,3,30,15,0,176,168,1,0,0,0,176,173,1,0,0,0,176,175,1,0,0,0,177,
        184,1,0,0,0,178,179,10,2,0,0,179,180,3,22,11,0,180,181,3,28,14,3,
        181,183,1,0,0,0,182,178,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,
        184,185,1,0,0,0,185,29,1,0,0,0,186,184,1,0,0,0,187,188,6,15,-1,0,
        188,189,5,10,0,0,189,190,3,30,15,0,190,191,5,11,0,0,191,197,1,0,
        0,0,192,197,3,32,16,0,193,197,5,35,0,0,194,197,5,36,0,0,195,197,
        5,34,0,0,196,187,1,0,0,0,196,192,1,0,0,0,196,193,1,0,0,0,196,194,
        1,0,0,0,196,195,1,0,0,0,197,204,1,0,0,0,198,199,10,6,0,0,199,200,
        3,26,13,0,200,201,3,30,15,7,201,203,1,0,0,0,202,198,1,0,0,0,203,
        206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,31,1,0,0,0,206,204,
        1,0,0,0,207,208,5,31,0,0,208,209,5,10,0,0,209,210,3,30,15,0,210,
        211,5,11,0,0,211,223,1,0,0,0,212,213,5,32,0,0,213,214,5,10,0,0,214,
        215,3,30,15,0,215,216,5,11,0,0,216,223,1,0,0,0,217,218,5,33,0,0,
        218,219,5,10,0,0,219,220,3,30,15,0,220,221,5,11,0,0,221,223,1,0,
        0,0,222,207,1,0,0,0,222,212,1,0,0,0,222,217,1,0,0,0,223,33,1,0,0,
        0,19,38,42,46,59,86,96,99,115,128,140,148,152,159,166,176,184,196,
        204,222
    ]

class MiniBParser ( Parser ):

    grammarFileName = "MiniB.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'<'", "'>'", "'<='", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NOT", "AND", "OR", "LET", "PRINT", "INPUT", "IF", 
                      "ELSE", "FOR", "TO", "NEXT", "WHILE", "REPEAT", "UNTIL", 
                      "CONTINUE", "EXIT", "END", "THEN", "MOD", "VAL", "LEN", 
                      "ISNAN", "ID", "NUMBER", "STRING_LITERAL", "NEWLINE", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_letStmt = 2
    RULE_opStmt = 3
    RULE_printStmt = 4
    RULE_inputStmt = 5
    RULE_ifStmt = 6
    RULE_forStmt = 7
    RULE_whileStmt = 8
    RULE_repeatStmt = 9
    RULE_keyStmt = 10
    RULE_logicalOp = 11
    RULE_comparisonOp = 12
    RULE_arithmeticOp = 13
    RULE_condition = 14
    RULE_expression = 15
    RULE_functionCall = 16

    ruleNames =  [ "program", "statement", "letStmt", "opStmt", "printStmt", 
                   "inputStmt", "ifStmt", "forStmt", "whileStmt", "repeatStmt", 
                   "keyStmt", "logicalOp", "comparisonOp", "arithmeticOp", 
                   "condition", "expression", "functionCall" ]

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
    NOT=12
    AND=13
    OR=14
    LET=15
    PRINT=16
    INPUT=17
    IF=18
    ELSE=19
    FOR=20
    TO=21
    NEXT=22
    WHILE=23
    REPEAT=24
    UNTIL=25
    CONTINUE=26
    EXIT=27
    END=28
    THEN=29
    MOD=30
    VAL=31
    LEN=32
    ISNAN=33
    ID=34
    NUMBER=35
    STRING_LITERAL=36
    NEWLINE=37
    COMMENT=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniBParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniBParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniBParser.NEWLINE)
            else:
                return self.getToken(MiniBParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniBParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniBParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.statement()
                    self.state = 36 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 35
                        self.match(MiniBParser.NEWLINE)
                        self.state = 38 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==37):
                            break
             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17407901696) != 0):
                self.state = 45
                self.statement()


            self.state = 48
            self.match(MiniBParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letStmt(self):
            return self.getTypedRuleContext(MiniBParser.LetStmtContext,0)


        def opStmt(self):
            return self.getTypedRuleContext(MiniBParser.OpStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(MiniBParser.PrintStmtContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(MiniBParser.InputStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniBParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniBParser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MiniBParser.WhileStmtContext,0)


        def repeatStmt(self):
            return self.getTypedRuleContext(MiniBParser.RepeatStmtContext,0)


        def keyStmt(self):
            return self.getTypedRuleContext(MiniBParser.KeyStmtContext,0)


        def getRuleIndex(self):
            return MiniBParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniBParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.letStmt()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.opStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.printStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.inputStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.ifStmt()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.forStmt()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.whileStmt()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 8)
                self.state = 57
                self.repeatStmt()
                pass
            elif token in [26, 27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 58
                self.keyStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_letStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LetContext(LetStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.LetStmtContext
            super().__init__(parser)
            self.id_ = None # Token
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(MiniBParser.LET, 0)
        def ID(self):
            return self.getToken(MiniBParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniBParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLet" ):
                listener.enterLet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLet" ):
                listener.exitLet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)



    def letStmt(self):

        localctx = MiniBParser.LetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_letStmt)
        try:
            localctx = MiniBParser.LetContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(MiniBParser.LET)
            self.state = 62
            localctx.id_ = self.match(MiniBParser.ID)
            self.state = 63
            self.match(MiniBParser.T__0)
            self.state = 64
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_opStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OpContext(OpStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.OpStmtContext
            super().__init__(parser)
            self.id_ = None # Token
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniBParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniBParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)



    def opStmt(self):

        localctx = MiniBParser.OpStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_opStmt)
        try:
            localctx = MiniBParser.OpContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            localctx.id_ = self.match(MiniBParser.ID)
            self.state = 67
            self.match(MiniBParser.T__0)
            self.state = 68
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_printStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(PrintStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.PrintStmtContext
            super().__init__(parser)
            self.exp = None # ExpressionContext
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(MiniBParser.PRINT, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniBParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)



    def printStmt(self):

        localctx = MiniBParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        try:
            localctx = MiniBParser.PrintContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MiniBParser.PRINT)
            self.state = 71
            localctx.exp = self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_inputStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InputContext(InputStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.InputStmtContext
            super().__init__(parser)
            self.str_ = None # Token
            self.id_ = None # Token
            self.copyFrom(ctx)

        def INPUT(self):
            return self.getToken(MiniBParser.INPUT, 0)
        def STRING_LITERAL(self):
            return self.getToken(MiniBParser.STRING_LITERAL, 0)
        def ID(self):
            return self.getToken(MiniBParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)



    def inputStmt(self):

        localctx = MiniBParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inputStmt)
        try:
            localctx = MiniBParser.InputContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MiniBParser.INPUT)
            self.state = 74
            localctx.str_ = self.match(MiniBParser.STRING_LITERAL)
            self.state = 75
            localctx.id_ = self.match(MiniBParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_ifStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfContext(IfStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.IfStmtContext
            super().__init__(parser)
            self.cond = None # ConditionContext
            self.statif = None # StatementContext
            self.statelse = None # StatementContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiniBParser.IF, 0)
        def THEN(self):
            return self.getToken(MiniBParser.THEN, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniBParser.NEWLINE)
            else:
                return self.getToken(MiniBParser.NEWLINE, i)
        def END(self):
            return self.getToken(MiniBParser.END, 0)
        def condition(self):
            return self.getTypedRuleContext(MiniBParser.ConditionContext,0)

        def ELSE(self):
            return self.getToken(MiniBParser.ELSE, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniBParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def ifStmt(self):

        localctx = MiniBParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            localctx = MiniBParser.IfContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(MiniBParser.IF)
            self.state = 78
            localctx.cond = self.condition(0)
            self.state = 79
            self.match(MiniBParser.THEN)
            self.state = 80
            self.match(MiniBParser.NEWLINE)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17407901696) != 0):
                self.state = 81
                localctx.statif = self.statement()
                self.state = 82
                self.match(MiniBParser.NEWLINE)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 89
                self.match(MiniBParser.ELSE)
                self.state = 90
                self.match(MiniBParser.NEWLINE)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17407901696) != 0):
                    self.state = 91
                    localctx.statelse = self.statement()
                    self.state = 92
                    self.match(MiniBParser.NEWLINE)
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 101
            self.match(MiniBParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_forStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForContext(ForStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ForStmtContext
            super().__init__(parser)
            self.id_ = None # Token
            self.exp1 = None # ExpressionContext
            self.exp2 = None # ExpressionContext
            self.stat = None # StatementContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(MiniBParser.FOR, 0)
        def TO(self):
            return self.getToken(MiniBParser.TO, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniBParser.NEWLINE)
            else:
                return self.getToken(MiniBParser.NEWLINE, i)
        def NEXT(self):
            return self.getToken(MiniBParser.NEXT, 0)
        def ID(self):
            return self.getToken(MiniBParser.ID, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniBParser.ExpressionContext,i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniBParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)



    def forStmt(self):

        localctx = MiniBParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            localctx = MiniBParser.ForContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(MiniBParser.FOR)
            self.state = 104
            localctx.id_ = self.match(MiniBParser.ID)
            self.state = 105
            self.match(MiniBParser.T__0)
            self.state = 106
            localctx.exp1 = self.expression(0)
            self.state = 107
            self.match(MiniBParser.TO)
            self.state = 108
            localctx.exp2 = self.expression(0)
            self.state = 109
            self.match(MiniBParser.NEWLINE)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17407901696) != 0):
                self.state = 110
                localctx.stat = self.statement()
                self.state = 111
                self.match(MiniBParser.NEWLINE)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(MiniBParser.NEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_whileStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileContext(WhileStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.WhileStmtContext
            super().__init__(parser)
            self.cond = None # ConditionContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(MiniBParser.WHILE, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniBParser.NEWLINE)
            else:
                return self.getToken(MiniBParser.NEWLINE, i)
        def END(self):
            return self.getToken(MiniBParser.END, 0)
        def condition(self):
            return self.getTypedRuleContext(MiniBParser.ConditionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniBParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)



    def whileStmt(self):

        localctx = MiniBParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            localctx = MiniBParser.WhileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(MiniBParser.WHILE)
            self.state = 121
            localctx.cond = self.condition(0)
            self.state = 122
            self.match(MiniBParser.NEWLINE)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17407901696) != 0):
                self.state = 123
                self.statement()
                self.state = 124
                self.match(MiniBParser.NEWLINE)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(MiniBParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_repeatStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RepeatContext(RepeatStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.RepeatStmtContext
            super().__init__(parser)
            self.cond = None # ConditionContext
            self.copyFrom(ctx)

        def REPEAT(self):
            return self.getToken(MiniBParser.REPEAT, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniBParser.NEWLINE)
            else:
                return self.getToken(MiniBParser.NEWLINE, i)
        def UNTIL(self):
            return self.getToken(MiniBParser.UNTIL, 0)
        def condition(self):
            return self.getTypedRuleContext(MiniBParser.ConditionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniBParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)



    def repeatStmt(self):

        localctx = MiniBParser.RepeatStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_repeatStmt)
        self._la = 0 # Token type
        try:
            localctx = MiniBParser.RepeatContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(MiniBParser.REPEAT)
            self.state = 134
            self.match(MiniBParser.NEWLINE)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17407901696) != 0):
                self.state = 135
                self.statement()
                self.state = 136
                self.match(MiniBParser.NEWLINE)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(MiniBParser.UNTIL)
            self.state = 144
            localctx.cond = self.condition(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_keyStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ContinueContext(KeyStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.KeyStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(MiniBParser.CONTINUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue" ):
                listener.enterContinue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue" ):
                listener.exitContinue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)


    class ExitContext(KeyStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.KeyStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXIT(self):
            return self.getToken(MiniBParser.EXIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit" ):
                listener.enterExit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit" ):
                listener.exitExit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExit" ):
                return visitor.visitExit(self)
            else:
                return visitor.visitChildren(self)



    def keyStmt(self):

        localctx = MiniBParser.KeyStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_keyStmt)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = MiniBParser.ContinueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MiniBParser.CONTINUE)
                pass
            elif token in [27]:
                localctx = MiniBParser.ExitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(MiniBParser.EXIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_logicalOp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrContext(LogicalOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.LogicalOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(MiniBParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(LogicalOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.LogicalOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(MiniBParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)



    def logicalOp(self):

        localctx = MiniBParser.LogicalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logicalOp)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = MiniBParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(MiniBParser.AND)
                pass
            elif token in [14]:
                localctx = MiniBParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(MiniBParser.OR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_comparisonOp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LessThanContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThan" ):
                listener.enterLessThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThan" ):
                listener.exitLessThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class LessThanOrEqualContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThanOrEqual" ):
                listener.enterLessThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThanOrEqual" ):
                listener.exitLessThanOrEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThanOrEqual" ):
                return visitor.visitLessThanOrEqual(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThan" ):
                listener.enterGreaterThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThan" ):
                listener.exitGreaterThan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThan" ):
                return visitor.visitGreaterThan(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanOrEqualContext(ComparisonOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ComparisonOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanOrEqual" ):
                listener.enterGreaterThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanOrEqual" ):
                listener.exitGreaterThanOrEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanOrEqual" ):
                return visitor.visitGreaterThanOrEqual(self)
            else:
                return visitor.visitChildren(self)



    def comparisonOp(self):

        localctx = MiniBParser.ComparisonOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparisonOp)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniBParser.LessThanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(MiniBParser.T__1)
                pass
            elif token in [3]:
                localctx = MiniBParser.GreaterThanContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(MiniBParser.T__2)
                pass
            elif token in [4]:
                localctx = MiniBParser.LessThanOrEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(MiniBParser.T__3)
                pass
            elif token in [5]:
                localctx = MiniBParser.GreaterThanOrEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.match(MiniBParser.T__4)
                pass
            elif token in [1]:
                localctx = MiniBParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(MiniBParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_arithmeticOp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivideContext(ArithmeticOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ArithmeticOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class ModuloContext(ArithmeticOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ArithmeticOpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOD(self):
            return self.getToken(MiniBParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo" ):
                listener.enterModulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo" ):
                listener.exitModulo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulo" ):
                return visitor.visitModulo(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(ArithmeticOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ArithmeticOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class PlusContext(ArithmeticOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ArithmeticOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(ArithmeticOpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ArithmeticOpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus" ):
                listener.enterMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus" ):
                listener.exitMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)



    def arithmeticOp(self):

        localctx = MiniBParser.ArithmeticOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arithmeticOp)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = MiniBParser.PlusContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(MiniBParser.T__5)
                pass
            elif token in [7]:
                localctx = MiniBParser.MinusContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(MiniBParser.T__6)
                pass
            elif token in [8]:
                localctx = MiniBParser.MultiplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(MiniBParser.T__7)
                pass
            elif token in [9]:
                localctx = MiniBParser.DivideContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.match(MiniBParser.T__8)
                pass
            elif token in [30]:
                localctx = MiniBParser.ModuloContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.match(MiniBParser.MOD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniBParser.ExpressionContext,i)


        def comparisonOp(self):
            return self.getTypedRuleContext(MiniBParser.ComparisonOpContext,0)


        def NOT(self):
            return self.getToken(MiniBParser.NOT, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MiniBParser.ConditionContext,i)


        def logicalOp(self):
            return self.getTypedRuleContext(MiniBParser.LogicalOpContext,0)


        def getRuleIndex(self):
            return MiniBParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniBParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 169
                self.expression(0)
                self.state = 170
                self.comparisonOp()
                self.state = 171
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 173
                self.match(MiniBParser.NOT)
                self.state = 174
                self.condition(3)
                pass

            elif la_ == 3:
                self.state = 175
                self.expression(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniBParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 178
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 179
                    self.logicalOp()
                    self.state = 180
                    self.condition(3) 
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BinaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniBParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniBParser.ExpressionContext,i)

        def arithmeticOp(self):
            return self.getTypedRuleContext(MiniBParser.ArithmeticOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpression" ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpression" ):
                listener.exitBinaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpression" ):
                return visitor.visitBinaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ExpressionContext
            super().__init__(parser)
            self.str_ = None # Token
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(MiniBParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ExpressionContext
            super().__init__(parser)
            self.id_ = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniBParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpression" ):
                listener.enterIdExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpression" ):
                listener.exitIdExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpression" ):
                return visitor.visitIdExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MiniBParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)


    class NumberExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ExpressionContext
            super().__init__(parser)
            self.num = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(MiniBParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpression" ):
                listener.enterNumberExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpression" ):
                listener.exitNumberExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpression" ):
                return visitor.visitNumberExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(MiniBParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpression" ):
                return visitor.visitFunctionCallExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniBParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = MiniBParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 188
                self.match(MiniBParser.T__9)
                self.state = 189
                self.expression(0)
                self.state = 190
                self.match(MiniBParser.T__10)
                pass
            elif token in [31, 32, 33]:
                localctx = MiniBParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.functionCall()
                pass
            elif token in [35]:
                localctx = MiniBParser.NumberExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 193
                localctx.num = self.match(MiniBParser.NUMBER)
                pass
            elif token in [36]:
                localctx = MiniBParser.StringExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                localctx.str_ = self.match(MiniBParser.STRING_LITERAL)
                pass
            elif token in [34]:
                localctx = MiniBParser.IdExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                localctx.id_ = self.match(MiniBParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniBParser.BinaryExpressionContext(self, MiniBParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 198
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 199
                    self.arithmeticOp()
                    self.state = 200
                    self.expression(7) 
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniBParser.RULE_functionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IsNanFunctionContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ISNAN(self):
            return self.getToken(MiniBParser.ISNAN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniBParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsNanFunction" ):
                listener.enterIsNanFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsNanFunction" ):
                listener.exitIsNanFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsNanFunction" ):
                return visitor.visitIsNanFunction(self)
            else:
                return visitor.visitChildren(self)


    class ValFunctionContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAL(self):
            return self.getToken(MiniBParser.VAL, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniBParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValFunction" ):
                listener.enterValFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValFunction" ):
                listener.exitValFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValFunction" ):
                return visitor.visitValFunction(self)
            else:
                return visitor.visitChildren(self)


    class LenFunctionContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniBParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEN(self):
            return self.getToken(MiniBParser.LEN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniBParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLenFunction" ):
                listener.enterLenFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLenFunction" ):
                listener.exitLenFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLenFunction" ):
                return visitor.visitLenFunction(self)
            else:
                return visitor.visitChildren(self)



    def functionCall(self):

        localctx = MiniBParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionCall)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = MiniBParser.ValFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(MiniBParser.VAL)
                self.state = 208
                self.match(MiniBParser.T__9)
                self.state = 209
                self.expression(0)
                self.state = 210
                self.match(MiniBParser.T__10)
                pass
            elif token in [32]:
                localctx = MiniBParser.LenFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(MiniBParser.LEN)
                self.state = 213
                self.match(MiniBParser.T__9)
                self.state = 214
                self.expression(0)
                self.state = 215
                self.match(MiniBParser.T__10)
                pass
            elif token in [33]:
                localctx = MiniBParser.IsNanFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.match(MiniBParser.ISNAN)
                self.state = 218
                self.match(MiniBParser.T__9)
                self.state = 219
                self.expression(0)
                self.state = 220
                self.match(MiniBParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.condition_sempred
        self._predicates[15] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         




