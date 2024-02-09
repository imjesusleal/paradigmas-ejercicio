'''
FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de
abstracción y crear un método muestre información específica de la
figura utilizando polimorfismo. Luego, crear una lista de figuras
geométricas de diferentes tipos y utilizar el polimorfismo para imprimir
su información.
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

    def __repr__(self):
        return f'{self.__class__.__name__}'


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
    

lista_geometria = [Circulo(5), Triangulo(3, 4), Rectangulo(5,5)]

for i in lista_geometria:
    print(f'Clase de figura: {i}, Perimetro: {i.perimetro}')
    print(f'Clase de figura: {i}, Area: {i.area}')

    if isinstance(i, Circulo) == True:
        print(f'Diametro del circulo: {i.diametro}')

    if isinstance(i, Triangulo) == True:
        print(f'Hipotenusa del triangulo: {i.hipotenusa} ')