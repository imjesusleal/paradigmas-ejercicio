'''
Sistema de Gestión de Personal
Diseña un sistema de gestión de personal para una empresa. Debes
implementar las siguientes clases:
Persona: Una clase base que representa a una persona con atributos como
nombre, edad y DNI. Utiliza el encapsulamiento para proteger los datos
sensibles.
Empleado: Una subclase de Persona que agrega atributos como salario y
cargo. Implementa el cálculo del salario en base al cargo y permite consultar el
salario.
Gerente: Una subclase de Empleado que agrega atributos específicos de un
gerente, como departamento.
Departamento: Una clase que contiene una lista de empleados y métodos
para agregar, eliminar y consultar empleados.
Crea instancias de estas clases y demuestra cómo agregar empleados a un
departamento, calcular salarios y acceder a la información de las personas
'''


## REHACER!!

from abc import ABC, abstractmethod
import itertools


class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, edad: int, dni: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._dni = dni if self.__validate_dni(dni) else None

    @property
    def dni(self):
        return self._dni
    
    def __validate_dni(self, dni: int) -> tuple[int,bool]:
        valid_dni = False
        if isinstance(dni, int) and dni > 0:
            valid_dni = True
        return dni, valid_dni
            
    def aumentar_edad(self):
        self.edad += 1


class Empleado(Persona):
    
    RANGO_SALARIAL = (30000,120000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni)
        self._salario = salario if self.__validate_salario(salario) else None

    @property
    def salario(self):
        return self._salario
    
    def __validate_salario(self, salario: int | float) -> tuple[int | float, bool]:
        valid_salario = False
        if isinstance(salario, (int,float)) and salario in self.RANGO_SALARIAL:
            valid_salario = True
        return salario, valid_salario

    def aumentar_salario(self, aumento: float | int):
        if isinstance(aumento, (int, float)):
            value = sum((self._salario, aumento))
            if value >= self.RANGO_SALARIAL[0] and value <= self.RANGO_SALARIAL[1]:
                self._salario = value
            else:
                raise ValueError(f"No se puede exceder el rango salarial del tipo de {type(self)}.")
    
    def __repr__(self) -> str:
        return f'{self.nombre} {self.apellido}'


class EmpleadoIT(Empleado):

    RANGO_SALARIAL = (40000,90000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni, salario)

    
class EmpleadoRRHH(Empleado):
    
    RANGO_SALARIAL = (30000,80000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni, salario)

class EmpleadoContable(Empleado):
    
    RANGO_SALARIAL = (40000,80000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni, salario)

class Gerente(Empleado):
    
    RANGO_SALARIAL = (70000,120000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni, salario)


class GerenteIT(Gerente):
    
    RANGO_SALARIAL = (100000,120000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni, salario)
        self.departamento = DepartamentoIT

class GerenteRRHH(Gerente):
    
    RANGO_SALARIAL = (80000,120000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni, salario)
        self.departamento = DepartamentoRRHH


class GerenteContable(Gerente):
    
    RANGO_SALARIAL = (90000,120000)

    def __init__(self, nombre: str, apellido: str, edad: int, dni: int, salario: int | float):
        super().__init__(nombre, apellido, edad, dni, salario)
        self.departamento = DepartamentoContable

class Departamento(ABC):

    def check_employee(self, employee:Empleado):
            if isinstance(employee, EmpleadoIT):
                return employee   
            if isinstance(employee, EmpleadoRRHH):
                return employee
            if isinstance(employee, EmpleadoContable):
                return employee
                
class DepartamentoIT(Departamento):

    CANTIDAD_EMPLEADOS = {}

    def __init__(self, empleado: Empleado):
        self._empleado = empleado if self.__check_employee(empleado) else None 
        self.ids = itertools.count(1) if self.__create_id(itertools.count(1)) else None

    def __check_employee(self, employee: Empleado):
        return super().check_employee(employee)

    def __create_id(self, id):
        if len(self.CANTIDAD_EMPLEADOS) == 0:
            self.CANTIDAD_EMPLEADOS[next(id)] = self._empleado
        else:
            id = len(self.CANTIDAD_EMPLEADOS) + 1
            self.CANTIDAD_EMPLEADOS[id] = self._empleado

class DepartamentoRRHH(Departamento):

    CANTIDAD_EMPLEADOS = {}

    def __init__(self, empleado: Empleado):
        self._empleado = empleado if self.__check_employee(empleado) else None 
        self.ids = itertools.count(1) if self.__create_id(itertools.count(1)) else None

    def __check_employee(self, employee: Empleado):
        return super().check_employee(employee) 
    
    def __create_id(self, id):
        if len(self.CANTIDAD_EMPLEADOS) == 0:
            self.CANTIDAD_EMPLEADOS[next(id)] = self._empleado
        else:
            id = len(self.CANTIDAD_EMPLEADOS) + 1
            self.CANTIDAD_EMPLEADOS[id] = self._empleado

