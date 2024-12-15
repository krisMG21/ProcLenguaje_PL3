VAL = """.method public static extractFirstNumber(Ljava/lang/String;)Ljava/lang/Integer;
    .limit locals 10
    .limit stack 10

    ; Parameters
    ; L0: String input
    ; L1: int index
    ; L2: char currentChar
    ; L3: StringBuilder numberBuilder
    ; L4: int number
    ; L5: boolean foundDigit

    ; Initialize local variables
    ldc 0
    istore 1          ; index = 0

    new java/lang/StringBuilder
    dup
    invokespecial java/lang/StringBuilder/<init>()V
    astore 3         ; numberBuilder = new StringBuilder()
    ldc 0
    istore 4          ; number = 0
    iconst_0
    istore 5          ; foundDigit = false

    ; Get the length of the string
    aload 0
    invokevirtual java/lang/String/length()I
    istore 6          ; length = input.length()

loop:
    iload 1
    iload 6
    if_icmpge done   ; if index >= length, exit loop

    ; Get the current character
    aload 0
    iload 1
    invokevirtual java/lang/String/charAt(I)C
    istore 2          ; currentChar = input.charAt(index)

    ; Check if the current character is a digit
    iload 2
    bipush 48         ; '0'
    if_icmplt checkSpace
    iload 2
    bipush 57         ; '9'
    if_icmpgt checkSpace

    ; It's a digit, append to numberBuilder
    aload 3
    iload 2
    invokevirtual java/lang/StringBuilder/append(C)Ljava/lang/StringBuilder;
    pop
    iconst_1
    istore 5          ; foundDigit = true

checkSpace:
    iload 5
    ifne continue     ; If we found a digit, continue collecting
    iload 2
    bipush 32         ; ' '
    if_icmpeq skip   ; If it's a space, skip it
    goto done        ; If it's a non-digit and not a space, exit

skip:
    ; Increment index and continue
    iinc 1 1
    goto loop

continue:
    ; Increment index
    iinc 1 1
    goto loop

done:
    iload 5
    ifeq returnNull   ; If no digit was found, return null

    ; Convert StringBuilder to String and parse to int
    aload 3
    invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
    invokestatic java/lang/Integer/parseInt(Ljava/lang/String;)I
    istore 4          ; number = parsed integer

    ; Return the number as Integer
    getstatic java/lang/Integer/valueOf(I)Ljava/lang/Integer;
    goto end


returnNull:
    aconst_null
    return
end:

.end method    """
LEN = """.method public static len(Ljava/lang/String;)I
    .limit stack 1
    .limit locals 1

    aload_0

    ; El String ya está en la cima de la pila
    invokevirtual java/lang/String/length()I

    ; Retorna el resultado (que ya está en la pila)
    ireturn
.end method
"""
ISNAN = """.method public static isNan(Ljava/lang/Object;)I
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
"""
