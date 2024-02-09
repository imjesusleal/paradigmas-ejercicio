'''
Animal: Utilizar la clase Animal del ejercicio de herencia y aplicar
polimorfismo para realizar el sonido característico del animal. Luego,
crear una lista de animales de diferentes tipos y utilizar el polimorfismo
para hacer que emiten sus sonidos.
'''

class Animal():

    SIZE: list = ['pequeño', 'mediano', 'grande']

    def __init__(self, nombre: str, edad: int, peso: float, tamaño: str):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self._tamaño = tamaño if self.validar_tamaño(tamaño) else None

    @property
    def tamaño(self) -> str:
        return self._tamaño

    @classmethod
    def validar_tamaño(cls, tamaño: str) -> str:
        if tamaño in cls.SIZE:
            return tamaño

    def comer(self) -> str:
        return f'Los animales comen'

    def moverse(self) -> str:
        return f'Los animales se mueven'

    def emitir_sonido(self) -> str:
        return f'Los animales emiten sonidos'
    
    def aumentar_edad(self) -> int:
        self.edad += 1

    def comer(self) -> str:
        if self.tamaño == 'pequeño':
            return f'Mi {self}: {self.nombre} come 3 veces al dia y cada comida es de {self.calcular_comida()} gramos.'
        elif self.tamaño == 'mediano':
            return f'Mi {self}: {self.nombre} come 2 veces al dia y cada comida es de {self.calcular_comida()} gramos.'
        elif self.tamaño == 'grande':
            return f'Mi {self}: {self.nombre} como 1 vez al dia y cad comida es de {self.calcular_comida()} gramos'
    
    def __repr__(self):
        return f'{self.__class__.__name__}'


class Perro(Animal):
    def __init__(self, nombre: str, edad: int, peso: float, tamaño:str):
        super().__init__(nombre, edad, peso, tamaño)
    
    def moverse(self) -> str:
        return f'Mi perro, {self.nombre} corre y salta.'
    
    def emitir_sonido(self) -> str:
        return f'Mi perro, {self.nombre} aulla en las noches de luna llena.'
    
    def calcular_comida(self) -> float:
        if self.tamaño == 'pequeño':
            return (self.peso * 2.5) / 100
        elif self.tamaño == 'mediano':
            return (self.peso * 4) / 100
        else:
            return (self.peso * 6) / 100


class Gato(Animal):
    def __init__(self, nombre:str, edad:int, peso:float, tamaño:str):
        super().__init__(nombre, edad, peso, tamaño)

    def moverse(self) -> str:
        return f'Mi gato, {self.nombre} corre y salta.'
    
    def emitir_sonido(self) -> str:
        return f'Mi gato, {self.nombre} maulla.'
    
    def calcular_comida(self) -> float:
        if self.tamaño == 'pequeño':
            return (self.peso * 1) / 100
        elif self.tamaño == 'mediano':
            return (self.peso * 2) / 100
        else:
            return (self.peso * 3) / 100

class Pajaro(Animal):
    def __init__(self, nombre:str, edad:int, peso:float, tamaño:str):
        super().__init__(nombre, edad, peso, tamaño)

    def moverse(self):
        return f'Mi pajaro, {self.nombre} vuela con sus alas'
    
    def emitir_sonido(self):
        return f'Mi pajaro, {self.nombre} canta todos los dias.'
    
    def calcular_comida(self) -> float:
        if self.tamaño == 'pequeño':
            return (self.peso * 1) / 100
        elif self.tamaño == 'mediano':
            return (self.peso * 2) / 100
        else:
            return (self.peso * 3) / 100
        

animales = [Perro('Annie', 1, 4.5, 'pequeño'), Gato('Momo', 1, 4, "mediano"), Pajaro("Birdie", 1, 2, "pequeño")]

for animal in animales:
    print(animal.emitir_sonido())