.class public MiniB
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    ldc 1
    istore_0
    REPEAT_START_0:
    getstatic java/lang/System/out Ljava/io/PrintStream;
    iload_0
    invokevirtual java/io/PrintStream/println(I)V
    iload_0
    ldc 1
    iadd
    ldc 1
    istore_0
    iload_0
    ldc 5
    if_icmpne REPEAT_START_0
    REPEAT_END_0:
    return
.end method
