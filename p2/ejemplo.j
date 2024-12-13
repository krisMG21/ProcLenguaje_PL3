.class public MiniB
.super java/lang/Object

.method public static len(Ljava/lang/String;)I
    .limit stack 1
    .limit locals 0

    ; El String ya está en la cima de la pila
    invokevirtual java/lang/String/length()I

    ; Retorna el resultado (que ya está en la pila)
    ireturn
.end method

.method public static val(Ljava/lang/String;)Ljava/lang/Integer;
    .limit stack 100
    .limit locals 100

    ; Inicializar resultado
    iconst_0
    istore_1

    ; Flag para indicar si se ha encontrado algún dígito
    iconst_0
    istore_2

    ; Obtener los caracteres del String
    aload_0
    invokevirtual java/lang/String/toCharArray()[C
    astore_3

    ; Iterar sobre los caracteres
    iconst_0
    istore_4

    loop_start:
    iload_4
    aload_3
    arraylength
    if_icmpge return_result

    aload_3
    iload_4
    caload

    invokestatic java/lang/Character/isDigit(C)Z
    ifeq next_char

    ; Si es dígito, añadirlo al resultado
    ldc '0'  ; '0' en ASCII
    isub
    iload_1
    bipush 10
    imul
    iadd
    istore_1

    ; Marcar que se ha encontrado un dígito
    iconst_1
    istore_2

    next_char:
    iinc 4 1
    goto loop_start

    return_result:
    iload_2
    ifeq return_nan  ; Si no se encontraron dígitos, devolver null

    iload_1
    invokestatic java/lang/Integer/valueOf(I)Ljava/lang/Integer;
    areturn

    return_nan:
    aconst_null
    areturn
.end method
    
.method public static isNan(Ljava/lang/Object;)I
    .limit stack 2
    .limit locals 1

    ; Comprobar si el valor es null
    aload_0            ; Cargar el parámetro en la pila
    ifnull ReturnTrue  ; Si es null, ir a ReturnTrue

    ; Comprobar si el valor es una instancia de Double o Float (para NaN)
    aload_0
    instanceof java/lang/Double
    ifeq CheckFloat    ; Si no es Double, verificar Float

    ; Comprobar si es NaN en Double
    aload_0
    checkcast java/lang/Double
    invokevirtual java/lang/Double/isNaN()Z
    ifne ReturnTrue    ; Si es NaN, ir a ReturnTrue
    goto ReturnFalse

CheckFloat:
    aload_0
    instanceof java/lang/Float
    ifeq ReturnFalse   ; Si no es Float, no es NaN

    ; Comprobar si es NaN en Float
    aload_0
    checkcast java/lang/Float
    invokevirtual java/lang/Float/isNaN()Z
    ifne ReturnTrue    ; Si es NaN, ir a ReturnTrue

ReturnFalse:
    iconst_0           ; Devuelve 0 si no es null ni NaN
    ireturn

ReturnTrue:
    iconst_1           ; Devuelve 1 si es null o NaN
    ireturn

.end method

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "12345"
    .method public static len(Ljava/lang/String;)I
    ldc 7
    invokevirtual java/io/PrintStream/println(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "not a number"
    invokestatic MiniB/val(Ljava/lang/String;)Ljava/lang/Integer;
    ldc None
    invokestatic MiniB/len(Ljava/lang/Object;)I;
    ldc 0
    invokevirtual java/io/PrintStream/println(I)V
    return
.end method
