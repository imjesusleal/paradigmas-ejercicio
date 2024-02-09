'''
Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las
clases deben contener atributos como color y dimensiones. Las
subclases deben heredar y definir métodos y atributos para calcular el
área y el perímetro de cada forma
'''

from math import sqrt
from abc import ABC

class Forma(ABC):

    PI = 3.1416

    def __init__(self, color: str, dimensiones = None):
        self.color = color
        self._dimensiones = dimensiones if self.validar_dimensiones(dimensiones) else None

    @property
    def dimensiones(self):
        return self._dimensiones
    
    def validar_dimensiones(self, dimensiones):
        dimensiones_validas = False
        if dimensiones >= 2:
            dimensiones_validas = True
            return dimensiones, dimensiones_validas
        else: 
            raise ValueError(f'Una forma no puede tener {dimensiones} dimensiones.')

class FormaPlana(Forma, ABC):
    def __init__(self, color: str):
            super().__init__(color, dimensiones=2)

class FormaEspacial(Forma, ABC):
    def __init__(self, color, *args, **kwargs):
        super().__init__(color, dimensiones=3)
        
class Circulo(FormaPlana):
    """Siempre se va a crear como una clase que hereda de FiguraPlana"""

    def __init__(self, color: str, radio: float):
        super().__init__(color)
        self.radio = radio
        if not getattr(self, 'diametro', None):
            setattr(self,'diametro', self.calcular_diametro())

    def calcular_diametro(self) -> float:
        if self.radio > 0:
            return self.radio ** 2

    def calcular_petrimetro(self) -> float:
        return 2 * self.PI * self.radio
    
    def calcular_area(self) -> float:
        return self.PI * self.diametro

class Triangulo(FormaPlana):
    """Siempre se va a crear como una clase que hereda de FiguraPlana."""
    def __init__(self, color: str, cateto_A: float = None, cateto_B: float = None, hipotenusa: float = None):
        super().__init__(color)
        self.cateto_A = cateto_A
        self.cateto_B = cateto_B
        self.hipotenusa = hipotenusa   

    def calcular_hipotenusa(self) -> float:
        """Calcula al hipotenusa suponiendo que poseemos el valor de los dos catetos."""
        if self.cateto_A  != None and self.cateto_B != None:
            self.hipotenusa = sqrt((self.cateto_A**2) + (self.cateto_B**2))
        else: 
            raise ValueError("No hay suficiente información para calcular la hipotenusa")
        
    def calcular_cateto(self) -> float:
        """Calcula un cateto suponiendo que tenemos la hipotenusa y alguno de los catetos."""
        if self.hipotenusa != None and self.cateto_A != None:
            self.cateto_B = sqrt((self.hipotenusa**2) - (self.cateto_A**2))
        elif self.hipotenusa != None and self.cateto_B != None:
            self.cateto_A = sqrt((self.hipotenusa**2) - (self.cateto_B**2))

    def calcular_altura(self, base) -> float:
        """Chequea con respecto al parametro base cual de los dos catetos es la base y calcula la altura. Setea la base 
        con respecto a el match usado."""
        match base:
            case "cateto_A":
                setattr(self, 'altura', sqrt((self.hipotenusa**2) - (self.cateto_B**2)))
                setattr(self, 'base', self.cateto_A)
            case "cateto_B":
                setattr(self, 'altura', sqrt((self.hipotenusa**2) - (self.cateto_A**2)))
                setattr(self, 'base', self.cateto_B)
        return self.altura

    def calcular_area(self) -> float:
        return self.base * self.altura
    
class Esfera(Circulo, FormaEspacial):
    def __init__(self, color: str, radio: float):
        super().__init__(color, radio)
        self.radio = radio

    def calcular_volumen(self):
        vol = self.radio **3
        return 4/3 * self.PI * vol
    
    def calcular_area(self):
        return 4 * self.PI * (self.radio**2)
    
c = Esfera('negro', 3)
print(c.calcular_diametro())
print(c.calcular_volumen())
print(c.calcular_area())