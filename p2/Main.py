import sys
import os
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
        output = sys.argv[output_index+1]

    except:
        output = "./ejemplo"
        

    with open(file, "r") as f:
        text = f.read()

    lexer = MiniBLexer(InputStream(text))
    tokens = CommonTokenStream(lexer)
    parser = MiniBParser(tokens)
    tree = parser.program()
    visitor = Visitor()
    return visitor.visit(tree)


def compile_to_bytecode(jasmin_file):
    print("Compilando a bytecode usando Jasmin...")
    try:
        subprocess.run(["java", "-jar", "jasmin.jar", jasmin_file], check=True)
        print("Bytecode generado con éxito.")
    except subprocess.CalledProcessError as e:
        print("Error al compilar a bytecode:", e)


def execute_program():
    print("Ejecutando programa...")
    try:
        subprocess.run(["java", "MiniB"], check=True)
        print("Programa ejecutado con éxito.")
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el programa:", e)


if __name__ == "__main__":
    main()
