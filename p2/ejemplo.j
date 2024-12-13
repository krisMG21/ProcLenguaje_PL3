.class public MiniB
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    ldc 1
    istore_0
    ldc 1.1
    fstore_1
    getstatic java/lang/System/out Ljava/io/PrintStream;
    
    new java/lang/StringBuilder
    dup
    invokespecial java/lang/StringBuilder/<init>()V

    ldc "1"
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    ldc "2"
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
    getstatic java/lang/System/out Ljava/io/PrintStream;
    swap
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 2.0
    fload_1
    fsub
    invokevirtual java/io/PrintStream/println(F)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 2.0
    ldc 3.3
    fmul
    invokevirtual java/io/PrintStream/println(F)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 4.0
    ldc 2.2
    fdiv
    invokevirtual java/io/PrintStream/println(F)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 7.0
    ldc 2.2
    fdiv
    invokevirtual java/io/PrintStream/println(F)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 5.3
    ldc 3.0
    frem
    invokevirtual java/io/PrintStream/println(F)V
    return
.end method
