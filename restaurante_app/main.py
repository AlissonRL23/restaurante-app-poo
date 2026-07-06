from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():

    restaurante = Restaurante()

    platillo1 = Platillo("Hamburguesa", 6.50, 850)
    platillo2 = Platillo("Pizza", 8.00, 950)

    bebida1 = Bebida("Coca Cola", 2.00, 500)
    bebida2 = Bebida("Jugo de Naranja", 2.50, 400)

    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    restaurante.mostrar_productos()


if __name__ == "__main__":
    main()
