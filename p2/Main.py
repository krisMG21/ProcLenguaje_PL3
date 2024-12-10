import sys
from antlr4 import InputStream, CommonTokenStream, ParseTree
from MiniBLexer import MiniBLexer
from MiniBParser import MiniBParser
from MyVisitor import MyVisitor


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Main.py <file>")
        sys.exit(1)

    file = sys.argv[1]

    with open(file, "r") as f:
        text = f.read()
        jasmin_text = compile(text)
        f.write(jasmin_text)
        f.close()


def compile(text: str):
    lexer: MiniBLexer = MiniBLexer(InputStream(text))
    tokens: CommonTokenStream = CommonTokenStream(lexer)
    parser: MiniBParser = MiniBParser(tokens)
    tree: ParseTree = parser.program()

    return create_jasmin_file(new MyVisitor().visit(tree))

def create_jasmin_file(instructions):
    text = f""".class public Sumar
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
   .limit stack 100visitor: MiniBVisitor = MiniBVisitor()
    jasmin_text = create_jasmin_file())
    return jasmin_text

   .limit locals 100

   getstatic java/lang/System/out Ljava/io/PrintStream;
{instructions}
   invokevirtual java/io/PrintStream/println(I)V
   return

.end method"""
    return text


if __name__ == "__main__":
    main()

