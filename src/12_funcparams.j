.class public methodParams
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 10
    .limit locals 2

    ; Llamar a la función funcParams con un String y un int
    ldc "Número:"   ; Cargar el String
    bipush 42                   ; Cargar el entero 42
    invokestatic methodParams/funcParams(Ljava/lang/String;I)V

    return
.end method

.method public static funcParams(Ljava/lang/String;I)V
    .limit stack 10
    .limit locals 3

    ; Local 0: String (argumento)
    ; Local 1: int (argumento)

    ; Imprimir el String
    getstatic java/lang/System/out Ljava/io/PrintStream;  ; Obtener System.out
    aload 0                                             ; Cargar el String
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V  ; Imprimir

    ; Imprimir el entero
    getstatic java/lang/System/out Ljava/io/PrintStream;  ; Obtener System.out
    iload 1                                             ; Cargar el int
    invokevirtual java/io/PrintStream/println(I)V       ; Imprimir

    return
.end method
