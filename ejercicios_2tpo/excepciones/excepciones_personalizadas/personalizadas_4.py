'''
Escribe un programa que intente abrir un archivo que no existe y
utilice un bloque try y except para manejar la excepción de
"FileNotFoundError"
'''

class TxtFileError(Exception):
    pass

def file_handler(file):
    if file.endswith('.txt'):
        raise TxtFileError("No se pueden abrir archivos de tipo txt")
    return open(file, 'r')

try:
    file_handler('archivo.txt')
except TxtFileError as err:
    print(err)