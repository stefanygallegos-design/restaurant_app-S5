class Restaurante:
    """
    Clase que administra los productos y clientes.
    """

    def __init__(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto) -> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente) -> None:
        self.clientes.append(cliente)

    def mostrar_productos(self) -> None:
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self) -> None:
        for cliente in self.clientes:
            print(cliente)
