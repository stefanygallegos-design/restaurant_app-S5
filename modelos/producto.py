class Producto:
    """
    Clase que representa un producto del restaurante.
    """

    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int,
        disponible: bool
    ):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    def mostrar_informacion(self) -> str:
        return (
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )

    def __str__(self) -> str:
        return (
            f"{self.nombre} "
            f"(${self.precio:.2f}) "
            f"- Stock: {self.stock}"
        )
