class MetaBiblioteca(type):

    def __new__(cls, nombre, bases, atributos):

        if "__init__" not in atributos:
            raise TypeError(
                "La clase debe definir un constructor (__init__)"
            )

        return super().__new__(
            cls,
            nombre,
            bases,
            atributos
        )