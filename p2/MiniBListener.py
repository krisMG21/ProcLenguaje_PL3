# Generated from MiniB.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniBParser import MiniBParser
else:
    from MiniBParser import MiniBParser

# This class defines a complete listener for a parse tree produced by MiniBParser.
class MiniBListener(ParseTreeListener):

    # Enter a parse tree produced by MiniBParser#program.
    def enterProgram(self, ctx:MiniBParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniBParser#program.
    def exitProgram(self, ctx:MiniBParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniBParser#statement.
    def enterStatement(self, ctx:MiniBParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniBParser#statement.
    def exitStatement(self, ctx:MiniBParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniBParser#Let.
    def enterLet(self, ctx:MiniBParser.LetContext):
        pass

    # Exit a parse tree produced by MiniBParser#Let.
    def exitLet(self, ctx:MiniBParser.LetContext):
        pass


    # Enter a parse tree produced by MiniBParser#Op.
    def enterOp(self, ctx:MiniBParser.OpContext):
        pass

    # Exit a parse tree produced by MiniBParser#Op.
    def exitOp(self, ctx:MiniBParser.OpContext):
        pass


    # Enter a parse tree produced by MiniBParser#Print.
    def enterPrint(self, ctx:MiniBParser.PrintContext):
        pass

    # Exit a parse tree produced by MiniBParser#Print.
    def exitPrint(self, ctx:MiniBParser.PrintContext):
        pass


    # Enter a parse tree produced by MiniBParser#Input.
    def enterInput(self, ctx:MiniBParser.InputContext):
        pass

    # Exit a parse tree produced by MiniBParser#Input.
    def exitInput(self, ctx:MiniBParser.InputContext):
        pass


    # Enter a parse tree produced by MiniBParser#If.
    def enterIf(self, ctx:MiniBParser.IfContext):
        pass

    # Exit a parse tree produced by MiniBParser#If.
    def exitIf(self, ctx:MiniBParser.IfContext):
        pass


    # Enter a parse tree produced by MiniBParser#For.
    def enterFor(self, ctx:MiniBParser.ForContext):
        pass

    # Exit a parse tree produced by MiniBParser#For.
    def exitFor(self, ctx:MiniBParser.ForContext):
        pass


    # Enter a parse tree produced by MiniBParser#While.
    def enterWhile(self, ctx:MiniBParser.WhileContext):
        pass

    # Exit a parse tree produced by MiniBParser#While.
    def exitWhile(self, ctx:MiniBParser.WhileContext):
        pass


    # Enter a parse tree produced by MiniBParser#Repeat.
    def enterRepeat(self, ctx:MiniBParser.RepeatContext):
        pass

    # Exit a parse tree produced by MiniBParser#Repeat.
    def exitRepeat(self, ctx:MiniBParser.RepeatContext):
        pass


    # Enter a parse tree produced by MiniBParser#Continue.
    def enterContinue(self, ctx:MiniBParser.ContinueContext):
        pass

    # Exit a parse tree produced by MiniBParser#Continue.
    def exitContinue(self, ctx:MiniBParser.ContinueContext):
        pass


    # Enter a parse tree produced by MiniBParser#Exit.
    def enterExit(self, ctx:MiniBParser.ExitContext):
        pass

    # Exit a parse tree produced by MiniBParser#Exit.
    def exitExit(self, ctx:MiniBParser.ExitContext):
        pass


    # Enter a parse tree produced by MiniBParser#logicalOp.
    def enterLogicalOp(self, ctx:MiniBParser.LogicalOpContext):
        pass

    # Exit a parse tree produced by MiniBParser#logicalOp.
    def exitLogicalOp(self, ctx:MiniBParser.LogicalOpContext):
        pass


    # Enter a parse tree produced by MiniBParser#comparisonOp.
    def enterComparisonOp(self, ctx:MiniBParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by MiniBParser#comparisonOp.
    def exitComparisonOp(self, ctx:MiniBParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by MiniBParser#arithmeticOp.
    def enterArithmeticOp(self, ctx:MiniBParser.ArithmeticOpContext):
        pass

    # Exit a parse tree produced by MiniBParser#arithmeticOp.
    def exitArithmeticOp(self, ctx:MiniBParser.ArithmeticOpContext):
        pass


    # Enter a parse tree produced by MiniBParser#Not.
    def enterNot(self, ctx:MiniBParser.NotContext):
        pass

    # Exit a parse tree produced by MiniBParser#Not.
    def exitNot(self, ctx:MiniBParser.NotContext):
        pass


    # Enter a parse tree produced by MiniBParser#condExp.
    def enterCondExp(self, ctx:MiniBParser.CondExpContext):
        pass

    # Exit a parse tree produced by MiniBParser#condExp.
    def exitCondExp(self, ctx:MiniBParser.CondExpContext):
        pass


    # Enter a parse tree produced by MiniBParser#Comparison.
    def enterComparison(self, ctx:MiniBParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MiniBParser#Comparison.
    def exitComparison(self, ctx:MiniBParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MiniBParser#Logical.
    def enterLogical(self, ctx:MiniBParser.LogicalContext):
        pass

    # Exit a parse tree produced by MiniBParser#Logical.
    def exitLogical(self, ctx:MiniBParser.LogicalContext):
        pass


    # Enter a parse tree produced by MiniBParser#StringExpression.
    def enterStringExpression(self, ctx:MiniBParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by MiniBParser#StringExpression.
    def exitStringExpression(self, ctx:MiniBParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by MiniBParser#IdExpression.
    def enterIdExpression(self, ctx:MiniBParser.IdExpressionContext):
        pass

    # Exit a parse tree produced by MiniBParser#IdExpression.
    def exitIdExpression(self, ctx:MiniBParser.IdExpressionContext):
        pass


    # Enter a parse tree produced by MiniBParser#ParenExpression.
    def enterParenExpression(self, ctx:MiniBParser.ParenExpressionContext):
        pass

    # Exit a parse tree produced by MiniBParser#ParenExpression.
    def exitParenExpression(self, ctx:MiniBParser.ParenExpressionContext):
        pass


    # Enter a parse tree produced by MiniBParser#NumberExpression.
    def enterNumberExpression(self, ctx:MiniBParser.NumberExpressionContext):
        pass

    # Exit a parse tree produced by MiniBParser#NumberExpression.
    def exitNumberExpression(self, ctx:MiniBParser.NumberExpressionContext):
        pass


    # Enter a parse tree produced by MiniBParser#ArithmeticExpression.
    def enterArithmeticExpression(self, ctx:MiniBParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by MiniBParser#ArithmeticExpression.
    def exitArithmeticExpression(self, ctx:MiniBParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by MiniBParser#FunctionCallExpression.
    def enterFunctionCallExpression(self, ctx:MiniBParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by MiniBParser#FunctionCallExpression.
    def exitFunctionCallExpression(self, ctx:MiniBParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by MiniBParser#ValFunction.
    def enterValFunction(self, ctx:MiniBParser.ValFunctionContext):
        pass

    # Exit a parse tree produced by MiniBParser#ValFunction.
    def exitValFunction(self, ctx:MiniBParser.ValFunctionContext):
        pass


    # Enter a parse tree produced by MiniBParser#LenFunction.
    def enterLenFunction(self, ctx:MiniBParser.LenFunctionContext):
        pass

    # Exit a parse tree produced by MiniBParser#LenFunction.
    def exitLenFunction(self, ctx:MiniBParser.LenFunctionContext):
        pass


    # Enter a parse tree produced by MiniBParser#IsNanFunction.
    def enterIsNanFunction(self, ctx:MiniBParser.IsNanFunctionContext):
        pass

    # Exit a parse tree produced by MiniBParser#IsNanFunction.
    def exitIsNanFunction(self, ctx:MiniBParser.IsNanFunctionContext):
        pass



del MiniBParser