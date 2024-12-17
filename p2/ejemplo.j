.class public MiniB
.super java/lang/Object


.method public static ADD(II)I
    .limit stack 10
    .limit locals 3

    ; Load parameters into local variables


; Function body
iload_0
iload_1
iadd

    ireturn
.end method


.method public static SUB(II)I
    .limit stack 10
    .limit locals 3

    ; Load parameters into local variables

iload_0
iload_1
isub

    ireturn
.end method

.method public static MUL(II)I
    .limit stack 10
    .limit locals 3

    ; Load parameters into local variables

iload_0
iload_1
imul

    ireturn
.end method


.method public static DIV(II)I
    .limit stack 10
    .limit locals 3

    ; Load parameters into local variables

iload_0
iload_1
idiv

    ireturn
.end method

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 1
    ldc 2
    invokestatic MiniB/ADD(II)I
    invokevirtual java/io/PrintStream/println(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 1
    ldc 2
    invokestatic MiniB/SUB(II)I
    invokevirtual java/io/PrintStream/println(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 1
    ldc 2
    invokestatic MiniB/MUL(II)I
    invokevirtual java/io/PrintStream/println(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc 1
    ldc 2
    invokestatic MiniB/DIV(II)I
    invokevirtual java/io/PrintStream/println(I)V
    return
.end method
