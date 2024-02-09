
class ReadCode:
    def __init__(self, codeblock):
        self.codeblock = codeblock

    def __enter__(self):
        print('Entrando al bloque de codigo')
        return self
        
    def exec_code(self, *args, **kwargs):
        if hasattr(self.codeblock, '__call__'):
            return self.codeblock(*args, **kwargs)
        else: 
            return self.codeblock

    def __exit__(self, type, value, traceback):
        print("Saliendo del bloque de codigo")
    
def sum(a,b):
    return a+b

def rest(a,b):
    return a-b

with ReadCode(sum) as code:
    print('Ejecutando bloque de codigo dentro del administrador')
    print(code.codeblock.__name__,code.exec_code(5,5))

with ReadCode(rest) as code:
    print(code.codeblock.__name__, code.exec_code(6,5))