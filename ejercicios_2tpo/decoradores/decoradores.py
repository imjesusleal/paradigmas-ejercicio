"""Nota para mi. Esto funciona puesto que en la definicion del decorador
leemos una sola vez el atributo 'calls' y el atributo 'args' y cuando se 
decora la funcion especifica se leen los atributos y se guarda el estado 
de esos atributos, algo como los atributos de una instancia. Cuando se ejecuta la funcion
ya no see la definicion del decorador, sino que se ejecuta directamente el cuerpo del decorador."""

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        wrapper.args += len(args)
        result = func(*args, **kwargs)
        return result
    wrapper.calls = 0
    wrapper.args = 0
    return wrapper

@count_calls
def sum(a,b):
    return a+b

print(sum(1,1))
print(sum(1,1))
print(sum(1,1))
print(sum(1,1))
print(sum.calls)
print(sum.args)