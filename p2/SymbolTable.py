class SymbolTable:
    """
    Contiene los índices de las variables declaradas en el programa.
    """

    def __init__(self):
        """
        Crea una nueva tabla de simbolos vacía.
        """
        self.symbols = {}
        self.var_count = 0

    def get(self, name):
        """
        Devuelve el valor de un simbolo, si existe.
        """
        if name not in self.symbols:
            self.symbols[name] = self.var_count
            self.var_count += 1
        return self.symbols[name]
