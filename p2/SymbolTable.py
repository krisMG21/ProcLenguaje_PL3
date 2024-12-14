class SymbolTable:
    """
    Contiene los índices de las variables declaradas en el programa.
    """

    def __init__(self):
        """
        Crea una nueva tabla de símbolos vacía.
        """
        self.symbols = {}
        self.var_count = 0
        self.error = False

    def add(self, name: str, value):  # -> int, any
        """
        Agrega un nuevo símbolo a la tabla y devuelve el índice y valor.
        Avisa si la variable ya ha sido declarada.
        """
        if name in self.symbols:
            print(f"WARNING: Variable {name} ya declarada. Usando la existente.")
            return self.symbols[name][0]
        else:
            self.symbols[name] = (self.var_count, value)
            self.var_count += 1
        return self.var_count - 1

    def get(self, name: str):  # -> int, any
        """
        Devuelve el valor e índice de un símbolo, si existe.
        Lanza una excepción KeyError si el símbolo no está declarado.
        """
        if name not in self.symbols:
            self.error = True
            raise KeyError(f"ERROR: Variable {name} no declarada.")
        return self.symbols[name]

    def get_by_index(self, index: int):  # -> str, any
        """
        Devuelve el nombre de un símbolo por su índice.
        Lanza una excepción KeyError si el índice no está asociado a ningún símbolo.
        """
        for name, value in self.symbols.items():
            if value[0] == index:
                return name, value[1]
        self.error = True
        raise KeyError(f"ERROR: No se encontró ningún símbolo con el índice {index}.")

    def mod(self, name: str, value):  # None
        """
        Modifica el valor de un símbolo, si existe.
        Lanza una excepción KeyError si el símbolo no está declarado.
        Devuelve el índice de la variable.
        """
        if name not in self.symbols:
            self.error = True
            raise KeyError(f"ERROR: Variable a modificar {name} no declarada.")
        self.symbols[name] = (self.symbols[name][0], value)
        return self.symbols[name][0]

    def __str__(self):
        """
        Devuelve una representación de la tabla de símbolos.
        """
        return str(self.symbols)


