.class public MiniB
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    ldc 5
    istore_0
    ldc 10
    istore_1
    ldc 15
    istore_2
    iload_0
    iload_1
    iload_1
    iload_2
    iand
    iload_2
    ldc 10
    iconst_1
    ixor
    ior
    ifeq ELSE_0
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Condition met"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    goto ENDIF_0
    ELSE_0:
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Condition not met"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    ENDIF_0:
    return
.end method
