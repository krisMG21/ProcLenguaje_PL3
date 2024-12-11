# Generated from MiniB.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .MiniBParser import MiniBParser
else:
    from MiniBParser import MiniBParser

# This class defines a complete generic visitor for a parse tree produced by MiniBParser.


class MiniBVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by MiniBParser#program.
    def visitProgram(self, ctx: MiniBParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#statement.
    def visitStatement(self, ctx: MiniBParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#Let.
    def visitLet(self, ctx: MiniBParser.LetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#Op.
    def visitOp(self, ctx: MiniBParser.OpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#Print.
    def visitPrint(self, ctx: MiniBParser.PrintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#Input.
    def visitInput(self, ctx: MiniBParser.InputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#If.
    def visitIf(self, ctx: MiniBParser.IfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#For.
    def visitFor(self, ctx: MiniBParser.ForContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#While.
    def visitWhile(self, ctx: MiniBParser.WhileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#Repeat.
    def visitRepeat(self, ctx: MiniBParser.RepeatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#Continue.
    def visitContinue(self, ctx: MiniBParser.ContinueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#Exit.
    def visitExit(self, ctx: MiniBParser.ExitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#logicalOp.
    def visitLogicalOp(self, ctx: MiniBParser.LogicalOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#comparisonOp.
    def visitComparisonOp(self, ctx: MiniBParser.ComparisonOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#arithmeticOp.
    def visitArithmeticOp(self, ctx: MiniBParser.ArithmeticOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#condition.
    def visitCondition(self, ctx: MiniBParser.ConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#StringExpression.
    def visitStringExpression(self, ctx: MiniBParser.StringExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#IdExpression.
    def visitIdExpression(self, ctx: MiniBParser.IdExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#ParenExpression.
    def visitParenExpression(self, ctx: MiniBParser.ParenExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#NumberExpression.
    def visitNumberExpression(self, ctx: MiniBParser.NumberExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#ArithmeticExpression.
    def visitArithmeticExpression(self, ctx: MiniBParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#FunctionCallExpression.
    def visitFunctionCallExpression(
        self, ctx: MiniBParser.FunctionCallExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#ValFunction.
    def visitValFunction(self, ctx: MiniBParser.ValFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#LenFunction.
    def visitLenFunction(self, ctx: MiniBParser.LenFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniBParser#IsNanFunction.
    def visitIsNanFunction(self, ctx: MiniBParser.IsNanFunctionContext):
        return self.visitChildren(ctx)


del MiniBParser
