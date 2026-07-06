from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, volumen):
        super().__init__(nombre, precio)
        self.volumen = volumen

    def mostrar_informacion(self):
        return f"Bebida: {self.nombre} | Precio: ${self.obtener_precio()} | Volumen: {self.volumen} ml"
