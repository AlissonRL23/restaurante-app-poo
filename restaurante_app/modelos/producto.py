class Producto:
    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.__precio = precio
        self.disponible = disponible

    def obtener_precio(self):
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.__precio} | {estado}"
