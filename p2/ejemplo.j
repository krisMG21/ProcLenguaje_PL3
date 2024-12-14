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
    ldc 3
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
    newarray int
    astore_2
    iconst_0
    istore_3
FOR_START_1:
    iload_3
    ldc 2
    if_icmpgt FOR_END_1
    aload_2
    iload_3
    aload_0
    iload_3
    iaload
    iastore
FOR_CONTINUE_1:
    iinc 3 1
    goto FOR_START_1
FOR_END_1:
    ldc 5
    newarray int
    astore_0
    iconst_0
    istore_4
FOR_START_2:
    iload_4
    ldc 4
    if_icmpgt FOR_END_2
    aload_0
    iload_4
    aload_2
    iload_4
    iaload
    iastore
FOR_CONTINUE_2:
    iinc 4 1
    goto FOR_START_2
FOR_END_2:
    return
.end method
