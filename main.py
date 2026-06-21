from biblioteca import Biblioteca
from singleton import Singleton

biblioteca = Singleton.obtener_biblioteca(Biblioteca)

def menu_usuarios():

    while True:

        print("\n========== GESTIÓN DE USUARIOS ==========")
        print("1. Alta")
        print("2. Modificación")
        print("3. Baja")
        print("4. Listado")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.alta_usuario()

        elif opcion == "2":
            biblioteca.modificar_usuario()

        elif opcion == "3":
            biblioteca.baja_usuario()

        elif opcion == "4":
            biblioteca.listar_usuarios()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


def menu_libros():

    while True:

        print("\n========== GESTIÓN DE LIBROS ==========")
        print("1. Alta")
        print("2. Modificación")
        print("3. Baja")
        print("4. Listado")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.alta_libro()

        elif opcion == "2":
            biblioteca.modificar_libro()

        elif opcion == "3":
            biblioteca.baja_libro()

        elif opcion == "4":
            biblioteca.listar_libros()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


def menu_prestamos():

    while True:

        print("\n========== GESTIÓN DE PRÉSTAMOS ==========")
        print("1. Registrar préstamo")
        print("2. Registrar devolución")
        print("3. Ver préstamos activos")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.registrar_prestamo()

        elif opcion == "2":
            biblioteca.registrar_devolucion()

        elif opcion == "3":
            biblioteca.prestamos_activos()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")


while True:

    print("\n========================================")
    print("      SISTEMA DE BIBLIOTECA DIGITAL")
    print("========================================")
    print("1. Gestión de Usuarios")
    print("2. Gestión de Libros")
    print("3. Gestión de Préstamos")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menu_usuarios()

    elif opcion == "2":
        menu_libros()

    elif opcion == "3":
        menu_prestamos()

    elif opcion == "0":
        print("\n¡Hasta luego!")
        break

    else:
        print("Opción inválida.")