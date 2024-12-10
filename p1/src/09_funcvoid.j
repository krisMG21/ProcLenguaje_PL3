.class public methodVacio
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
   .limit stack 100
   .limit locals 100


   ; Llamar al método funcVacio
   invokestatic methodVacio/funcVacio()V

   ; Terminar el main
   return


.end method


.method public static funcVacio()V

   .limit stack 100
   .limit locals 100

   getstatic java/lang/System/out Ljava/io/PrintStream;

   ldc "Esta función es inútil"

   invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
   return

.end method
