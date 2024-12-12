.class public MiniB
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
    .limit stack 100
    .limit locals 100
    ldc "foo"
    astore_0
    ldc 123
    istore_1
    lcd bar
    istore_(-1, 'foo')
    return
.end method
