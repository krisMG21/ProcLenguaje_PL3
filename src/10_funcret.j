.class public methodRet
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 10
    .limit locals 10

    ; Llamar al método funcRet
    invokestatic methodRet/funcRet()I

    ; Imprimir el valor de retorno
    getstatic java/lang/System/out Ljava/io/PrintStream;
    swap
    invokevirtual java/io/PrintStream/println(I)V

    ; Terminar el main
    return

.end method

.method public static funcRet()I
    .limit stack 10
    .limit locals 10

    getstatic java/lang/System/out Ljava/io/PrintStream;

    ldc "Esta función devuelve 10"

    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V

    ; Retornar el valor 10
    bipush 10
    ireturn

.end method
