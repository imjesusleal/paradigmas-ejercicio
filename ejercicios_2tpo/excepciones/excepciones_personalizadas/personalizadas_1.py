'''
Escribe un programa que solicite al usuario dos números y realice
la división de uno por el otro. Utiliza un bloque try y except para
manejar la excepción que ocurre si el segundo número es cero
'''

class TwoDivisionError(Exception):
    pass

def division(a,b):
    if b == 2:
        raise TwoDivisionError("No se puede dividir por 2")
    return a / b

try:
    division(5,2)
except TwoDivisionError as err:
    print(err)

