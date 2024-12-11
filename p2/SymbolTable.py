class SymbolTable:
    """
    Contiene las variables y constantes del programa,
    con sus correspondientes valores.

    (Las funciones no se contemplan en esta tabla, ya que de eso se ocupa Jasmin, cuando toque simplemente escribimos
    el codigo Jasmin que permita definir y usar las funciones.)
    """

    def __init__(self):
        """
        Crea una nueva tabla de simbolos vacía.
        """
        self.symbols = {}

    def add(self, name, value):
        """
        Agrega un simbolo a la tabla de simbolos, si
        no existe ya.
        """
        if name in self.symbols:
            raise Exception(f"Symbol {name} already exists")

        self.symbols[name] = value

    def mod(self, name, value):
        """
        Modifica el valor de un simbolo, si existe.
        """
        if name not in self.symbols:
            raise Exception(f"Symbol {name} not found")
        self.symbols[name] = value

    def get(self, name):
        """
        Devuelve el valor de un simbolo, si existe.
        """
        if name not in self.symbols:
            raise Exception(f"Symbol {name} not found")
        return self.symbols[name]
