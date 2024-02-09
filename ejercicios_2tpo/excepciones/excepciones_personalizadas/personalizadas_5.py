'''
Crea un diccionario y luego intenta acceder a un valor utilizando
una clave que no está en el diccionario. Utiliza un bloque try y
except para manejar la excepción que se produce si la clave no
existe.
'''

class KeyStringError(Exception):
    pass
        
def check_dic(dict, key):
    if isinstance(key, str):
        del dict[key]
        raise KeyStringError("No se aceptan las llaves de tipo string")
    return dict[key]

try:
    dicc = {"a":1, "b":2}
    check_dic(dicc, "a")
except KeyStringError as err:
    print(err)