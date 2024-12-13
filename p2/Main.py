import os
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
        jasmin_text = compile_source(file)
        
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
    print("Checking if visitor generation is needed...")
    grammar_file = "MiniB.g4"
    generated_files = ["MiniBLexer.py", "MiniBParser.py", "MiniBVisitor.py"]

    # Get the modification time of the grammar file
    grammar_mtime = os.path.getmtime(grammar_file)

    # Check if any generated file is older than the grammar file
    need_generation = False
    for file in generated_files:
        if not os.path.exists(file) or os.path.getmtime(file) < grammar_mtime:
            need_generation = True
            break

    if need_generation:
        print("Generating visitor for the grammar...")
        try:
            subprocess.run(
                ["antlr4", "-Dlanguage=Python3", "-no-listener", "-visitor", grammar_file],
                check=True,
            )
            print("Visitor generated successfully.")
            
            # Optionally, delete intermediate files if needed
            intermediate_files = ["MiniBLexer.intermediate", "MiniBParser.intermediate"]  # Adjust as necessary
            for file in intermediate_files:
                if os.path.exists(file):
                    os.remove(file)
                    print(f"Deleted intermediate file: {file}")

        except subprocess.CalledProcessError as e:
            print("Error generating the visitor:", e)
    else:
        print("No need to generate the visitor. Files are up to date.")


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
    if visitor.error:
            print("Error/es al compilar el código fuente.")
            sys.exit(1)
    return text


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
