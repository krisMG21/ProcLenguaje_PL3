.class public MiniB
.super java/lang/Object


.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    ldc 5
    newarray int
    astore_0
    aload_0
    ldc 0
    ldc "Hello"
    iastore
    return
.end method
