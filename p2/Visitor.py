from antlr4 import *
from MiniBParser import MiniBParser
from SymbolTable import SymbolTable


class Visitor(ParseTreeVisitor):
    def __init__(self):
        self.instructions = []
        self.label_count = 0
        self.stack_limit = 100
        self.local_limit = 100
        self.symbol_table = SymbolTable()
        self.current_var = 0

    def get_jasmin_code(self):
        header = f""".class public MiniB
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack {self.stack_limit}
    .limit locals {self.local_limit}
"""
        footer = """
    return
.end method
"""
        return header + "\n".join(self.instructions) + footer

    def add_instruction(self, instruction):
        self.instructions.append(f"    {instruction}")

    def get_variable(self, name):
        if name not in self.symbol_table.symbols:
            index = self.current_var
            self.symbol_table.add(name, index)
            self.current_var += 1
        else:
            index = self.symbol_table.get(name)
        return index

    def visitProgram(self, ctx: MiniBParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.get_jasmin_code()

    def visitLet(self, ctx: MiniBParser.LetContext):
        print("En let: ", ctx.ID().getText())
        var_name = ctx.ID().getText()
        self.visit(ctx.exp)
        var_index = self.get_variable(var_name)
        self.add_instruction(f"istore {var_index}")

    def visitOp(self, ctx: MiniBParser.OpContext):
        var_name = ctx.id.text
        self.visit(ctx.exp)
        var_index = self.get_variable(var_name)
        self.add_instruction(f"istore {var_index}")

    def visitPrint(self, ctx: MiniBParser.PrintContext):
        self.add_instruction("getstatic java/lang/System/out Ljava/io/PrintStream;")
        self.visit(ctx.exp)
        self.add_instruction("invokevirtual java/io/PrintStream/println(I)V")

    def visitInput(self, ctx: MiniBParser.InputContext):
        # Simplified input: just push 0 onto the stack
        self.add_instruction("ldc 0")
        var_index = self.get_variable(ctx.id.text)
        self.add_instruction(f"istore {var_index}")

    def visitIf(self, ctx: MiniBParser.IfContext):
        else_label = f"ELSE_{self.label_count}"
        end_label = f"ENDIF_{self.label_count}"
        self.label_count += 1

        self.visit(ctx.cond)
        self.add_instruction(f"ifeq {else_label}")

        for stmt in ctx.statif:
            self.visit(stmt)

        self.add_instruction(f"goto {end_label}")
        self.add_instruction(f"{else_label}:")

        if ctx.statelse:
            for stmt in ctx.statelse:
                self.visit(stmt)

        self.add_instruction(f"{end_label}:")

    def visitFor(self, ctx: MiniBParser.ForContext):
        var_index = self.get_variable(ctx.id.text)
        start_label = f"FOR_START_{self.label_count}"
        end_label = f"FOR_END_{self.label_count}"
        self.label_count += 1

        self.visit(ctx.exp1)
        self.add_instruction(f"istore {var_index}")

        self.add_instruction(f"{start_label}:")
        self.add_instruction(f"iload {var_index}")
        self.visit(ctx.exp2)
        self.add_instruction(f"if_icmpgt {end_label}")

        for stmt in ctx.stat:
            self.visit(stmt)

        self.add_instruction(f"iinc {var_index} 1")
        self.add_instruction(f"goto {start_label}")
        self.add_instruction(f"{end_label}:")

    def visitWhile(self, ctx: MiniBParser.WhileContext):
        start_label = f"WHILE_START_{self.label_count}"
        end_label = f"WHILE_END_{self.label_count}"
        self.label_count += 1

        self.add_instruction(f"{start_label}:")
        self.visit(ctx.cond)
        self.add_instruction(f"ifeq {end_label}")

        for stmt in ctx.statement():
            self.visit(stmt)

        self.add_instruction(f"goto {start_label}")
        self.add_instruction(f"{end_label}:")

    def visitRepeat(self, ctx: MiniBParser.RepeatContext):
        start_label = f"REPEAT_START_{self.label_count}"
        self.label_count += 1

        self.add_instruction(f"{start_label}:")

        for stmt in ctx.stat:
            self.visit(stmt)

        self.visit(ctx.cond)
        self.add_instruction(f"ifeq {start_label}")

    def visitContinue(self, ctx: MiniBParser.ContinueContext):
        # This is a simplified version, actual implementation depends on loop context
        self.add_instruction("goto CONTINUE")

    def visitExit(self, ctx: MiniBParser.ExitContext):
        self.add_instruction("return")

    def visitCondition(self, ctx: MiniBParser.ConditionContext):
        if ctx.NOT():
            self.visit(ctx.condition())
            self.add_instruction("iconst_1")
            self.add_instruction("ixor")
        elif ctx.logicalOp():
            self.visit(ctx.condition(0))
            self.visit(ctx.condition(1))
            op = ctx.logicalOp().getText().lower()
            if op == "and":
                self.add_instruction("iand")
            elif op == "or":
                self.add_instruction("ior")
        elif ctx.comparisonOp():
            self.visit(ctx.expression(0))
            self.visit(ctx.expression(1))
            op = ctx.comparisonOp().getText()
            if op == "<":
                self.add_instruction("if_icmplt")
            elif op == ">":
                self.add_instruction("if_icmpgt")
            elif op == "<=":
                self.add_instruction("if_icmple")
            elif op == ">=":
                self.add_instruction("if_icmpge")
            elif op == "=":
                self.add_instruction("if_icmpeq")
        else:
            self.visit(ctx.expression(0))

    def visitArithmeticExpression(self, ctx: MiniBParser.ArithmeticExpressionContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        op = ctx.arithmeticOp().getText()
        if op == "+":
            self.add_instruction("iadd")
        elif op == "-":
            self.add_instruction("isub")
        elif op == "*":
            self.add_instruction("imul")
        elif op == "/":
            self.add_instruction("idiv")
        elif op == "%":
            self.add_instruction("irem")

    def visitParenExpression(self, ctx: MiniBParser.ParenExpressionContext):
        self.visit(ctx.expression())

    def visitNumberExpression(self, ctx: MiniBParser.NumberExpressionContext):
        self.add_instruction(f"ldc {ctx.NUMBER().getText()}")

    def visitStringExpression(self, ctx: MiniBParser.StringExpressionContext):
        # Simplified: treat strings as their length
        self.add_instruction(
            f"ldc {len(ctx.STRING_LITERAL().getText()) - 2}"
        )  # -2 for quotes

    def visitIdExpression(self, ctx: MiniBParser.IdExpressionContext):
        var_name = ctx.id.text
        var_index = self.get_variable(var_name)
        self.add_instruction(f"iload {var_index}")

    def visitFunctionCallExpression(
        self, ctx: MiniBParser.FunctionCallExpressionContext
    ):
        self.visit(ctx.fun)

    def visitValFunction(self, ctx: MiniBParser.ValFunctionContext):
        self.visit(ctx.expression())
        # VAL function is treated as identity function in this simplified version

    def visitLenFunction(self, ctx: MiniBParser.LenFunctionContext):
        # Simplified: LEN function returns 1 for all inputs
        self.add_instruction("ldc 1")

    def visitIsNanFunction(self, ctx: MiniBParser.IsNanFunctionContext):
        # Simplified: ISNAN function always returns false (0)
        self.add_instruction("ldc 0")


# Usage:
# lexer = MiniBLexer(input_stream)
# token_stream = CommonTokenStream(lexer)
# parser = MiniBParser(token_stream)
# tree = parser.program()
# visitor = JasminVisitor()
# jasmin_code = visitor.visit(tree)
# print(jasmin_code)
