'''
Sistema de Comercio Electrónico
Diseña un sistema de comercio electrónico para una tienda en línea. Debes
implementar las siguientes clases:
Producto: Una clase que representa un producto con atributos como nombre,
precio, cantidad en stock, etc.
CarritoCompra: Una clase que representa el carrito de compras de un cliente.
Debe permitir agregar, eliminar y calcular el total de los productos en el carrito.
Cliente: Una clase que representa a un cliente con atributos como nombre,
dirección, carrito de compra, etc.
Crea instancias de estas clases y demuestra cómo un cliente puede agregar
productos a su carrito, realizar una compra y calcular el total.
'''

import datetime
from dateutil.relativedelta import relativedelta

class Producto:

    CATEGORIAS = ['Hombre', 'Mujer', 'Mixta', 'Niños']


    def __init__(self, nombre: str, precio: float, stock: int | float, categoria: str, perecedero: bool = None):
        self.nombre = nombre.capitalize()
        self._precio = precio if self.__validate_precio(precio) else None
        self._stock = stock if self.__validate_stock(stock) else None
        self._categoria = categoria if self.__validate_categoria(categoria.capitalize()) else None
        self.perecedero = perecedero

        if self.perecedero == True:
            self._creation = self.__creation_date()
            if not getattr(self, '_creation', None):
                setattr(self, '_creation', self.__creation_date())

            if not getattr(self, '_expiration', None):
                setattr(self, '_expiration', self.__expiration_date())

    @property
    def precio(self):
        return self._precio
    
    @property
    def stock(self):
        return self._stock
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def creation_date(self):
        return self._creation
    
    @property
    def expiration_date(self):
        return self._expiration
    
    def __validate_stock(self, stock: int) -> tuple[int, bool]:
        valid_stock = False
        if stock > 0:
            valid_stock = True
        return stock, valid_stock
    
    def __validate_precio(self, precio: float) -> tuple[float, bool]:
        valid_precio = False
        if precio > 0:
            valid_precio = True
        return precio, valid_precio
    
    def __validate_categoria(self, categoria: str) -> tuple[str, bool]:
        valid_categoria = False
        if categoria in self.CATEGORIAS:
            valid_categoria = True
        return categoria, valid_categoria

    def incrementar_stock(self, incremento: int):
        self.stock += incremento

    def cambiar_precio(self, precio: float): 
        self.precio = precio
    
    def __creation_date(self) -> datetime:
        creation = datetime.date.today()
        return creation
    
    def __expiration_date(self):
        expiration = self.creation_date + relativedelta(months=+3)
        return expiration

    def __repr__(self):
        return f'{self.nombre}'

class CarritoCompra:
    """Clase que se instancia y compone de Producto de dos maneras: solo un Producto o una lista de Productos."""
    def __init__(self, productos: list[Producto] | Producto):
        self._productos = productos if self.__validate_producto(productos) else None

    @property
    def productos(self):
        return self._productos

    def __validate_producto(self, productos: Producto | list[Producto]) -> tuple[Producto | list[Producto], bool]:
        """Fuerza el uso de solo los tipos adminitos. 
        Si los objetos instanciados son de tipo Producto o de tipo lista[Productos] se instancia la clase."""
        valid_producto = False
        if not isinstance(productos, (Producto, list)):
            raise ValueError("Este atributo necesita ser de tipo Producto o una lista de Productos") 
        else: 
            valid_producto = True
        return productos, valid_producto

    def __check_type(self) -> bool:
        if type(self.productos) != list:
            return True
        else:
            return False

    def add_productos(self, nuevo_producto: list[Producto] | Producto):
        """Añade productos a la instancia. Admite Productos o lista[Productos].
        Verifica primero el estado de self.productos: si type(self.productos) == Producto
        crea una lista guardando el unico producto que tiene. Si type(self.productos) == list
        apendea los productos añadidos. 
        
        Si se añade solo un Producto, se apendea a self.productos directamente, de lo contario
        se recorre nuevo_producto y se apendea cada uno de sus elementos."""
        if self.__check_type():
            if self.productos != None:
                self.productos = list(self.productos)
            else:
                self._productos = list()
        if type(nuevo_producto) == list:
            for prod in nuevo_producto:
                self.productos.append(prod)
        else:           
                self.productos.append(nuevo_producto)

    def remove_producto(self, nombre_producto: str):
        """Remueve un producto pasandole el nombre del producto"""
        if type(self.productos) == list:
            for producto in self.productos:
                if nombre_producto in producto.__dict__.values():
                    self.productos.remove(producto)
                    break
        else:
            setattr(self, '_productos', None)
    

    def clear_products(self):
        """Limpia la lista de productos en el carrito de compras. 
        Si self.productos no es una lista, simplemente elimina el objeto encontrado"""
        if type(self.productos) == list:
            self.productos.clear()
        else:
            setattr(self, '_productos', None)
    
    def count_products(self) -> int:
        """Devuelve el tamaño del carrito de productos."""
        if type(self.productos) == list:
            return len(self.productos)
        else:
            return 1
        
    def total_price(self) -> float:
        """Devuelve el precio total actual del carrito de compras."""
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total


class Cliente:
    """Clase que se instancia y compone a CarritoCompra. Admite solo un tipo de dato en composición: instancia de tipo CarritoCompra"""
    def __init__(self, nombre: str, edad: int, direccion: str, compra: CarritoCompra):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion.capitalize()
        self._compra = compra if self.__validate_compra(compra) else None

    @property
    def compra(self):
        return self._compra
    
    def __validate_compra(self, compra: CarritoCompra) -> tuple[CarritoCompra, bool]:
        valid_compra = False
        if not isinstance(compra, CarritoCompra):
            raise ValueError("Este atributo necesita ser de tipo CarritoCompra")
        else:
            valid_compra = True
        return compra, valid_compra
    
    

mesa = Producto('mesa', 10000, 10, 'mixta')
silla = Producto('silla', 5000, 10, 'mixta')
lista: list[Producto] = [mesa, silla]
print(lista)
compra = CarritoCompra(lista.copy())
print(compra.productos)
compra.add_productos(mesa)
print(compra.productos)

print(compra.total_price())
compra.remove_producto('Silla')
print(compra.productos)

cliente1 = Cliente('jesus', 28, "argentina", compra)
print("Aca inicia")
print(cliente1.compra.productos)
cliente1.compra.add_productos(lista)
print(cliente1.compra.productos)
cliente1.compra.add_productos(silla)
print(cliente1.compra.productos)
print(cliente1.compra.count_products())
print(cliente1.compra.productos)
cliente1.compra.remove_producto('Mesa')
print(cliente1.compra.productos)
cliente1.compra.add_productos(lista)
print(cliente1.compra.productos)
cliente1.compra.add_productos(lista)
print(cliente1.compra.productos)
print(cliente1.compra.total_price())

compra2 = CarritoCompra(mesa)
cliente2 = Cliente('clara', 28, 'argentina', compra2)
print("arranca")
print(cliente2.compra.productos)
cliente2.compra.remove_producto('Mesa')
print(cliente2.compra.productos)
cliente2.compra.add_productos(mesa)
print(cliente2.compra.productos)
cliente2.compra.add_productos(lista.copy())
print(cliente2.compra.productos)