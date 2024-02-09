'''
Escribe un programa que intente abrir un archivo, leer su
contenido y luego cerrarlo. Utiliza bloques try, except y finally
para asegurarte de que el archivo se cierre correctamente,
incluso si ocurre una excepción durante la lectura.
'''

try:
    file = open('loquesea.txt', 'r')
    lines = file.read().splitlines()
    print(lines)
except FileNotFoundError as err:
    print(err)
finally:
    file.close()

