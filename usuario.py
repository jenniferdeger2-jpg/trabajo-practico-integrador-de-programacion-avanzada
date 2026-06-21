from persona import Persona

class Usuario(Persona):

    def __init__(self,nombre,apellido,dni,correo):

        super().__init__(nombre,apellido,dni)

        self.correo=correo

    def __str__(self):

        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"