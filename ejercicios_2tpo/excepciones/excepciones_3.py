'''
Solicita al usuario que ingrese una cadena que represente un
número. Utiliza un bloque try y except para manejar la excepción
que se produce si la cadena no se puede convertir a un número
'''

input_choice = input("Ingresa un numero:\n")

try:
    int(input_choice)
except ValueError as err:
    print(f"No se pudo transformar el input ingresado, se encontro el error: {err}")