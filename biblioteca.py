from usuario import Usuario
from libro import Libro
from prestamo import Prestamo
from decoradores import registrar_accion
from metaclase import MetaBiblioteca

class Biblioteca(metaclass=MetaBiblioteca):

    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []
        
    @registrar_accion    
    def alta_usuario(self):

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        correo = input("Correo: ")

        for usuario in self.usuarios:
            if usuario.dni == dni:
                print("Ya existe un usuario con ese DNI.")
                return

        usuario = Usuario(nombre, apellido, dni, correo)
        self.usuarios.append(usuario)

        print("Usuario agregado correctamente.")

    def listar_usuarios(self):

        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        print("\n===== USUARIOS =====")

        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario}")

    def modificar_usuario(self):

        dni = input("Ingrese el DNI del usuario: ")

        for usuario in self.usuarios:

            if usuario.dni == dni:

                usuario.nombre = input("Nuevo nombre: ")
                usuario.apellido = input("Nuevo apellido: ")
                usuario.correo = input("Nuevo correo: ")

                print("Usuario modificado correctamente.")
                return

        print("Usuario no encontrado.")

    def baja_usuario(self):

        dni = input("Ingrese el DNI del usuario: ")

        for usuario in self.usuarios:

            if usuario.dni == dni:
                self.usuarios.remove(usuario)
                print("Usuario eliminado correctamente.")
                return

        print("Usuario no encontrado.")
        
    @registrar_accion
    def alta_libro(self):

        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        anio = int(input("Año de publicación: "))
        paginas = int(input("Cantidad de páginas: "))

        for libro in self.libros:
            if libro.isbn == isbn:
                print("Ya existe un libro con ese ISBN.")
                return

        libro = Libro(titulo, autor, isbn, anio, paginas)

        self.libros.append(libro)

        print("Libro agregado correctamente.")

    def listar_libros(self):

        if not self.libros:
            print("No hay libros registrados.")
            return

        print("\n===== LIBROS =====")

        for i, libro in enumerate(self.libros, start=1):
            print(f"{i}. {libro}")

    def modificar_libro(self):

        isbn = input("Ingrese el ISBN del libro: ")

        for libro in self.libros:

            if libro.isbn == isbn:

                libro.titulo = input("Nuevo título: ")
                libro.autor = input("Nuevo autor: ")
                libro.anio = int(input("Nuevo año: "))
                libro.paginas = int(input("Nueva cantidad de páginas: "))

                print("Libro modificado correctamente.")
                return

        print("Libro no encontrado.")

    def baja_libro(self):

        isbn = input("Ingrese el ISBN del libro: ")

        for libro in self.libros:

            if libro.isbn == isbn:
                self.libros.remove(libro)
                print("Libro eliminado correctamente.")
                return

        print("Libro no encontrado.")
        
    @registrar_accion
    def registrar_prestamo(self):

        dni = input("Ingrese el DNI del usuario: ")
        isbn = input("Ingrese el ISBN del libro: ")

        usuario_encontrado = None
        libro_encontrado = None

        # Buscar usuario
        for usuario in self.usuarios:
            if usuario.dni == dni:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            print("Usuario no encontrado.")
            return

        # Buscar libro
        for libro in self.libros:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break

        if libro_encontrado is None:
            print("Libro no encontrado.")
            return

        # Verificar préstamo activo
        for prestamo in self.prestamos:
            if (
                prestamo.libro.isbn == isbn
                and prestamo.esta_activo()
            ):
                print("El libro ya posee un préstamo activo.")
                return

        nuevo_prestamo = Prestamo(
            usuario_encontrado,
            libro_encontrado
        )

        self.prestamos.append(nuevo_prestamo)

        print("Préstamo registrado correctamente.")

    def registrar_devolucion(self):

        isbn = input("Ingrese el ISBN del libro: ")

        for prestamo in self.prestamos:

            if (
                prestamo.libro.isbn == isbn
                and prestamo.esta_activo()
            ):

                prestamo.registrar_devolucion()

                print("Devolución registrada correctamente.")
                return

        print("No existe un préstamo activo para ese libro.")

    def prestamos_activos(self):

        hay_prestamos = False

        print("\n===== PRÉSTAMOS ACTIVOS =====")

        for prestamo in self.prestamos:

            if prestamo.esta_activo():

                hay_prestamos = True

                print("--------------------------------")
                print(f"Usuario: {prestamo.usuario}")
                print(f"Libro: {prestamo.libro}")
                print(f"Fecha: {prestamo.fecha_prestamo}")

        if not hay_prestamos:
            print("No hay préstamos activos.")