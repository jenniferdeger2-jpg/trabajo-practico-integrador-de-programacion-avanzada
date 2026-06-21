from datetime import date

class Prestamo:

    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None

    def registrar_devolucion(self):
        self.fecha_devolucion = date.today()

    def esta_activo(self):
        return self.fecha_devolucion is None