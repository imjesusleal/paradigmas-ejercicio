class MiddleLengthError(Exception):
    pass

def find_index(lista, idx):
    if idx == len(lista) // 2:
        raise MiddleLengthError("No se puede acceder al indice en la mitad de la lista.")
    return lista[idx]

try:
    lista = [1,2,3,4,5,6,7,8]
    find_index(lista, 4)
except MiddleLengthError as err:
    print(err)