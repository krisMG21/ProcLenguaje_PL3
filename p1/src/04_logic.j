.class public LogicOp
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 0
    ldc 1
    iand

    invokevirtual java/io/PrintStream/println(I)V
    return

.end method
