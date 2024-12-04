.class IfNested
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100

    ; x = 42
    ldc 42
    ; if x > 0
    ifgt L1
    ; else
    ldc "x is negative"
    goto L2
L1:
    ldc "x is positive"
L2:
    getstatic java/lang/System/out Ljava/io/PrintStream;
    swap
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V

    return
.end method
