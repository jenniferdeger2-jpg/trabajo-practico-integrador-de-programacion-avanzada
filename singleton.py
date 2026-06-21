class Singleton:

    _instancia = None

    @classmethod
    def obtener_biblioteca(cls, Biblioteca):

        if cls._instancia is None:
            cls._instancia = Biblioteca()

        return cls._instancia