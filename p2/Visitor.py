import sys
from funciones import VAL, LEN, ISNAN
from antlr4 import ParseTreeVisitor
from MiniBParser import MiniBParser
from SymbolTable import SymbolTable


class Visitor(ParseTreeVisitor):
    def __init__(self):
        self.imports = []
        self.functions = []
        self.instructions = []
        self.instructions = []
        self.index_for = []

        self.label_count = 0
        self.current_var = 0

        self.stack_limit = 100
        self.local_limit = 100

        self.tabla = SymbolTable()
        self.error = False

    def get_jasmin_code(self):
        header = """.class public MiniB
.super java/lang/Object

"""
        main = f"""
.method public static main([Ljava/lang/String;)V
    .limit stack {self.stack_limit}
    .limit locals {self.local_limit}
"""
        footer = """
    return
.end method
"""
        return (
            header
            + "\n".join(self.functions)
            + main
            + "\n".join(self.imports)
            + "\n".join(self.instructions)
            + footer
        )

    def add_import(self, import_):
        """
        Agrega una instrucción de importación a la lista de instrucciones.
        Estas se agregan al archivo final entre header y footer.
        """
        self.imports.append(f"    {import_}")

    def def_function(self, function):
        """
        Define una función a la lista de funciones.
        Estas se agregan al archivo final entre header y footer.
        """
        if function in self.functions:
            name = function[21:].split(":")[0]
            print(f"WARNING: La función {name}... ya esta definida")
        else:
            self.functions.append(function)

    def add_function(self, function):
        """
        Agrega una función a la lista de funciones.
            Estas se agregan al archivo final entre header y footer.
        """
        if function not in self.functions:
            self.functions.append(function)

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
            case str() | None:
                self.add_instruction(f"astore_{var_index}")
            case int() | bool():
                self.add_instruction(f"istore_{var_index}")
            case float():
                self.add_instruction(f"fstore_{var_index}")

    def load_var(self, var_index: int, var_value):
        """
        Carga una variable en la pila con el tipo adecuado.
        """
        match var_value:
            case str() | None:
                self.add_instruction(f"aload_{var_index}")
            case int() | bool():
                self.add_instruction(f"iload_{var_index}")
            case float():
                self.add_instruction(f"fload_{var_index}")

    def concat(self, val0: str, val1: str):
        # En vez de triple comillas, añadir cada instrucción por separado
        self.add_instruction("new java/lang/StringBuilder")
        self.add_instruction("dup")
        self.add_instruction("invokespecial java/lang/StringBuilder/<init>()V")
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
        return val0 + val1

    def try_ID(self, exp, var_value, load=True):
        try:
            var_name = exp.ID().getText()
            var_index, _ = self.tabla.get(var_name)
            self.load_var(var_index, var_value)
        except AttributeError:
            if load:
                if (
                    isinstance(var_value, str)
                    and '"' not in var_value[1:-1]
                    or not isinstance(var_value, str)
                ):
                    self.add_instruction(f"ldc {var_value}")

    def visitProgram(self, ctx: MiniBParser.ProgramContext):
        """
        Regla raíz, simplemente visita cada instrucción (teoricamente)
        (Probar)
        """
        for stmt in ctx.statement():
            self.visit(stmt)

        self.error = self.error or self.tabla.error

        return self.get_jasmin_code()

    def visitLet(self, ctx: MiniBParser.LetContext):
        """
        Declara una variable, le asigna el último valor en pila,
        cena en la siguiente posición de locals.

        Guardamos dicha posición en la tabla de simbolos.
        """
        var_name = ctx.ID().getText()
        var_value = self.visit(ctx.exp)

        self.try_ID(ctx.exp, var_value)

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

        is_op = False
        try:
            is_op = bool(ctx.exp.op or ctx.exp.fun)
        except Exception:
            pass

        self.try_ID(ctx.exp, var_value, not is_op)
        self.store_var(var_index, var_value)

    def visitPrint(self, ctx: MiniBParser.PrintContext):
        """
        Imprime resultado de una expresión
        """
        self.add_instruction("getstatic java/lang/System/out Ljava/io/PrintStream;")

        value = self.visit(ctx.exp)

        # Verifica si la expresión es un acceso a array
        if isinstance(ctx.exp, MiniBParser.ArrayAccessExpressionContext):
            # Como es un acceso a array y usamos iaload, en la pila hay un int
            # No llamamos a try_ID, y asignamos printtype directamente
            printtype = "I"
        else:
            # Caso normal
            is_op = False
            try:
                is_op = bool(ctx.exp.op)
            except Exception:
                try:
                    is_op = bool(ctx.exp.fun)
                except Exception:
                    pass

            self.try_ID(ctx.exp, value, not is_op)

            # Asignar printtype según el valor
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
                case _:
                    # Por si acaso, un valor por defecto
                    printtype = "Ljava/lang/Object;"

        self.add_instruction(f"invokevirtual java/io/PrintStream/println({printtype})V")

    def visitInput(self, ctx: MiniBParser.InputContext):
        """
        Prints a prompt string, waits for user input, and stores the input in a variable
        """

        prompt = ctx.STRING_LITERAL().getText()
        var_name = ctx.ID().getText()
        var_index = self.tabla.add(var_name, "")

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

        self.start_label = else_label
        self.end_label = end_label
        self.label_count += 1

        cond = self.visit(ctx.cond)

        try:
            exp = self.try_ID(ctx.cond.expr, 1)
        except AttributeError:
            pass

        if cond is None or cond == "":
            self.add_instruction(f"ifeq {else_label}")
        else:
            self.add_instruction(f"{cond} {else_label}")

        for stmt in ctx.statif.getChildren():
            self.visit(stmt)

        self.add_instruction(f"goto {end_label}")  # Salta al final
        self.add_instruction(f"{else_label}:")

        if ctx.statelse:
            for stmt in ctx.statelse.getChildren():
                self.visit(stmt)

        self.add_instruction(f"{end_label}:")

    def visitFor(self, ctx: MiniBParser.ForContext):
        self.index_for.append(self.label_count)
        start_label = f"FOR_START_{self.label_count}"
        continue_label = f"FOR_CONTINUE_{self.label_count}"
        end_label = f"FOR_END_{self.label_count}"
        self.label_count += 1

        var_name = ctx.ID().getText()
        var_value = self.visit(ctx.exp1)
        self.add_instruction(f"ldc {var_value}")

        var_index = self.tabla.add(var_name, var_value)
        self.add_instruction(f"ldc {var_value}")
        self.store_var(var_index, var_value)

        self.add_instruction(f"{start_label}:")

        self.add_instruction(f"iload_{var_index}")
        var2_value = self.visit(ctx.exp2)
        self.add_instruction(f"ldc {var2_value}")
        self.add_instruction(f"if_icmpgt {end_label}")

        for stmt in ctx.statement():
            self.visit(stmt)

        self.add_instruction(f"{continue_label}:")
        self.add_instruction(f"iinc {var_index} 1")
        self.add_instruction(f"goto {start_label}")
        self.add_instruction(f"{end_label}:")
        self.index_for.pop()

    def visitWhile(self, ctx: MiniBParser.WhileContext):
        start_label = f"WHILE_START_{self.label_count}"
        end_label = f"WHILE_END_{self.label_count}"
        self.label_count += 1

        self.add_instruction(f"{start_label}:")
        cond = self.visit(ctx.cond)

        if cond is None or cond == "":
            self.add_instruction(f"ifeq {end_label}")
        else:
            self.add_instruction(f"{cond} {end_label}")

        for stmt in ctx.statement():
            self.visit(stmt)

        self.add_instruction(f"goto {start_label}")
        self.add_instruction(f"{end_label}:")

    def visitRepeat(self, ctx: MiniBParser.RepeatContext):
        start_label = f"REPEAT_START_{self.label_count}"
        end_label = f"REPEAT_END_{self.label_count}"
        self.label_count += 1

        self.add_instruction(f"{start_label}:")

        for stmt in ctx.statement():
            self.visit(stmt)

        cond = self.visit(ctx.cond)
        if cond is None or cond == "":
            self.add_instruction(f"ifeq {start_label}")
        else:
            self.add_instruction(f"{cond} {start_label}")

    def visitContinue(self, ctx: MiniBParser.ContinueContext):
        # This is a simplified version, actual implementation depends on loop context
        self.add_instruction(f"goto FOR_CONTINUE_{self.index_for[-1]}")

    def visitExit(self, ctx: MiniBParser.ExitContext):
        self.add_instruction(f"goto FOR_END_{self.index_for[-1]}")

    def visitComparison(self, ctx: MiniBParser.ComparisonContext):
        print("En comparison")
        val0 = self.visit(
            ctx.left
        )  # Carga el lado izquierdo de la comparación en la pila
        val1 = self.visit(
            ctx.right
        )  # Carga el lado derecho de la comparación en la pila

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
        elif op == "=":
            comp = "if_icmpne"
        elif op == "!=":
            comp = "if_icmpeq"

        self.try_ID(ctx.left, val0)
        self.try_ID(ctx.right, val1)

        return comp

    def visitNot(self, ctx: MiniBParser.NotContext):
        self.visit(ctx.cond)  # Visita la condición
        self.add_instruction("iconst_1")  # Carga el valor 1 (verdadero)
        self.add_instruction("ixor")  # Realiza XOR para invertir el booleano

    def visitLogical(self, ctx: MiniBParser.LogicalContext):
        self.visit(ctx.left)  # Lado izquierdo
        self.visit(ctx.right)  # Lado derecho

        op = ctx.op.getText().lower()  # Operador lógico (AND/OR)
        if op == "and":
            self.add_instruction("iand")  # AND lógico
        elif op == "or":
            self.add_instruction("ior")  # OR lógico

    def visitCondExp(self, ctx: MiniBParser.CondExpContext):
        val = self.visit(ctx.expr)

        is_op = False
        try:
            is_op = bool(ctx.expr.op)
        except Exception:
            pass

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

        self.try_ID(ctx.left, val0)
        self.try_ID(ctx.right, val1)

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
        """
        Interpreta int y float, en bases 10, 16, 8 y 2.
        """
        num_text = ctx.NUMBER().getText().lower()
        base = 10
        prefixes = {"0x": 16, "0b": 2, "0o": 8}

        for prefix, b in prefixes.items():
            if num_text.startswith(prefix):
                base = b
                num_text = num_text[len(prefix) :]
                break

        if "." in num_text:
            integer_part, fractional_part = num_text.split(".")
            value = int(integer_part or "0", base)
            value += sum(
                int(d, base) * (base ** -(i + 1)) for i, d in enumerate(fractional_part)
            )
            value = float(value)
        else:
            value = int(num_text, base)

        return value

    def visitStringExpression(self, ctx: MiniBParser.StringExpressionContext):
        """
        Carga una cadena en la cima del stack.
        """
        value = f"{ctx.STRING_LITERAL().getText()}"
        # self.add_instruction(f"ldc {value}")
        return value

    def visitIdExpression(self, ctx: MiniBParser.IdExpressionContext):
        """
        Carga el valor de la variable en la cima del stack.
        """
        var_name = ctx.ID().getText()
        _, var_value = self.tabla.get(var_name)
        # print("en id", var_name, var_value)
        # self.load_var(var_index, var_value)
        return var_value

    def visitFunctionCallExpression(
        self, ctx: MiniBParser.FunctionCallExpressionContext
    ):
        fname = ctx.fun.getText()
        # Leer nombre de función y llamarla con MiniB/nombre
        # Leer los parámetros para cargarlos en la pila
        return self.visit(ctx.fun)

    def visitValFunction(self, ctx: MiniBParser.ValFunctionContext):
        value = self.visit(ctx.expr)

        self.add_function(VAL)

        self.try_ID(ctx.expr, value)
        self.add_instruction(
            "invokestatic MiniB/val(Ljava/lang/String;)Ljava/lang/Integer;"
        )

        try:
            value = int(value)
        except Exception:
            value = None
            # print("En VAL() no se ha podido convertir el valor")
        return value

    def visitLenFunction(self, ctx: MiniBParser.LenFunctionContext):
        """
        Calcula la longitud de un valor dado
        """
        value = self.visit(ctx.expr)

        self.add_function(LEN)

        self.try_ID(ctx.expr, value)
        self.add_instruction("invokestatic MiniB/len(Ljava/lang/String;)I")
        return len(value)

    def visitIsNanFunction(self, ctx: MiniBParser.IsNanFunctionContext):
        value = self.visit(ctx.expr)

        self.add_function(ISNAN)

        self.try_ID(ctx.expr, value)
        self.add_instruction("invokestatic MiniB/len(Ljava/lang/Object;)I")

        return 0

    def visitDim(self, ctx: MiniBParser.DimContext):
        """
        Define una variable de tipo array.
        Ejemplo:
        DIM numbers[3]

        Pasos:
        1. Calcular el tamaño del array visitando ctx.exp
        2. Crear el array con 'newarray int'
        3. Guardar en la tabla de símbolos y almacenar en locals con 'astore_x'
        """
        var_name = ctx.ID().getText()
        size = self.visit(ctx.exp)  # Calcula la dimensión

        # Cargar el tamaño en la pila
        self.add_instruction(f"ldc {size}")

        # Crear un array de enteros
        self.add_instruction("newarray int")

        # Añadir o modificar la variable en la tabla con el tamaño
        # Si la variable no existe, add; si ya existe (como un redim), mod.
        try:
            var_index, _ = self.tabla.get(var_name)
            # Si llega aquí, significa que la variable existe
            var_index = self.tabla.mod(var_name, size)
        except Exception:
            # Si lanza error es que no existe, entonces la creamos
            var_index = self.tabla.add(var_name, size)

        # Guardamos la referencia del array en un local
        self.add_instruction(f"astore_{var_index}")

    def visitArrayOp(self, ctx: MiniBParser.ArrayOpContext):
        var_name = ctx.ID().getText()
        var_index, array_size = self.tabla.get(
            var_name
        )  # Ahora array_size es el tamaño del array

        # Cargar la referencia del array
        self.add_instruction(f"aload_{var_index}")

        # Cargar el índice
        index_value = self.visit(ctx.exp1)
        if not isinstance(
            ctx.exp1, MiniBParser.ArithmeticExpressionContext
        ) and not isinstance(ctx.exp1, MiniBParser.ArrayAccessExpressionContext):
            self.try_ID(ctx.exp1, index_value)

        # Cargar el valor a asignar
        if ctx.exp2:
            value = self.visit(ctx.exp2)
            if not isinstance(
                ctx.exp2, MiniBParser.ArithmeticExpressionContext
            ) and not isinstance(ctx.exp2, MiniBParser.ArrayAccessExpressionContext):
                self.try_ID(ctx.exp2, value)
        else:
            value = self.visit(ctx.cond)
            if not isinstance(
                ctx.cond, MiniBParser.ArithmeticExpressionContext
            ) and not isinstance(ctx.cond, MiniBParser.ArrayAccessExpressionContext):
                self.try_ID(ctx.cond, value)

        # Ahora: stack = [arrayref, index, value]
        self.add_instruction("iastore")

    def visitArrayAccessExpression(self, ctx: MiniBParser.ArrayAccessExpressionContext):
        var_name = ctx.ID().getText()
        var_index, array_size = self.tabla.get(var_name)  # obtener también el tamaño

        # Cargar la referencia del array
        self.add_instruction(f"aload_{var_index}")

        # Evaluar y cargar el índice
        index_value = self.visit(ctx.expr)
        self.try_ID(ctx.expr, index_value)

        # stack = [arrayref, index]
        self.add_instruction("iaload")  # Carga el valor del array en la pila
        return None

    def visitRedim(self, ctx: MiniBParser.RedimContext):
        # Obtener el nombre del array y su tamaño actual
        var_name = ctx.ID().getText()
        old_var_index, old_size = self.tabla.get(var_name)

        # Obtener el nuevo tamaño
        new_size = self.visit(ctx.exp)
        # Carga el nuevo tamaño en la pila
        self.add_instruction(f"ldc {new_size}")
        # Crea el array temporal (var_name_redim)
        temp_name = var_name + "Redim"
        temp_var_index = self.tabla.add(temp_name, new_size)
        self.add_instruction("newarray int")
        self.add_instruction(f"astore_{temp_var_index}")

        # Determinar el minimo entre old_size y new_size
        min_size = min(old_size, new_size)

        # PRIMER BUCLE: Copiar desde var_name (viejo) a var_nameRedim (temp)
        # Estructura equivalente a:
        # for i = 0 to min_size-1:
        #   var_nameRedim[i] = var_name[i]

        # i = 0
        i_index = self.tabla.add("$i_loop_redim_1", 0)
        self.add_instruction("iconst_0")
        self.add_instruction(f"istore_{i_index}")

        start_label_1 = f"FOR_START_{self.label_count}"
        continue_label_1 = f"FOR_CONTINUE_{self.label_count}"
        end_label_1 = f"FOR_END_{self.label_count}"
        self.label_count += 1

        self.instructions.append(f"{start_label_1}:")
        # if i > min_size-1 goto end
        self.add_instruction(f"iload_{i_index}")
        self.add_instruction(f"ldc {min_size - 1}")
        self.add_instruction(f"if_icmpgt {end_label_1}")

        # var_nameRedim[i] = var_name[i]
        # cargar var_nameRedim
        self.add_instruction(f"aload_{temp_var_index}")
        # cargar i
        self.add_instruction(f"iload_{i_index}")
        # cargar var_name
        self.add_instruction(f"aload_{old_var_index}")
        # cargar i
        self.add_instruction(f"iload_{i_index}")
        # iaload
        self.add_instruction("iaload")
        # iastore
        self.add_instruction("iastore")

        self.instructions.append(f"{continue_label_1}:")
        self.add_instruction(f"iinc {i_index} 1")
        self.add_instruction(f"goto {start_label_1}")
        self.instructions.append(f"{end_label_1}:")

        # Ahora redimensionamos var_name
        # DIM var_name[new_size]
        # Esto es equivalente a volver a declarar el array
        self.add_instruction(f"ldc {new_size}")
        self.add_instruction("newarray int")
        # En vez de add, usamos mod, porque la variable ya existe
        self.tabla.mod(var_name, new_size)
        # var_name tiene el mismo var_index
        self.add_instruction(f"astore_{old_var_index}")

        # SEGUNDO BUCLE: Copiar desde var_nameRedim a var_name (nuevo)
        # for i = 0 to new_size-1:
        #   var_name[i] = var_nameRedim[i]

        # i = 0 (reutilizamos el mismo i_loop o creamos uno nuevo)
        i2_index = self.tabla.add("$i_loop_redim_2", 0)
        self.add_instruction("iconst_0")
        self.add_instruction(f"istore_{i2_index}")

        start_label_2 = f"FOR_START_{self.label_count}"
        continue_label_2 = f"FOR_CONTINUE_{self.label_count}"
        end_label_2 = f"FOR_END_{self.label_count}"
        self.label_count += 1

        self.instructions.append(f"{start_label_2}:")
        # if i > new_size-1 goto end
        self.add_instruction(f"iload_{i2_index}")
        self.add_instruction(f"ldc {new_size - 1}")
        self.add_instruction(f"if_icmpgt {end_label_2}")

        # var_name[i] = var_nameRedim[i]
        self.add_instruction(f"aload_{old_var_index}")
        self.add_instruction(f"iload_{i2_index}")
        self.add_instruction(f"aload_{temp_var_index}")
        self.add_instruction(f"iload_{i2_index}")
        self.add_instruction("iaload")
        self.add_instruction("iastore")

        self.instructions.append(f"{continue_label_2}:")
        self.add_instruction(f"iinc {i2_index} 1")
        self.add_instruction(f"goto {start_label_2}")
        self.instructions.append(f"{end_label_2}:")
