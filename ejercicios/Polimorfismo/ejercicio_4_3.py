'''
Empleado: Utilizar la clase Empleado del ejercicio de herencia y aplicar
polimorfismo para calcular el salario de acuerdo con las reglas
específicas de cada tipo de empleado. Luego, crear una lista de
empleados de diferentes tipos y utilizar el polimorfismo para calcular
sus salarios
'''

class Empleado:

    """
    La clase base. Controla la creación de cada Empleado (incluyendo sus clases hijos) y guarda los records de 
    todas las instancias en un diccionario."""

    ID_MAP: dict[int, object] = {}
    DEPARTAMENTOS: list[str] = ['Marketing', 'IT', 'RRHH']

    def __init__(self, nombre: str, apellido: str, salario: float, departamento: str,  id: int):
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self._salario = salario if self.validate_salario(salario) else None
        self._departamento = departamento if self.validate_departamento(departamento) else None
        self._id = id if self.set_id(id) else None

    @property
    def id(self):
        return self._id
    
    @property
    def salario(self):
        return self._salario
    
    @property
    def departamento(self):
        return self._departamento
    
    def validate_salario(self, salario: float) -> tuple[bool, float]:
        salario_validado = False
        if salario > 0:
            salario_validado = True
        return salario_validado, salario
    
    def actualizar_salario(self, salario: float) -> tuple[bool, float]:
        salario_validado = False
        if self.validate_salario(salario):
            salario_validado = True
            self._salario = salario
        return salario_validado, self._salario

    def set_id(self, id: int) -> tuple[bool, int]:
        """Chequea si el id ingresado para el Empleado es valido. 
        El control de validez se realiza en función de numeros enteros. 
        Si el numero entero ya existe en ID_MAP rechaza la creación de la instancia."""
        valid_id = False
        ids = self.ID_MAP.keys()
        if len(self.ID_MAP) > 0: 
            if id in ids:
                raise ValueError("ID already being used by another employee")
            else:
                valid_id = True
                self.ID_MAP[id] = self
        else:
                self.ID_MAP[id] = self

        return valid_id, id
    
    def validate_departamento(self, departamento: str) -> str:
        if departamento in self.DEPARTAMENTOS:
            self._departamento = departamento
        return self._departamento
    
    def actualizar_departamento(self, nuevo_departamento: str) -> str:
        if nuevo_departamento in self.DEPARTAMENTOS:
            self._departamento = nuevo_departamento
        return self._departamento
   
    def __repr__(self):
        return f'{self.nombre} {self.apellido}'
    
class Gerente(Empleado):
    """Clase que maneja la instanciación de los Gerentes, permite agregar personal del departamento que maneja."""
    def __init__(self, nombre, apellido, salario, departamento, id):
        super().__init__(nombre, apellido, salario, departamento,id)
        self._salario = salario if self.validate_departamento(salario) else None
        if not (getattr(self, '_personal', {})):
            setattr(self, '_personal', {})

    def validate_salario(self, salario: float) -> tuple[float, bool]:
        salario_valido = False
        if salario < 50000:
            raise ValueError("El salario de Gerente no puede ser menor a 50000")
        else:
            salario_valido = True
            return salario, salario_valido
        
    @property
    def personal(self):
        """Retorna la cantidad de personal a cargo del Gerente del Departamento.
        Debido a esto, el parametro departamento es obligatorio, para poder contar empleados por departamento."""
        return self._personal 

    def __add_personal(self, id, personal: object):
        self._personal[id] = personal
    
    def validate_personal(self, id: int, departamento: str) -> tuple[bool, int]:
        """Validación del personal asignado. Verificamos si el departamento del gerente y el empleado es el mismo. 
        Luego verifica que el id del empleado este en nuestro mapeo de empleados y compara que el departamento sea el mismo."""
        personal_validado = False
        ids = self.ID_MAP.keys()
        if self.departamento == departamento and not isinstance(self.ID_MAP[id], Gerente):
            if (id in ids) and (departamento == self.ID_MAP[id].departamento):
                personal_validado = True
                self.__add_personal(id, self.ID_MAP[id])
            else:
                raise TypeError('Cannot assigned a employee to a manager of another department')
        return personal_validado, self._personal

    def despedir_personal(self, id: int):
        """El gerente puede despedir solo a los empleados bajo su cargo."""
        ids = self.personal.keys()
        if id in ids:
            del self.personal[id]


class Trabajador(Empleado):
    """Logica a implementar. Trabajador que hereda de Empleado"""
    def __init__(self, nombre, apellido, salario, departamento, id):
        super().__init__(nombre, apellido, salario,departamento, id)
        self._salario = salario if self.validate_salario(salario) else None
    
    def validate_salario(self, salario: float) -> tuple[float, bool]:
        salario_valido = False
        if salario > 50000:
            raise ValueError("El salario de Trabajador no puede ser mayor a 50000")
        else:
            salario_valido = True
            return salario, salario_valido
        

empleados = [Gerente('jesus', 'leal', 50001, 'IT', 1), Trabajador('quien', 'sea', 40000, 'IT', 2)]

for empleado in empleados:
    print(empleado.salario)