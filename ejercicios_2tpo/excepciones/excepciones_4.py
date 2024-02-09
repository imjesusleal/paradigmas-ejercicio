'''
Escribe un programa que intente abrir un archivo que no existe y
utilice un bloque try y except para manejar la excepción de
"FileNotFoundError".
'''

try:
    open('archivo.txt', 'r')
except FileNotFoundError as err:
    print(f"No se pudo abrir el archivo, se encontro el error: {err}")