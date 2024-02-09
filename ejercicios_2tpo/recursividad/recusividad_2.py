'''
Escribe una función recursiva para calcular el MCD de dos números
enteros
'''

def mcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return mcd(num2, num1 % num2)


print(mcd(48, 12))
    

