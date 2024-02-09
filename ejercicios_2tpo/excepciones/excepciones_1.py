'''
Escribe un programa que solicite al usuario dos números y realice
la división de uno por el otro. Utiliza un bloque try y except para
manejar la excepción que ocurre si el segundo número es cero
'''

def division(a,b):
    return a / b
    
try:        
    division(5,0)
except ZeroDivisionError as err:
    print("Error stopped execution:", err)
