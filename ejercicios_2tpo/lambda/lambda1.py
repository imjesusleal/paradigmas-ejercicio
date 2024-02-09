import math

'''
Dada una lista de números, utiliza map y una función lambda para crear
una nueva lista que contenga el doble de cada número.
'''
# lista = [1,2,3,4,5,6]
# print(list(map(lambda x: x*2, lista)))

'''
Toma una lista de cadenas y utiliza map con una función lambda para
convertir todas las cadenas en mayúsculas.
'''

# lista = ['hola', 'como', 'estas']
# print(list(map(lambda x: x.upper() , lista)))

'''
Dada una lista de cadenas, utiliza map y una función lambda para crear
una lista con la longitud de cada palabra.
'''

# lista = ["hola", 'como', 'estas']
# print(list(map(lambda x: [*x], lista)))

'''
Toma una lista de números y utiliza map con una función lambda para
calcular la raíz cuadrada de cada número.
'''

lista = [2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: math.sqrt(x), lista)))