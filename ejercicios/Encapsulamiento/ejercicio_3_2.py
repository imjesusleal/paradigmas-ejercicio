'''
Estudiante: Implementar la clase Estudiante con atributos como nombre,
edad y calificaciones. Utilizar el encapsulamiento para proteger los
datos que deban ser protegidos y proporcionar métodos públicos para
obtener dichos datos.
'''

class Estudiante:

    MATERIAS = ['POO', 'Algebra', 'Calculo', 'Estadistica']

    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

        if not (getattr(self, '_calificaciones', {})):
            setattr(self, '_calificaciones', {})

    @property
    def calificaciones(self):
        return self._calificaciones
    
    def set_calificaciones(self, materia: str, nota: int):
        """Recibe una materia y una nota. Valida la materia en los casos aplicables y
        asigna una nota al diccionario."""

        if materia in self.MATERIAS:
            self._calificaciones[materia] = nota
        else:
            return ValueError("La materia asignada no está siendo cursada")
        
    
jesus = Estudiante('jesus', 'leal', 28)

jesus.set_calificaciones('POO', 10)
print(jesus.calificaciones)

            