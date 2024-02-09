'''
Crea un programa que solicite al usuario dos números y una
operación matemática (suma, resta, multiplicación, división) para
realizar. Utiliza bloques try, except y finally para manejar cualquier
excepción que pueda ocurrir durante la operación y asegurarte
de que los recursos se liberen correctamente.
'''

def suma(*args):
    return args[0][0] + args[0][1]

def resta(*args):
    return args[0][0] - args[0][1]

def mult(*args):
    return args[0][0] * args[0][1]

def division(*args):
    return args[0][0] / args[0][1]

def ask_oper():
    list_op = ["sumar", "restar", "multiplicar", "dividir"]
    input_choice = input("Ingrese un tipo de operaciones entre estas:\nSumar\nRestar\nMultiplicar\nDividir\n\n")
    if input_choice.lower() in list_op:
        return input_choice

def ask_nums():
    num1 = input("Ingrese un numero:\n")
    num2 = input("Ingrese otro numero:\n")
    return num1, num2 


def main():

    while True:
        try:
            nums = [int(x) for x in ask_nums()]
            break
        except ValueError as err:
            print(err)
            
    try:
        oper = ask_oper()
    except ValueError as err:
        print(err)

    match oper:
        case "sumar":
            print(suma(nums))
        case "restar":
            print(resta(nums))
        case "multiplicar":
            print(mult(nums))
        case "dividir":
            try:
                print(division(nums))
            except ZeroDivisionError as err:
                print("error:",err)

main()
