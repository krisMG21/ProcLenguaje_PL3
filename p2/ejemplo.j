.class public MiniB
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Name: "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    new java/util/Scanner
    dup
    getstatic java/lang/System/in Ljava/io/InputStream;
    invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;
    astore_0
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "name"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    return
.end method
