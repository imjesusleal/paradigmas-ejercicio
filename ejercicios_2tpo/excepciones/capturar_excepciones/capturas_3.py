
class StringCastingError(Exception):
    pass

def ask_string():
    input_choice = input("Inserta un numero:\n") 
    if input_choice != int:
        raise StringCastingError("No se puede castear el valor a un entero.")
    return input_choice
try:
    ask_string()
except StringCastingError as err:
    print(err) 