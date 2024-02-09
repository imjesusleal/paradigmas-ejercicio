'''
Punto3D: Una clase que representa un punto en el espacio 3D con
coordenadas x, y, y z.
Figura3D: Una clase abstracta que representa una figura tridimensional y
define métodos abstractos para calcular su volumen y área superficial.
Cubo, Esfera y Cilindro: Subclases de Figura3D que implementan los métodos
para calcular el volumen y área superficial específicos de cada figura.
'''

from abc import ABC, abstractmethod


class Punto3D:
    def __init__(self, puntos: tuple[int | float]):
        self.x, self.y, self.z = puntos

    def punto(self) -> tuple[int | float]:
        punto = (self.x, self.y, self.z)
        return punto

class Figura3D(ABC):

    PI = 3.1416
    
    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass
 
class Cubo(Figura3D):
    def __init__(self, lados: tuple[int | float]):
        self._lados = Punto3D(lados) if self.__validate_lados(lados) else None

    @property
    def lados(self):
        return self._lados
    
    def __validate_lados(self, lados: tuple[int | float]) -> tuple[int | float, bool]:
        valid_lados = False
        if not isinstance(lados, tuple):
            raise TypeError("Debes enviar un objeto de tipo tupla")
        else:
            if len(set(lados)) == 1:
                valid_lados = True
            else:
                raise ValueError("El valor de los lados de un cubo debe ser igual")
        return lados, valid_lados
    
    def calcular_volumen(self) -> int | float:
        return self.lados.x ** 3
    
    def calcular_area(self) -> int | float:
        return 6 * (self.lados.x**2)
    
class Esfera(Figura3D):
    def __init__(self, radio: int | float):
        self._radio = radio if self.__validate_radio(radio) else None

    @property
    def radio(self):
        return self._radio 
    
    def __validate_radio(self, radio: int | float) -> tuple[int | float, bool]:
        valid_radio = False
        if isinstance(radio, (int, float)):
            valid_radio = True
        return radio, valid_radio

    def calcular_volumen(self) -> int | float:
        vol = self.radio **3
        return 4/3 * self.PI * vol
    
    def calcular_area(self) -> int | float:
        return 4 * self.PI * (self.radio**2)


class Cilindro(Figura3D):
    def __init__(self, radio: int | float, altura: int | float):
        self.radio = radio
        self.altura = altura

    def calcular_area(self) -> int | float:
        return (2 * self.PI * self.altura) + (2 * self.PI * self.radio**2)

    def calcular_volumen(self) -> int | float:
        return self.PI * (self.radio**2) * self.altura 

lados = (3,3,3)
c = Cubo(lados)
print(c.calcular_area())
print(c.calcular_volumen())

e = Esfera(5)
print(e.calcular_area())
print(e.calcular_volumen())

d = Cilindro(5,10)
print(d.calcular_area())
print(d.calcular_volumen())
