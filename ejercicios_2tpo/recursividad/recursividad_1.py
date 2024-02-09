'''
Escribe una función recursiva para encontrar y sumar todos los números
primos desde 1 hasta un número deseado
'''


def prime_numbers(final, start=1):
    if start > final:
        return 0
    if start <= 1:
        return prime_numbers(final, start+1)
    for i in range(2, int(start**0.5+1)):
        if start % i == 0:
            return prime_numbers(final, start+1)
    return start + prime_numbers(final, start+1)

print(prime_numbers(5))


    