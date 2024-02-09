'''
Escribe una función que sume los dígitos de un número pares de un
número entero. Si el número es impar, restarle 3 y sumarlo. Si el número
da negativo, sumar 1.
'''


#Lo intente hacer en un oneliner pero fracase, no me dio la cabeza
def algoritmo(numero):
    lista_num = [int(num) for num in str(numero)]
    #result = sum(number for number in num if number % 2 == 0)    
    result = 0
    for num in lista_num:
        if num % 2 == 0:
            result+=num
        elif num % 2 == 1:
            if num -3 >= 0:
                result += (num-3)
            else:
                result += 1
    return result
            

print(algoritmo(2414))
