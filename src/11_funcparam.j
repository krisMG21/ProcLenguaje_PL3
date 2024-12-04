.class public methodParam
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
   .limit stack 2
   .limit locals 1

   ; Cargar el número 42 en la pila
   bipush 42

   ; Llamar al método funcPatam con el número como argumento
   invokestatic methodParam/funcParam(I)V
   
   ; Terminar el main
   return
.end method


.method public static funcParam(I)V
   .limit stack 2
   .limit locals 1

   ; Obtener System.out para imprimir
   getstatic java/lang/System/out Ljava/io/PrintStream;

   ; Cargar el número recibido (primer argumento)
   iload_0

   ; Llamar a println para imprimir el número
   invokevirtual java/io/PrintStream/println(I)V

   ; Terminar el método
   return   
.end method
