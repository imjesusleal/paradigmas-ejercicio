'''
Escribe un programa que abra un archivo, lea su contenido y
escriba el mismo contenido en otro archivo. Utiliza bloques try,
except y finally para manejar cualquier excepción que pueda
ocurrir durante la lectura o escritura, y asegúrate de que ambos
archivos se cierren correctamente.
'''

try:
    file = open('loquesea.txt', 'r+')
    content = file.readlines()
except FileNotFoundError as err:
    print(err)
finally:
    file.close()    

try:
    new_file = open('new_loquesea.txt', 'w')
    new_file.writelines(content)
except FileExistsError as err:
    print(err)
finally:
    new_file.close()
    

