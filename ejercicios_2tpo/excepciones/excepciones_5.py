'''
Crea un diccionario y luego intenta acceder a un valor utilizando
una clave que no está en el diccionario. Utiliza un bloque try y
except para manejar la excepción que se produce si la clave no
existe.
'''

dicc = {"a": 1, "b": 2}

try:
    dicc["c"]
except KeyError as err:
    print(f"No se pudo acceder a la llave dada, se encontro el error: {err}")