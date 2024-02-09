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