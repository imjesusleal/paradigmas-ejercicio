'''
Escribe un programa que abra un archivo de entrada, lea su contenido y
luego escriba ese contenido en un nuevo archivo de salida. Asegúrate
de cerrar ambos archivos al final.
'''

with open('loquesea.txt', 'r') as f:
    content = f.readlines()
    with open('new_loquesea.txt', 'w') as new_f:
        new_f.writelines(content)