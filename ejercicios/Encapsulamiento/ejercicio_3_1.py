'''
CuentaBancaria: Crear la clase CuentaBancaria con atributos privados y
públicos para el saldo y titular. Definir métodos para depositar, retirar y
consultar el saldo de la cuenta
'''

class CuentaBancaria():
    def __init__(self, titular:str, saldo: float = None):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo        

    def depositar(self, deposito: float) -> float:
        if self.saldo == None:
            self._saldo = deposito
        else:
            self._saldo += deposito
    
    def retiro(self, retiro: float) -> float:
        if self.saldo > 0:
            self.saldo -= retiro

alberto = CuentaBancaria('Alberto')
alberto.depositar(10000)
print(alberto.saldo)
