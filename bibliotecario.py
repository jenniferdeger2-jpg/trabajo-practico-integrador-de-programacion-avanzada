from persona import Persona

class Bibliotecario(Persona):

    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        self.legajo = legajo

    def __str__(self):
        return f"Bibliotecario: {self.nombre} {self.apellido} - Legajo: {self.legajo}"