class DepartamentoContable(Departamento):

    CANTIDAD_EMPLEADOS = {}

    def __init__(self, empleado: Empleado):
        self._empleado = empleado if self.__check_employee(empleado) else None 
        self.ids = itertools.count(1) if self.__create_id(itertools.count(1)) else None

    def __check_employee(self, employee: Empleado):
        return super().check_employee(employee) 
    
    def __create_id(self, id):
        if len(self.CANTIDAD_EMPLEADOS) == 0:
            self.CANTIDAD_EMPLEADOS[next(id)] = self._empleado
        else:
            id = len(self.CANTIDAD_EMPLEADOS) + 1
            self.CANTIDAD_EMPLEADOS[id] = self._empleado


if __name__ == '__main__':
    e = EmpleadoIT('jesus', 'leal', 28, 95810079, 70000)
    f = EmpleadoIT('oscar', 'leal', 31, 95810079, 70000)
    d = GerenteIT('profe', 'paradigmas', 30, 25123456, 120000)
    d.departamento = DepartamentoIT(e)
    d.departamento = DepartamentoIT(f)
    a = EmpleadoRRHH('nuevo', 'apellido', 25, 12345678, 50000)
    b = GerenteRRHH('gerente', 'rrhh', 31, 45789123, 100000)
    b.departamento = DepartamentoRRHH(a)
    c = EmpleadoContable('empleado', 'contable', 27, 17894562, 80000)
    x = GerenteContable('gerente', 'contable', 31, 54789123, 120000)
    x.departamento = DepartamentoContable(c)
    print(f"Empleados Contables | {x.departamento.CANTIDAD_EMPLEADOS}")
    print(f"Empleados RRHH | {b.departamento.CANTIDAD_EMPLEADOS}")
    print(f"Empleado IT | {d.departamento.CANTIDAD_EMPLEADOS}")
    

# from abc import ABC
# import itertools

# class Persona(ABC):

#     """Clase base abstracta. Usamos abstraccion para evitar que me la instancien. Define 
#     atributos en comunes entre todas las clases."""

#     def __init__(self, nombre: str, edad: int, dni: int):
#         self.nombre = nombre.capitalize()
#         self.edad = edad
#         self._dni = dni if self.__validate_dni(dni) else None

#     @property
#     def dni(self):
#         return self._dni
    
#     def __validate_dni(self, dni: int) -> tuple[int, bool]:
#         valid_dni = False
#         if dni > 0:
#             valid_dni = True
#         return dni, valid_dni

#     def aumentar_edad(self):
#         self.edad += 1

# class Empleado(Persona, ABC):

#     """Clase de Empleado. Define el cargo del empleado, salario y se instancia dentro de la clase Departamento para mantener
#     una base de datos de cada empleado. Define los cargos dentro de un diccionario cuyo valor es el salario."""

#     CARGOS = {'Asistente':30000,'Analista de requisitos': 40000, 
#             'Desarrollador':55000, 'Devops':60000, 'Gerente':70000}

#     def __init__(self, nombre: str, edad: int, dni: int, cargo: str):
#         super().__init__(nombre, edad, dni)
#         self._cargo = cargo.capitalize() if self.__validate_cargo else None
        
#         if not getattr(self, '_salario', None):
#             setattr(self, '_salario', self.calculate_salario())

#         if isinstance(self, Empleado) and not isinstance(self, Gerente):
#             Departamento(self)

#     @property
#     def cargo(self):
#         return self._cargo
    
#     @property
#     def salario(self):
#         return self._salario
    
#     def __validate_cargo(self, cargo: str) -> tuple[str, bool]:
#         valid_cargo = False
#         if cargo in self.CARGOS.keys():
#             valid_cargo = True
#         return cargo, valid_cargo
    
#     def calculate_salario(self) -> float:
#         return self.CARGOS[self.cargo]
    
#     def __str__(self):
#         return f'Nombre: {self.nombre}, Cargo: {self.cargo}'
    
#     def __repr__(self):
#         return f'{self.nombre} {self.dni} {self.cargo}'

# class Gerente(Empleado):

#     """Se instancia para definir funciones gerenciales. Tambien define que departamento gerencia cada instancia.
#     Se instancia dentro de Departamento para llevar control en la base de datos."""

#     DEPARTAMENTOS = ['IT', 'MARKETING', 'RRHH']

