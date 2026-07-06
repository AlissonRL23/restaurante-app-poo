from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, calorias):
        super().__init__(nombre, precio)
        self.calorias = calorias

    def mostrar_informacion(self):
        return f"Platillo: {self.nombre} | Precio: ${self.obtener_precio()} | Calorías: {self.calorias}"
