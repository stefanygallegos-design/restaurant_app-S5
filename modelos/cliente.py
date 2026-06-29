class Cliente:
    """
    Clase que representa un cliente del restaurante.
    """

    def __init__(
        self,
        nombre: str,
        correo: str,
        edad: int,
        miembro_vip: bool
    ):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.miembro_vip = miembro_vip

    def mostrar_informacion(self) -> str:
        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def __str__(self) -> str:
        return (
            f"{self.nombre} "
            f"({self.edad} años)"
        )
