import sys
from antlr4 import InputStream, CommonTokenStream
from antlr4.ParserRuleContext import ParseTree
from MiniBLexer import MiniBLexer
from MiniBParser import MiniBParser
from Visitor import Visitor
from SymbolTable import SymbolTable


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Main.py <file>")
        sys.exit(1)

    file = sys.argv[1]
    
    try:
        output_index = sys.argv.index("-o")
        if (output_index != -1): 
            output += sys.argv[output_index+1]
    except:
        output = "./ejemplo"
        

    with open(file, "r") as f:
        text = f.read()
        jasmin_text = compile(text)
        print(jasmin_text)
        f.close()

    with open(output, "w") as f:
        f.write(jasmin_text)
        f.close()


def compile(text: str):
    # Creamos tabla de simbolos

    lexer: MiniBLexer = MiniBLexer(InputStream(text))
    tokens: CommonTokenStream = CommonTokenStream(lexer)
    parser: MiniBParser = MiniBParser(tokens)
    tree: ParseTree = parser.program()
    visitor: Visitor = Visitor()

    return visitor.visit(tree)




if __name__ == "__main__":
    main()
