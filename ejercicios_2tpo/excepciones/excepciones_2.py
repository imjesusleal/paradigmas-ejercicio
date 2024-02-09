'''
Crea una lista de números y, a continuación, intenta acceder a un
elemento en un índice especificado por el usuario. Utiliza un
bloque try y except para manejar la excepción que se produce si
el índice está fuera de rango
'''

lista = [1,2,3,4,5,6,7,8,9]
input_choice = int(input("Ingresa el numero del indice que desees consultar, del uno al ocho:\n"))

try:
    print(f"El valor del indice indicado es {lista[input_choice]}")
except IndexError as err:
    print(f"El indice esta fuera del tamaño de la lista, se consiguio el error {err}")


