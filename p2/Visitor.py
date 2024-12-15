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
        self.function_defs = {}
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
            + "\n".join(self.imports)
            + "\n".join(self.functions)
            + main
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

    def load_var_f(self, var_index: int, var_value):
        """
        Carga una variable en la pila con el tipo adecuado.
        """
        match var_value:
            case str() | None:
                self.add_function(f"aload_{var_index}")
            case int() | bool():
                self.add_function(f"iload_{var_index}")
            case float():
                self.add_function(f"fload_{var_index}")

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

    def have_to_load(self, exp):
        is_op = False
        try:
            is_op = bool(exp.op)
        except Exception:
            try:
                is_op = bool(exp.fun)
            except Exception:
                pass

        return not is_op

    def try_ID(self, exp, var_value):
        try:
            var_name = exp.ID().getText()
            var_index, _ = self.tabla.get(var_name)
            self.load_var(var_index, var_value)
        except AttributeError:
            if self.have_to_load(exp):
                if (
                    isinstance(var_value, str)
                    and '"' not in var_value[1:-1]
                    or not isinstance(var_value, str)
                ):
                    self.add_instruction(f"ldc {var_value}")

    def try_IDf(self, exp, var_value):
        try:
            var_name = exp.ID().getText()
            var_index, _ = self.tabla.get(var_name)
            self.load_var_f(var_index, var_value)
        except AttributeError:
            if self.have_to_load(exp):
                if (
                    isinstance(var_value, str)
                    and '"' not in var_value[1:-1]
                    or not isinstance(var_value, str)
                ):
                    self.add_function(f"ldc {var_value}")

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

        self.try_ID(ctx.exp, var_value)
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
            self.try_ID(ctx.exp, value)
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

    def visitArithmeticExpression(self, ctx: MiniBParser.ArithmeticExpressionContext):
        val0 = self.visit(ctx.expression(0))
        val1 = self.visit(ctx.expression(1))

        # Tratamiento de nulos
        val0 = 0 if val0 is None else val0
        val1 = 0 if val1 is None else val1

        # Manejo especial para convertir strings a números si es posible
        var_index_0 = None
        var_index_1 = None

        if isinstance(val0, str) and not isinstance(val1, str):
            try:
                raw_val0 = val0.strip('"')  # Elimina las comillas externas
                val0 = int(raw_val0) if "." not in raw_val0 else float(raw_val0)
                var_name_0 = ctx.expression(0).getText()
                var_index_0 = self.tabla.add(
                    f"{var_name_0}_num", val0
                )  # Asignar nueva posición
                self.add_instruction(f"ldc {val0}")  # Cargar el valor convertido
                self.store_var(var_index_0, val0)  # Guardar el valor convertido
            except ValueError:
                val1 = f'"{val1}"'
                return self.concat(val0, str(val1))

        elif isinstance(val1, str) and not isinstance(val0, str):
            try:
                raw_val1 = val1.strip('"')  # Elimina las comillas externas
                val1 = int(raw_val1) if "." not in raw_val1 else float(raw_val1)
                var_name_1 = ctx.expression(1).getText()
                var_index_1 = self.tabla.add(
                    f"{var_name_1}_num", val1
                )  # Asignar nueva posición
                self.add_instruction(f"ldc {val1}")  # Cargar el valor convertido
                self.store_var(var_index_1, val1)  # Guardar el valor convertido
            except ValueError:
                # Transformar el valor que no es string a string y concatenarlos
                val0 = f'"{val0}"'
                return self.concat(str(val0), val1)
        elif isinstance(val0, str) and isinstance(val1, str):
            return self.concat(val0, val1)

        # Contagio de tipo
        if isinstance(val1, float) and isinstance(val0, int):
            val0 = float(val0)
        elif isinstance(val0, float) and isinstance(val1, int):
            val1 = float(val1)

        # Referencias consistentes a los índices de variables locales
        if var_index_0 is not None:
            self.add_instruction(f"iload_{var_index_0}")
        else:
            self.try_ID(ctx.expression(0), val0)

        if var_index_1 is not None:
            self.add_instruction(f"iload_{var_index_1}")
        else:
            self.try_ID(ctx.expression(1), val1)

        # Generar la operación
        op = self.visit(ctx.op)
        instr = ""

        # Determinar las instrucciones basadas en el tipo
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

        # Agregar la instrucción final
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

    def visitFunctionDef(self, ctx: MiniBParser.FunctionDefContext):
        # Extract function name and parameters
        function_name = ctx.name.text
        params = ctx.params.text.split(",") if ctx.params else []
        param_count = len(params)

        # Visit the expression (function body)
        function_body = self.visit(ctx.exp)

        jasmin_code = f"""
.method public static {function_name}({'I' * param_count})I
    .limit stack 10
    .limit locals {param_count + 1}

    ; Load parameters into local variables
"""
        for i, param in enumerate(params):
            jasmin_code += f"    iload_{i} ; Load parameter {param}\n"

        jasmin_code += f"""
    ; Function body
        {function_body}

    ireturn
.end method
    """
        # Add the function to the list of defined functions
        self.add_function(jasmin_code)

    def visitGenericFunction(self, ctx: MiniBParser.GenericFunctionContext):
        # Extract function name and arguments
        function_name = ctx.name.text
        arguments = ctx.expr

        # Visit each argument and push it onto the stack
        for arg in arguments:
            self.visit(arg)

        # Generate Jasmin code to call the function
        param_count = len(arguments)
        self.add_instruction(
            f"invokestatic MiniB/{function_name}({'I' * param_count})I"
        )

    def visitValFunction(self, ctx: MiniBParser.ValFunctionContext):
        value = self.visit(ctx.expr)

        try: 
            value = int(value[1:-1])
            self.try_ID(ctx.expr, value)
        except:
            value = None
            self.add_instruction(f"aconst_null")
        
        # 

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
        #self.add_instruction("invokestatic MiniB/len(Ljava/lang/Object;)I")
        
        return value

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
        var_name = ctx.ID().getText()  # Nombre de la variable
        size = self.visit(ctx.exp)  # Calcula la dimensión del array

        # Cargar el tamaño en la pila
        self.add_instruction(f"ldc {size}")

        # Crear un array de enteros
        self.add_instruction("newarray int")

        try:
            # Añadir la variable a la tabla de símbolos
            var_index = self.tabla.add(var_name, size)
        except KeyError as e:
            print(f"Error al agregar variable a la tabla de símbolos: {e}")
            self.error = True
            return

        # Guardar la referencia del array en un local
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
        var_name = ctx.ID().getText()
        old_var_index, old_size = self.tabla.get(var_name)

        new_size = self.visit(ctx.exp)
        if not isinstance(new_size, int):
            raise ValueError("El tamaño de REDIM debe ser un entero.")

        # Crear el nuevo array temporal
        self.add_instruction(f"ldc {new_size}")
        temp_name = f"{var_name}_Redim"
        temp_var_index = self.tabla.add(temp_name, new_size)
        self.add_instruction("newarray int")
        self.add_instruction(f"astore_{temp_var_index}")

        min_size = min(old_size, new_size)

        # Bucle 1: Copiar del array viejo al temporal
        i_index = self.tabla.add(f"$i_loop_redim_{self.label_count}_1", 0)
        self.add_instruction("iconst_0")
        self.add_instruction(f"istore_{i_index}")

        self.index_for.append(self.label_count)
        start_label_1 = f"FOR_START_{self.label_count}"
        continue_label_1 = f"FOR_CONTINUE_{self.label_count}"
        end_label_1 = f"FOR_END_{self.label_count}"
        self.label_count += 1
        # Generar bucle
        self.add_instruction(f"{start_label_1}:")
        self.add_instruction(f"iload_{i_index}")
        self.add_instruction(f"ldc {min_size - 1}")
        self.add_instruction(f"if_icmpgt {end_label_1}")

        # Copiar valor
        self.add_instruction(f"aload_{temp_var_index}")
        self.add_instruction(f"iload_{i_index}")
        self.add_instruction(f"aload_{old_var_index}")
        self.add_instruction(f"iload_{i_index}")
        self.add_instruction("iaload")
        self.add_instruction("iastore")

        self.add_instruction(f"{continue_label_1}:")
        self.add_instruction(f"iinc {i_index} 1")
        self.add_instruction(f"goto {start_label_1}")
        self.add_instruction(f"{end_label_1}:")
        self.index_for.pop()
        # Redimensionar el array original
        self.add_instruction(f"ldc {new_size}")
        self.add_instruction("newarray int")
        self.tabla.mod(var_name, new_size)
        self.add_instruction(f"astore_{old_var_index}")

        # Bucle 2: Copiar del temporal al array redimensionado
        i2_index = self.tabla.add(f"$i_loop_redim_{self.label_count}_2", 0)
        self.add_instruction("iconst_0")
        self.add_instruction(f"istore_{i2_index}")

        self.index_for.append(self.label_count)
        start_label_2 = f"FOR_START_{self.label_count}"
        continue_label_2 = f"FOR_CONTINUE_{self.label_count}"
        end_label_2 = f"FOR_END_{self.label_count}"
        self.label_count += 1

        # Generar bucle
        self.add_instruction(f"{start_label_2}:")
        self.add_instruction(f"iload_{i2_index}")
        self.add_instruction(f"ldc {min_size - 1}")
        self.add_instruction(f"if_icmpgt {end_label_2}")
        self.index_for.pop()

        # Copiar valor
        self.add_instruction(f"aload_{old_var_index}")
        self.add_instruction(f"iload_{i2_index}")
        self.add_instruction(f"aload_{temp_var_index}")
        self.add_instruction(f"iload_{i2_index}")
        self.add_instruction("iaload")
        self.add_instruction("iastore")

        self.add_instruction(f"{continue_label_2}:")
        self.add_instruction(f"iinc {i2_index} 1")
        self.add_instruction(f"goto {start_label_2}")
        self.add_instruction(f"{end_label_2}:")
