'''
Escribe un programa que tome varios archivos de texto y los concatena
en un solo archivo de salida. Asegúrate de cerrar todos los archivos
correctamente.
'''

with open('loquesea.txt', 'r') as f:
    first_file = f.readlines()
    with open('new_loquesea.txt', 'r') as file_two:
        first_file += file_two.readlines()
        with open('concated_file', 'w') as new_file:
            new_file.writelines(first_file)