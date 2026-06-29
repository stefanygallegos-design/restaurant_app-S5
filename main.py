from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    # Crear productos
    producto1 = Producto(
        "Hamburguesa Clásica",
        "Comida",
        6.50,
        30,
        True
    )

    producto2 = Producto(
        "Jugo Natural",
        "Bebida",
        2.75,
        20,
        True
    )

    # Crear clientes
    cliente1 = Cliente(
        "María López",
        "maria@gmail.com",
        24,
        True
    )

    cliente2 = Cliente(
        "Carlos Pérez",
        "carlos@gmail.com",
        31,
        False
    )

    # Crear restaurante
    restaurante = Restaurante()

    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    print("===== PRODUCTOS =====")
    restaurante.mostrar_productos()

    print("\n===== CLIENTES =====")
    restaurante.mostrar_clientes()


if __name__ == "__main__":
    main()
