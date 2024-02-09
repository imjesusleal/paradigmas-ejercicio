'''
FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo
y Triangulo y que contenga métodos y atributos relacionados con el
cálculo del área y perímetro de una figura geométrica. Definan los
métodos y atributos necesarios para calcular el área y el perímetro de
cada tipo de figura utilizando los conceptos de abstracción
'''

from abc import ABC, abstractmethod
from math import pi 

class FiguraGeometrico(ABC):        
    
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Circulo(FiguraGeometrico):
                                                                #Perimetro de un circulo es igual a pi * d
    def __init__(self, radio: float):                           #Area de un circulo es igual a pi * r^2
        self.radio = radio    

    @property 
    def diametro(self):
        return self.calcular_diametro()

    @property
    def area(self):
        return self.calcular_area()
    
    @property
    def perimetro(self):
        return self.calcular_perimetro()

    def calcular_area(self):
        return pi * (self.radio**2)

    def calcular_perimetro(self):
        return pi * self.diametro
    
    def calcular_diametro(self):
        return self.radio * 2


class Rectangulo(FiguraGeometrico):                     #Area de rectangulo es base * altura
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.calcular_area()

    @property
    def perimetro(self):
        return self.calcular_perimetro()

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2*self.base) + (2*self.altura) 

class Triangulo(FiguraGeometrico):                                      
    def __init__(self, base: float, altura: float):             #Area de rectangulo es base * altura / 2
        self.base = base                                
        self.altura = altura
    
    @property
    def hipotenusa(self):
        return self.calcular_hipotenusa()
    
    @property
    def area(self):
        return self.calcular_area()
    
    @property
    def perimetro(self):
        return self.calcular_perimetro()

    def calcular_hipotenusa(self):
        return (self.base**2) + (self.altura**2)
    
    def calcular_area(self):
        return (self.base * self.altura) / 2 
    
    def calcular_perimetro(self):
        return self.base + self.altura + self.hipotenusa
        



# c1 = Circulo(5)
# print(c1.diametro)
# print(c1.area)
# print(c1.perimetro)

# t1 = Triangulo(3, 4)
# print(t1.hipotenusa)
# print(t1.perimetro)
# print(t1.area)

# r1 = Rectangulo(5,5)
# print(r1.area)
# print(r1.perimetro)

