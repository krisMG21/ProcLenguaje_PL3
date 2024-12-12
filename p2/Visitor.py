import sys
from antlr4 import ParseTreeVisitor
from MiniBParser import MiniBParser
from SymbolTable import SymbolTable


class Visitor(ParseTreeVisitor):
    def __init__(self):
        self.imports = []
        self.instructions = []
        self.instructions = []
        self.label_count = 0
        self.current_var = 0
        self.stack_limit = 100
        self.local_limit = 100
        self.tabla = SymbolTable()

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

    def add_import(self, import_):
        """
        Agrega una instrucción de importación a la lista de instrucciones.
        Estas se agregan al archivo final entre header y footer.
        """
        if import_ in self.imports:
            self.imports.append(import_)

    def add_instruction(self, instruction):
        """
        Agrega una instrucción a la lista de instrucciones.
        Estas se agregan al archivo final entre header y footer.
        """
        self.instructions.append(f"    {instruction}")

    def store_var(self, var_index, var_value):
        """
        Guarda un valor en la pila, con el tipo de dato adecuado.
        """
        match var_value:
            case str():
                self.add_instruction(f"astore_{var_index}")
            case int() | bool():
                self.add_instruction(f"istore_{var_index}")
            case float():
                self.add_instruction(f"fstore_{var_index}")

    def load_var(self, var_index: int, var_value):
        """
        Carga una variable en la pila.
        """
        match var_value:
            case str():
                self.add_instruction(f"aload_{var_index}")
            case int() | bool():
                self.add_instruction(f"iload_{var_index}")
            case float():
                self.add_instruction(f"fload_{var_index}")

    def concat(self, val0: str, val1: str):
        self.add_instruction("""
    new java/lang/StringBuilder
    dup
    invokespecial java/lang/StringBuilder/<init>()V
""")
        self.add_instruction(f"ldc {val0}")
        self.add_instruction(
            "invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;"
        )
        self.add_instruction(f"ldc {val1}")
        self.add_instruction(
            "invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;"
        )
        self.add_instruction(
            "invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;"
        )
        self.add_instruction("getstatic java/lang/System/out Ljava/io/PrintStream;")
        self.add_instruction("swap")
        return val0 + val1

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
        Declara una variable, le asigna el último valor en pila,
        cena en la siguiente posición de locals.

        Guardamos dicha posición en la tabla de simbolos.
        """
        var_name = ctx.ID().getText()
        var_value = self.visit(ctx.exp)

        var_index = self.tabla.add(var_name, var_value)

        self.store_var(var_index, var_value)

    def visitOp(self, ctx: MiniBParser.OpContext):
        """
        Asigna un valor a una variable, y la almacena
        en su posición de locals.
        """
        # print("En op: ", ctx.ID().getText())
        var_name = ctx.ID().getText()
        var_value = self.visit(ctx.exp)

        var_index = self.tabla.mod(var_name, var_value)
        self.store_var(var_index, var_value)

    def visitPrint(self, ctx: MiniBParser.PrintContext):
        """
        Imprime resultado de una expresión
        (lo que se encuentre en la cima del stack)
        """
        self.add_instruction("getstatic java/lang/System/out Ljava/io/PrintStream;")

        value = self.visit(ctx.exp)

        try:
            var_name = ctx.exp.ID().getText()
            var_index, _ = self.tabla.get(var_name)
            self.load_var(var_index, value)

        except AttributeError:
            pass

        printtype = ""

        match value:
            case int():
                printtype = "I"
            case float():
                printtype = "F"
            case str():
                printtype = "Ljava/lang/String;"
            case bool():
                printtype = "Z"
            case list():
                printtype = "Ljava/util/List;"
        self.add_instruction(f"invokevirtual java/io/PrintStream/println({printtype})V")

    def visitInput(self, ctx: MiniBParser.InputContext):
        """
        Prints a prompt string, waits for user input, and stores the input in a variable
        """

        prompt = ctx.STRING_LITERAL().getText()
        var_name = ctx.ID().getText()
        var_index = self.tabla.add(var_name, "")

        print(f"{self.tabla}")

        # Print the prompt
        self.add_instruction("getstatic java/lang/System/out Ljava/io/PrintStream;")
        self.add_instruction(f"ldc {prompt}")
        self.add_instruction(
            "invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V"
        )

        # Create a Scanner object for reading input
        self.add_instruction("new java/util/Scanner")
        self.add_instruction("dup")
        self.add_instruction("getstatic java/lang/System/in Ljava/io/InputStream;")
        self.add_instruction(
            "invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V"
        )

        # Read a line of input
        self.add_instruction(
            "invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;"
        )
        # Store the input in the variable
        self.add_instruction(f"astore_{var_index}")

    def visitIf(self, ctx: MiniBParser.IfContext):
        # Crea las labels
        else_label = f"ELSE_{self.label_count}"
        end_label = f"ENDIF_{self.label_count}"
        self.label_count += 1

        cond = self.visit(ctx.cond)

        if cond is None:
            self.add_instruction(f"ifeq {else_label}")
        else:
            self.add_instruction(f"{cond} {else_label}")

        for stmt in ctx.statif.getChildren():
            self.visit(stmt)

        self.add_instruction(f"goto {end_label}")
        self.add_instruction(f"{else_label}:")

        if ctx.statelse:
            for stmt in ctx.statelse.getChildren():
                self.visit(stmt)

        self.add_instruction(f"{end_label}:")

    def visitFor(self, ctx: MiniBParser.ForContext):
        var_index = self.tabla.add(ctx.ID().getText(), "")
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

    def visitComparison(self, ctx: MiniBParser.ComparisonContext):
        print("En comparison")
        self.visit(ctx.left)  # Carga el lado izquierdo de la comparación en la pila
        self.visit(ctx.right)  # Carga el lado derecho de la comparación en la pila

        op = ctx.op.getText()  # Operador de comparación
        comp = ""  # Instrucción de comparación"

        # Se asigna el comparador contrario porque saltamos
        # al else si es correcto
        if op == "<":
            comp = "if_icmpge"
        elif op == ">":
            comp = "if_icmple"
        elif op == "<=":
            comp = "if_icmpgt"
        elif op == ">=":
            comp = "if_icmplt"
        elif op == "==":
            comp = "if_icmpne"
        elif op == "!=":
            comp = "if_icmpeq"

        return comp

    def visitNot(self, ctx: MiniBParser.NotContext):
        print("En not")
        self.visit(ctx.cond)  # Visita la condición
        self.add_instruction("iconst_1")  # Carga el valor 1 (verdadero)
        self.add_instruction("ixor")  # Realiza XOR para invertir el booleano

    def visitLogical(self, ctx: MiniBParser.LogicalContext):
        print("En logical")
        self.visit(ctx.left)  # Lado izquierdo
        self.visit(ctx.right)  # Lado derecho

        op = ctx.op.getText().lower()  # Operador lógico (AND/OR)
        if op == "and":
            self.add_instruction("iand")  # AND lógico
        elif op == "or":
            self.add_instruction("ior")  # OR lógico

    def visitCondExp(self, ctx: MiniBParser.CondExpContext):
        self.visit(ctx.expr)

    def visitArithmeticExpression(self, ctx: MiniBParser.ArithmeticExpressionContext):
        val0 = self.visit(ctx.expression(0))
        val1 = self.visit(ctx.expression(1))

        # Tratamiento de nulos
        val0 = 0 if val0 is None else val0
        val1 = 0 if val1 is None else val1

        # Contagio de tipo
        if isinstance(val1, float) and isinstance(val0, int):
            val0 = float(val0)
        elif isinstance(val0, float) and isinstance(val1, int):
            val1 = float(val1)
        elif isinstance(val0, str) or isinstance(val1, str):
            val0, val1 = str(val0), str(val1)
            val0 = '"' + val0 + '"' if not val0.startswith('"') else val0
            val1 = '"' + val1 + '"' if not val1.startswith('"') else val1

        if type(val0) is str and type(val1) is str:
            val0 = self.concat(val0, val1)
            return val0

        self.add_instruction(f"ldc {val0}")
        self.add_instruction(f"ldc {val1}")

        op = self.visit(ctx.op)
        instr = ""

        match val0:
            case int() | bool():
                val0 = int(val0)
                instr = "i"
            case float():
                instr = "f"
            case str():
                instr = "a"

        match op:
            case "+":
                instr += "add"
            case "-":
                instr += "sub"
            case "*":
                instr += "mul"
            case "/":
                instr += "div"
            case "%":
                instr += "rem"

        self.add_instruction(instr)

        return val0

    def visitPlusOperation(self, ctx: MiniBParser.PlusOperationContext):
        return "+"

    # Visit a parse tree produced by MiniBParser#MinusOperation.
    def visitMinusOperation(self, ctx: MiniBParser.MinusOperationContext):
        return "-"

    # Visit a parse tree produced by MiniBParser#MulOperation.
    def visitMulOperation(self, ctx: MiniBParser.MulOperationContext):
        return "*"

    # Visit a parse tree produced by MiniBParser#DivOperation.
    def visitDivOperation(self, ctx: MiniBParser.DivOperationContext):
        return "/"

    # Visit a parse tree produced by MiniBParser#ModOperation.
    def visitModOperation(self, ctx: MiniBParser.ModOperationContext):
        return "%"

    def visitParenExpression(self, ctx: MiniBParser.ParenExpressionContext):
        self.visit(ctx.expression())

    def visitNumberExpression(self, ctx: MiniBParser.NumberExpressionContext):
        # WARNING: Revisar
        num_text = ctx.NUMBER().getText().lower()
        base = 10
        if num_text.startswith("0x"):
            base = 16
            num_text = num_text[2:]
        elif num_text.startswith("0b"):
            base = 2
            num_text = num_text[2:]
        elif num_text.startswith("0o"):
            base = 8
            num_text = num_text[2:]

        if "." in num_text:
            integer_part, fractional_part = num_text.split(".")
            integer_value = int(integer_part, base) if integer_part else 0
            fractional_value = 0.0
            for i, digit in enumerate(fractional_part):
                fractional_value += int(digit, base) * (base ** -(i + 1))
            value = integer_value + fractional_value
            return value
        else:
            if base != 10:
                value = int(num_text, base)
                return value
            else:
                value = float(num_text) if "." in num_text else int(num_text)
                return value

    def visitStringExpression(self, ctx: MiniBParser.StringExpressionContext):
        """
        Carga una cadena en la cima del stack.
        """
        value = f"{ctx.STRING_LITERAL().getText()}"
        self.add_instruction(f"ldc {value}")
        return value  # Borrar las comillas de " "

    def visitIdExpression(self, ctx: MiniBParser.IdExpressionContext):
        """
        Carga el valor de la variable en la cima del stack.
        """
        var_name = ctx.ID().getText()
        var_index, var_value = self.tabla.get(var_name)

        return var_value

    def visitFunctionCallExpression(
        self, ctx: MiniBParser.FunctionCallExpressionContext
    ):
        return self.visit(ctx.fun)

    def visitValFunction(self, ctx: MiniBParser.ValFunctionContext):
        value = self.visit(ctx.expression())
        try:
            value = int(value)
        except:
            value = None
            print("En VAL() no se ha podido convertir el valor")
        return value
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
        return 0
