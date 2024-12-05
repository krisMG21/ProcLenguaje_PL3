.class public While
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 10
    .limit locals 2

    ; Inicializamos el contador (i) a 9
    bipush 9            ; Cargar el valor 9 en la pila
    istore_1            ; Guardar el valor de 9 en la variable local 1 (i)

    ; Inicia el bucle while: mientras i > 0
    start_loop:     ; Etiqueta para el inicio del bucle
    iload_1             ; Cargar el valor de i
    ifle end_loop       ; Si i <= 0, salimos del bucle

    ; Imprimir el valor de i
    getstatic java/lang/System/out Ljava/io/PrintStream;  ; Obtener System.out
    iload_1             ; Cargar el valor de i
    invokevirtual java/io/PrintStream/println(I)V   ; Imprimir el valor de i

    ; Decrementar i en 2 (i -= 2)
    iinc 1 -2           ; Decrementar el valor de la variable local 1 (i) por 2

    goto start_loop     ; Volver al inicio del bucle

    end_loop:      ; Etiqueta para el final del bucle

    return

.end method
