class Libro:

    def __init__(self, titulo, autor, isbn, anio, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} - {self.autor}"