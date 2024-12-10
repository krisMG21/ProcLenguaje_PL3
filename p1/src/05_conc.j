.class public Concatenation
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100

    ; Create StringBuilder
    new java/lang/StringBuilder
    dup
    invokespecial java/lang/StringBuilder/<init>()V

    ; Append "Hello" to StringBuilder
    ldc "The answer is "
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    ; Append 42 to StringBuilder (convert to String)
    ldc 42
    invokestatic java/lang/String/valueOf(I)Ljava/lang/String;  ; Convert int to String
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    ; Convert StringBuilder to String
    invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;

    ; Print the result
    getstatic java/lang/System/out Ljava/io/PrintStream;
    swap
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V

    return
.end method
