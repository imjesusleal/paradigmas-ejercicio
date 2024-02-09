'''
Vehiculo: Implementar las clases Vehiculo, Coche, Motocicleta y
Bicicleta. La clase Vehiculo debe tener propiedades como marca,
modelo y velocidad_maxima. Cada subclase debe definir sus métodos y
atributos específicos relacionados con el comportamiento de cada tipo
de vehículo.
'''

from abc import ABC, abstractmethod
import time


class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0
        self.velocidad_final = 0
        self.encendido = False

    def encender(self):
        self.encendido = True

    def arrancar(self):
        self.init_time = time.time()

    @abstractmethod
    def calcular_acelaracion(self):
        pass

    @abstractmethod
    def acelerar(self, velocidad, aumento_velocidad = None):
        pass

    def frenar(self):
        self.brake_time = time.time()

    @abstractmethod
    def mostrar_datos(self):
        pass

class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, velocidad_maxima: int, puertas: int):
        super().__init__(marca, modelo, velocidad_maxima)
        self.puertas = puertas

        
    def acelerar(self, velocidad_inicial):
        return f'Aceleracion es igual a '

    def arrancar(self):
        if self.encendido == False:
            self.encender()
            return f'El carro se ha encendido y ha arrancado'
        else: 
            return f'El carro ya estaba encendido y ha arrancado'