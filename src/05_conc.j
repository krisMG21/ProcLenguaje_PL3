.class public Concatenation
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
   .limit stack 100
   .limit locals 100

   getstatic java/lang/System/out Ljava/io/PrintStream;

   ldc 42
   invokevirtual java/lang/String/valueOf(I)Ljava/lang/String;
   astore_1
   ldc "The answer is "
   aload_1
   invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
   invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
   return
.end method
