import sys


class SymbolTable:
    """
    Contiene los índices de las variables declaradas en el programa.
    """

    def __init__(self):
        """
        Crea una nueva tabla de simbolos vacía.
        """
        self.symbols = {}
        self.var_count = -1

    def add(self, name: str, value):
        """
        Agrega un nuevo simbolo a la tabla y devuelve el índice y valor.
        Avisa si la variable ya ha sido declarada.
        """
        if name in self.symbols:
            print(f"WARNING: Variable {name} declarada más de una vez.")
        else:
            self.symbols[name] = (self.var_count, value)
            self.var_count += 1
        return self.var_count

    def get(self, name: str):
        """
        Devuelve el valor e indice de un simbolo, si existe, si no lanza un error.
        """
        if name not in self.symbols:
            sys.exit(f"ERROR: Variable {name} no declarada.")
            # Sale del programa
        return self.symbols[name]
