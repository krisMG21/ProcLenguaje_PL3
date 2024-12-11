import sys
from antlr4 import ParseTreeVisitor
from MiniBParser import MiniBParser
from SymbolTable import SymbolTable


class Visitor(ParseTreeVisitor):
    def __init__(self):
        self.instructions = []
        self.label_count = 0
        self.stack_limit = 100
        self.local_limit = 100
        self.tabla = SymbolTable()
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
        """
        Agrega una instrucción a la lista de instrucciones.
        Estas se agregan al archivo final entre header y footer.
        """
        self.instructions.append(f"    {instruction}")

    def visitProgram(self, ctx: MiniBParser.ProgramContext):
        """
        Regla raíz, simplemente visita cada instrucción (teoricamente)
        (Probar)
        """
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.get_jasmin_code()

    def visitLet(self, ctx: MiniBParser.LetContext):
        """
        Declara una variable, le asigna un valor, y la almacena
        en la siguiente posición de locals.

        Guardamos dicha posición en la tabla de simbolos.
        """
        # print("En let: ", ctx.ID().getText())
        var_name = ctx.ID().getText()
        var_index = self.tabla.add(var_name)
        self.visit(ctx.exp)
        self.add_instruction(f"istore {var_index}")

    def visitOp(self, ctx: MiniBParser.OpContext):
        """
        Asigna un valor a una variable, y la almacena
        en su posición de locals.
        """
        # print("En op: ", ctx.ID().getText())
        var_name = ctx.ID().getText()
        var_index = self.tabla.get(var_name)
        self.visit(ctx.exp)
        self.add_instruction(f"istore {var_index}")

    def visitPrint(self, ctx: MiniBParser.PrintContext):
        """
        Imprime resultado de una expresión
        (lo que se encuentre en la cima del stack)
        """
        self.add_instruction("getstatic java/lang/System/out Ljava/io/PrintStream;")

        value = self.visit(ctx.exp)
        print_type = ""

        match value:
            case int():
                print_type = "I"
            case str():
                print_type = "Ljava/lang/String;"
            case bool():
                print_type = "Z"
            case float():
                print_type = "F"
            case list():
                print_type = "Ljava/util/List;"
            case dict():
                print_type = "Ljava/util/Map;"
            case None:
                print_type = "V"

        self.add_instruction(
            f"invokevirtual java/io/PrintStream/println({print_type})V"
        )

    def visitInput(self, ctx: MiniBParser.InputContext):
        """
        Alamcena una string en una variable
        """
        string = ctx.STRING_LITERAL().getText()
        var_name = ctx.ID().getText()
        var_index = self.tabla.add(var_name)
        self.add_instruction(f"ldc {string}")
        self.add_instruction(f"istore {var_index}")

    def visitIf(self, ctx: MiniBParser.IfContext):
        else_label = f"ELSE_{self.label_count}"
        end_label = f"ENDIF_{self.label_count}"
        self.label_count += 1

        self.visit(ctx.cond)
        self.add_instruction(f"ifeq {else_label}")

        for stmt in ctx.statif():
            self.visit(stmt)

        self.add_instruction(f"goto {end_label}")
        self.add_instruction(f"{else_label}:")

        if ctx.statelse:
            for stmt in ctx.statelse():
                self.visit(stmt)

        self.add_instruction(f"{end_label}:")

    def visitFor(self, ctx: MiniBParser.ForContext):
        var_index = self.tabla.get(ctx.ID().getText())
        start_label = f"FOR_START_{self.label_count}"
        end_label = f"FOR_END_{self.label_count}"
        self.label_count += 1

        self.visit(ctx.exp1)
        self.add_instruction(f"istore {var_index}")

        self.add_instruction(f"{start_label}:")
        self.add_instruction(f"iload {var_index}")
        self.visit(ctx.exp2)
        self.add_instruction(f"if_icmpgt {end_label}")

        for stmt in ctx.stat():
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

        for stmt in ctx.stat():
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
        num_text = ctx.NUMBER().getText().lower()
        base = 10
        if num_text.startswith('0x'):
            base = 16
            num_text = num_text[2:]
        elif num_text.startswith('0b'):
            base = 2
            num_text = num_text[2:]
        elif num_text.startswith('0o'):
            base = 8
            num_text = num_text[2:]
    
        if '.' in num_text:
            integer_part, fractional_part = num_text.split('.')
            integer_value = int(integer_part, base) if integer_part else 0
            fractional_value = 0.0
            for i, digit in enumerate(fractional_part):
                fractional_value += int(digit, base) * (base ** -(i + 1))
            value = integer_value + fractional_value
            self.add_instruction(f"ldc {value}")
        else:
            if base != 10:
                value = int(num_text, base)
                self.add_instruction(f"ldc {value}")
            else:
                value = float(num_text) if '.' in num_text else int(num_text)
                self.add_instruction(f"ldc {value}")

    def visitStringExpression(self, ctx: MiniBParser.StringExpressionContext):
        """
        Carga una cadena en la cima del stack.
        """
        self.add_instruction(f"ldc {ctx.STRING_LITERAL().getText()}")

    def visitIdExpression(self, ctx: MiniBParser.IdExpressionContext):
        """
        Carga el valor de la variable en la cima del stack.
        """
        var_name = ctx.ID().getText()
        var_index = self.tabla.get(var_name)
        self.add_instruction(f"iload {var_index}")
        return

    def visitFunctionCallExpression(
        self, ctx: MiniBParser.FunctionCallExpressionContext
    ):
        self.visit(ctx.fun)

    def visitValFunction(self, ctx: MiniBParser.ValFunctionContext):
        self.visit(ctx.expression())
        # VAL function is treated as identity function in this simplified version

    def visitLenFunction(self, ctx: MiniBParser.LenFunctionContext):
        """
        Calcula la longitud de un valor dado
        """
        value = self.visit(ctx.expression())

        # Get length of the value
        self.add_instruction("invokestatic java/lang/String.length()I")
        return len(value)

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
