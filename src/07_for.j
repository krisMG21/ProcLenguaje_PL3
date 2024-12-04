.class public For
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 10
    .limit locals 2

    ; Inicializamos el contador (i) a 0
    iconst_0            ; Cargar el valor 0 en la pila
    istore_1            ; Guardar el valor de 0 en la variable local 1 (i)

    ; Inicia el bucle for: para i = 0; i < 5; i++
    start_loop:     ; Etiqueta para el inicio del bucle
    iload_1             ; Cargar el valor de i
    bipush 5            ; Cargar el valor 5
    if_icmpge end_loop  ; Si i >= 5, salimos del bucle

    ; Imprimir el valor de i
    getstatic java/lang/System/out Ljava/io/PrintStream;  ; Obtener System.out
    iload_1             ; Cargar el valor de i
    invokevirtual java/io/PrintStream/println(I)V   ; Imprimir el valor de i

    ; Incrementar i (i++)
    iinc 1 1            ; Incrementar el valor de la variable local 1 (i) por 1

    goto start_loop     ; Volver al inicio del bucle

    end_loop:      ; Etiqueta para el final del bucle

    return              ; Terminar la ejecución del método
.end method
