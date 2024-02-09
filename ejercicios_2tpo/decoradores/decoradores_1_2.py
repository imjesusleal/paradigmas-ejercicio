"""Una manera de hacer esto es como el profe habia mandado chequeando elemento por elemento
en la variable '*args' pero en este caso como solo queremos sumar valores de tipo enteros, podemos
chequearlos todos en una misma linea con all() creando dentro un bucle que itere dentro de los argumentos,
nos devuelve true si todos son enteros y por ende se ejecuta la función, de lo contrario levanta una excepcion."""

def arg_validation(data_type):
    def _arg_validation(func):
        def wrapper(*args, **kwargs):
            if not all(isinstance(a, data_type) for a in args):
                raise TypeError("Needs to be of the same type")
            result = func(*args,**kwargs)
            return result
        return wrapper
    return _arg_validation

@arg_validation(int)
def sum(a,b):
    return a+b

print(sum(1.5,1))