'''
Escribe un programa que abra un archivo de texto, cuente cuántas
palabras contiene y muestre el resultado en la pantalla
'''

with open('loquesea.txt', 'r') as f:
    count = 0
    for linea in f:
        words = linea.split()
        count += len(words)

print(count)

    





