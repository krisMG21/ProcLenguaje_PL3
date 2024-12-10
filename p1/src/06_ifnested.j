.class public IfNested
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 3
    .limit locals 3

    ldc 5
    istore_1

    ldc 10
    istore 2
    istore_1

    ldc 15            ; Load 15 onto the stack (c)
    istore 3          ; Store it in local variable 3 (c)

    ; First if statement: if (a < b)
    iload 1           ; Load a onto the stack
    iload 2           ; Load b onto the stack
    if_icmpge else1   ; If a >= b, jump to else1

    ; Nested if statement: if (b < c)
    iload 2           ; Load b onto the stack
    iload 3           ; Load c onto the stack
    if_icmpge else2   ; If b >= c, jump to else2

    ; If b < c, print "b is less than c"
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "b is less than c"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
    goto end_if       ; Jump to end_if

else2:
    ; If b >= c, print "b is not less than c"
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "b is not less than c"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V

end_if:
    goto end_outer_if  ; Jump to end_outer_if

else1:
    ; If a >= b, print "a is not less than b"
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "a is not less than b"
    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V

end_outer_if:
    return
.end method