#     def __init__(self, nombre: str, edad: int, dni: int, cargo: str, departamento:str):
#         super().__init__(nombre, edad, dni, cargo)
#         self._departamento = departamento.upper() if self.__validate_departamento(departamento) else None
#         Departamento(self)
        
#     @property
#     def departamento(self):
#         return self._departamento
    
#     def __validate_departamento(self, departamento: str) -> tuple[str, bool]:
#         valid_departamento = False
#         if departamento in self.DEPARTAMENTOS:
#             valid_departamento = True
#         return departamento, valid_departamento

#     def __str__(self):
#         return f'Nombre: {self.nombre}, Cargo: {self.cargo}'
    
#     def __repr__(self):
#         return f'{self.nombre} {self.dni} {self.cargo}'

# class Departamento:

#     """Clase sin uso practico para su instanciacion, al menos que se instancie dentro de Empleado o Gerente.
#     Sirve para guardar registro de la cantidad de empleados en total que lleva el sistema, tomando en cuenta
#     si son empleados o gerentes. """
    
#     EMPLEADOS: dict = {}
#     GERENTES: dict = {}
#     id_counter = itertools.count(1)

#     def __new__(cls, obj: Empleado | Gerente):

#         """Antes de instanciarse la clase, se chequea que tipo de empleado son y se guarda dentro de un diccionario.
#         Se inicia una variable de clase id que sirve como un generador de IDs incrementales para cada uno de los empleados."""

#         cls.id = next(cls.id_counter)
#         if isinstance(obj, Empleado):
#             cls.add_empleados(obj)
#         else:
#             if isinstance(obj, Gerente):
#                 cls.add_gerente(obj)

#     @classmethod
#     def add_empleados(cls, empleado: Empleado | Gerente):
#         """Añade un empleado. Se usa primordialmente para instanciar
#         en Departamento al empleado."""
#         if isinstance(empleado, Empleado) or isinstance(empleado, Gerente):
#             cls.EMPLEADOS[cls.id] = empleado
#         else:
#             raise TypeError("No se puede instanciar")

#     @classmethod
#     def add_gerente(cls, gerente):
#         """Añade un gerente. Se usa primordialmente para instanciar
#         en Departamento al gerente."""
#         cls.GERENTES[cls.id] = gerente

#     @classmethod    
#     def del_empleados(cls, id):
#         """Elimina una empleado de la base tomando el id"""
#         cls.EMPLEADOS.pop(id)
        
#     @classmethod
#     def del_gerentes(cls, id):
#         """Elimina una gerente de la base tomando el id"""
#         cls.GERENTES.pop(id)

#     @classmethod
#     def look_empleado(cls, id) -> dict:
#         """Retorna un empleado buscando por id"""
#         return cls.EMPLEADOS[id]
    
#     @classmethod
#     def look_gerente(cls, id) -> dict:
#         """Returna un gerente buscando por id"""
#         return cls.GERENTES[id]
    
#     @classmethod
#     def look_mixed(cls):
#         """Mixed look up. Chequea ambas bases por ids y devuelve una base mezclada con 
#         Empleados y Gerentes, de manera ordenada"""
#         mixed = []
#         ids_empleados = cls.EMPLEADOS.keys() 
#         ids_gerentes = cls.GERENTES.keys()
#         for i in range(1,len(ids_empleados) + len(ids_gerentes) + 1):
#             if i in ids_empleados:
#                 mixed.append(cls.EMPLEADOS[i])
#             else:
#                 mixed.append(cls.GERENTES[i])
#         return mixed 
        
# employee = Empleado('jesus', 28, 95810079, 'asistente')
# print(employee.cargo)
# print(employee.salario)

# employee2 = Empleado('sabri', 28, 95810080, 'asistente')

# gerente = Gerente('oscar', 30, 95810098, 'gerente', 'it')
# print(gerente.salario)
# print(gerente.departamento)
# print(Departamento.GERENTES)
# print(Departamento.EMPLEADOS)
# print(Departamento.look_mixed())
# x = Departamento.look_mixed()

# for i in x:
#     print(i.nombre, i.dni, i.edad, i.cargo)


# c = EmpleadoIT('jesus', 'leal', 28, 95810079, 50000, 'Desarrollador')
# print(c.apellido)
# c.aumentar_salario(10000)
# c.aumentar_salario(10000)
# c.aumentar_salario(10000)
# c.aumentar_salario(10000)
# c.aumentar_salario(10000)
# print(c.salario)







# b = EmpleadoRRHH('jesus', 'leal', 28, 95810079, 50000, 'desarrollador')
# b.aumentar_salario(10000)
# b.aumentar_salario(10000)
# b.aumentar_salario(10000)
# b.aumentar_salario(10000)
# b.aumentar_salario(10000)
# b.aumentar_salario(10000)