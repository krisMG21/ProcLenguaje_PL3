import sys
import subprocess
from antlr4 import InputStream, CommonTokenStream
from antlr4.ParserRuleContext import ParseTree
from MiniBLexer import MiniBLexer
from MiniBParser import MiniBParser
from Visitor import Visitor


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_fuente> [-o <output>] [-m <modos>]")
        sys.exit(1)

    file = sys.argv[1]

    try:
        output_index = sys.argv.index("-o")
        output = sys.argv[output_index + 1]
    except ValueError:
        output = "./ejemplo.j"

    try:
        mode_index = sys.argv.index("-m")
        modes = sys.argv[mode_index + 1]
    except ValueError:
        modes = "c"

    if "v" in modes:
        generate_visitor()

    if "c" in modes:
        jasmin_text, error = compile_source(file)
        if error:
            print("Error/es al compilar el código fuente.")
            sys.exit(1)
        try:
            with open(output, "w") as f:
                print("Guardando archivo en:", output)
                f.write(jasmin_text)
        except Exception:
            print("Error al guardar el archivo.")
            sys.exit(1)

        compile_to_bytecode(output)

    if "e" in modes:
        execute_program()


def generate_visitor():
    print("Generando visitor para la gramática...")
    try:
        subprocess.run(
            ["antlr4", "-Dlanguage=Python3", "-no-listener", "-visitor", "MiniB.g4"],
            check=True,
        )
        print("Visitor generado con éxito.")
    except subprocess.CalledProcessError as e:
        print("Error al generar el visitor:", e)


def compile_source(file):
    print("Compilando fuente...")
    with open(file, "r") as f:
        text = f.read()

    lexer: MiniBLexer = MiniBLexer(InputStream(text))
    tokens: CommonTokenStream = CommonTokenStream(lexer)
    parser: MiniBParser = MiniBParser(tokens)
    tree: ParseTree = parser.program()
    visitor: Visitor = Visitor()
    text: str = visitor.visit(tree)
    return text, visitor.error


def compile_to_bytecode(jasmin_file):
    print("Compilando a bytecode usando Jasmin...")
    try:
        subprocess.run(["java", "-jar", "jasmin.jar", jasmin_file], check=True)
        print("Bytecode generado con éxito.")
    except subprocess.CalledProcessError as e:
        print("Error de proceso al compilar a bytecode:", e)
        sys.exit(1)
    except Exception:
        print("Error de compilación, abortando...")
        sys.exit(1)


def execute_program():
    print("Ejecutando programa...")
    try:
        subprocess.run(["java", "MiniB"], check=True)
        print("Programa ejecutado con éxito.")
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el programa:", e)


if __name__ == "__main__":
    main()
