.class public MiniB
.super java/lang/Object


.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    ldc 3
    newarray int
    astore_0
    ldc 0
    ldc 0
    istore_1
    FOR_START_0:
    iload_1
    ldc 2
    if_icmpgt FOR_END_0
    aload_0
    iload_1
    iload_1
    ldc 2
    imul
    iastore
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    iload_1
    iaload
    invokevirtual java/io/PrintStream/println(I)V
    FOR_CONTINUE_0:
    iinc 1 1
    goto FOR_START_0
    FOR_END_0:
    ldc 5
    aload_0
    astore_2
    aload_2
    arraylength
    istore_3
    ldc 5
    istore_4
    iload_4
    newarray int
    astore_0
    iload_3
    iload_4
    if_icmple MIN_LE_1
    iload_4
    istore_5
    goto MIN_END_1
    MIN_LE_1:
    iload_3
    istore_5
    MIN_END_1:
    iconst_0
    istore_6
    COPY_START_2:
    iload_6
    iload_5
    if_icmpge COPY_END_2
    aload_0
    iload_6
    aload_2
    iload_6
    iaload
    iastore
    iinc 6 1
    goto COPY_START_2
    COPY_END_2:
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    ldc 0
    iaload
    invokevirtual java/io/PrintStream/println(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    ldc 1
    iaload
    invokevirtual java/io/PrintStream/println(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    ldc 2
    iaload
    invokevirtual java/io/PrintStream/println(I)V
    return
.end method
