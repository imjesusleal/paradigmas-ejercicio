'''
Imagina que estás desarrollando un sistema de gestión para una empresa de comercio electrónico. 
Tu tarea es diseñar un conjunto de clases orientadas a objetos para manejar productos, carritos de compra, 
usuarios y pedidos. 
Debes crear clases como 'Producto', 'Carrito', 'Usuario' y 'Pedido'. 
Aplica herencia para representar diferentes tipos de usuarios, como 'Cliente' y 'Administrador'. 
Utiliza la composición para gestionar la relación entre productos y carritos, y asegúrate de que el diseño sea 
escalable para futuras características del comercio electrónico.'''

from abc import ABC, abstractmethod


#Clase Abstracta, no se instancia
class Producto(ABC):
    def __init__(self, nombre: str, marca: str, precio: float):
        self. nombre = nombre
        self.marca = marca
        self._precio = precio if self.__validate_precio(precio) else None #encapsulo y valido el precio

    @property
    def precio(self):
        return self._precio

    def __validate_precio(self, precio: float):
        valid_precio = False
        if isinstance(precio, float):
            valid_precio = True
        else:
            raise TypeError("Esperaba una float")
        return valid_precio

    @abstractmethod
    def actualizar_precio(self,precio: float):
        pass
        
    def __repr__(self):
        return f'{self.nombre} {self.marca}'

#Implementa Producto
class ProductoPerecedero(Producto):

    RANGO_PRECIO = (2000,5000)

    def __init__(self, nombre: str, marca: str, precio: float, fecha_vencimiento: str):
        super().__init__(nombre, marca, precio)
        self.fecha_vencimiento = fecha_vencimiento

    def actualizar_precio(self, precio: float):
        if precio in range(self.RANGO_PRECIO[0], self.RANGO_PRECIO[1]):
            self._precio = precio

#Implementa Producto
class ProductoNoPerecedero(Producto):
    RANGO_PRECIO = (4000,7000)

    def __init__(self, nombre: str, marca: str, precio: float):
        super().__init__(nombre, marca, precio)
        
    def actualizar_precio(self, precio: float):
        if precio in range(self.RANGO_PRECIO[0], self.RANGO_PRECIO[1]):
            self._precio = precio


#Usa composicion para guardar la lista de productos
class Carrito:
    def __init__(self):
        self.__lista_productos = []    
    
    @property
    def lista_productos(self):
        return self.__lista_productos
    
    def add_producto(self, producto: Producto):
        if isinstance(producto, Producto):
            self.__lista_productos.append(producto)
        else:
            raise TypeError("No es una instancia de producto")
        
    def borrar_producto(self, producto: str):
        for item in self.__lista_productos:
            if producto.upper() == item.nombre:
                self.__lista_productos.remove(item)

#Compone todo el carrito en un pedido
class Pedido:
    def __init__(self, carrito: Carrito, direccion: str):
        self.carrito = carrito 
        self.direccion = direccion
 
#Clase base.
class Usuario:
    def __init__(self, username, contraseña):
        self.username = username
        self._contraseña = contraseña if self._validate_contraseña(contraseña) else None
    
    @property
    def contraseña(self):
        return self._contraseña
    
    def _validate_contraseña(self, contraseña):
        valid_contraseña = False
        if isinstance(contraseña, str):
            valid_contraseña = True
        return valid_contraseña 


#Extiende de usuario, compone un pedido con un carrito que compone productos
class Cliente(Usuario):
    def __init__(self, username, contraseña, metodo_pago, pedido=None | Pedido):
        super().__init__(username, contraseña)
        self.metodo_pago = metodo_pago
        self._pedido = pedido if self._validate_pedido(pedido) else None

    @property
    def pedido(self):
        return self._pedido
    
    def _validate_pedido(self, pedido: Pedido) -> bool:
        valid_pedido = False
        if isinstance(pedido, Pedido):
            valid_pedido = True
        return valid_pedido
    
    def actualizar_pedido(self, pedido: Pedido):
        if isinstance(pedido, Pedido):
            self._pedido = pedido

#Extiende de Usuario, no sabemos si funciona la logica de borrar usuarios xD
class Administrador(Usuario):
    def __init__(self, username, contraseña):
        super().__init__(username, contraseña)
        self.username = username
        self.contraseña = contraseña

    def eliminar_usuarios(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            del usuario
        else:
            raise ValueError("No existe tal usuario")

producto_1 = ProductoNoPerecedero("TV", "Phillips", 40000.00)
carrito_1 = Carrito()
carrito_1.add_producto(producto_1)
pedido_1 = Pedido(carrito_1, "French")
cliente_1 = Cliente("nadia", "123456", "visa")
cliente_1.actualizar_pedido(pedido_1)
producto_2 = ProductoNoPerecedero("PC", "Phillips", 70000.00)
cliente_1.pedido.carrito.add_producto(producto_2)
print(cliente_1.pedido.carrito.lista_productos)


#Integrantes
# Leonardo Ponce, 
# Nadia De Cinti, 
# Maria Paz Arbuco, 
# leobaldo perez, 
# Angeles Pulvet, 
# Sofia Crego, 
# Berenice Robertazzi, 
# Diego Messirlian, 
# Jesus Leal, 
# Elio Lobo