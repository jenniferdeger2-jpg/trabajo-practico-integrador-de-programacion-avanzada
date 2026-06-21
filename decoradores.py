from functools import wraps

def registrar_accion(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("\n==============================")
        print(f"Ejecutando -> {func.__name__}")
        print("==============================")

        resultado = func(*args, **kwargs)

        print("==============================")
        print("Operación finalizada")
        print("==============================\n")

        return resultado

    return wrapper