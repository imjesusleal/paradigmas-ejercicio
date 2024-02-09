class TwoDivisionError(Exception):
    pass

def division(a,b):
    if b == 2:
        raise TwoDivisionError("No se puede dividir por 2")
    return a / b

try:
    division(5,2)
except TwoDivisionError as err:
    print(err)


