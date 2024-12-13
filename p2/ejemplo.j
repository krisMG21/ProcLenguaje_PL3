.class public MiniB
.super java/lang/Object


.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    ldc 1
    ldc 2
    if_icmpge ELSE_0
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "true"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    goto ENDIF_0
    ELSE_0:
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "false"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    ENDIF_0:
    ldc 2
    ldc 3
    if_icmple ELSE_1
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "true"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    goto ENDIF_1
    ELSE_1:
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "false"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    ENDIF_1:
    return
.end method
