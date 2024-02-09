'''
Coche: Crear la clase Coche con atributos privados y/o públicos según
corresponda de velocidad y kilometraje. Definir métodos públicos para
acelerar y registrar el kilometraje de manera segura.
'''
import time, timeit, math

class Coche:
    def __init__(self, velocidad: float, kilometraje: float):
        self.velocidad = velocidad
        self._kilometraje = kilometraje if self.validar_kilometraje(kilometraje) else None
        self.tiempo = 0.0
    
    @property
    def kilometraje(self):
        return self._kilometraje
    
    def validar_kilometraje(self, kilometraje):
        kilometraje_valido = False 
        if kilometraje > self.velocidad:
            kilometraje_valido = True
        else:
            raise ValueError("La velocidad no puede ser mayor al kilometraje del auto.")
        return kilometraje_valido, kilometraje

    def __frenar(self, inicio):
        final = math.ceil(timeit.default_timer() - inicio)
        return final, True
    
    def arrancar(self):
        inicio = timeit.default_timer()
        yield inicio
        
    def acelerar(self, frenar = None):
        inicio = self.arrancar()
        if frenar == True:
            final, _ = self.__frenar(next(inicio))
            return f'El auto viaja a: {abs(self.velocidad / final)} m/s.'
        
        
carro = Coche(240, 250)
print(carro.kilometraje)
carro.acelerar()
carro.acelerar()
print(carro.acelerar(frenar = True))
