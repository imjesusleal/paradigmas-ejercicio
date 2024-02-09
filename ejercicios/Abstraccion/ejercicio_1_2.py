'''
Libro: Crear las clases Libro y Libreria. La clase Libro debe incluir
atributos como titulo, autor y precio. La clase Libreria debe contener una
lista de objetos Libro y métodos para calcular el precio total de todos
los libros en la librería.
'''

class Libro:
    def __init__(self, titulo: str, autor: str, precio: float):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

class Libreria:
    def __init__(self, libros: list[Libro]):
        self.libros = libros

    def calcular_precio(self):
        precio_total = 0
        for libro in self.libros:
            precio_total += libro.precio
        return precio_total
    
libro1 = Libro('The lord of the ring', 'Tolkin', 15000)
libro2 = Libro('A Game of Thrones', 'George R.R. Martin', 15000)
libro3 = Libro('Rich dad, Poor dad', 'IDK', 15000)

libreria1 = Libreria([libro1, libro2, libro3])
print(libreria1.calcular_precio())
