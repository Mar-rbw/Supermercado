from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, nombreConsola: str, version: str):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__nombreConsola = nombreConsola
        self.__version = version

    @property
    def _nombreConsola(self):
        return self.__nombreConsola

    @_nombreConsola.setter
    def _nombreConsola(self, value):
        self.__nombreConsola = value

    @property
    def _version(self):
        return self.__version

    @_version.setter
    def _version(self, value):
        self.__version = value

        

    def calcularDescuento(self):
        descuento, total = super().calcularDescuento()
        if "Lite" in self.__version.capitalize():
            descuentoAdicionalLite = 0.05
            descuento *= (1 + descuentoAdicionalLite)
            total *= (1 - descuentoAdicionalLite)
            return descuento, total
        else:
            pass
        

    def __str__(self) -> str:
        precioDescuento, TotalPagar = self.calcularDescuento()
        return f"{super().__str__()}\nNombre de la consola: {self.__nombreConsola.capitalize()}\nVersión: {self.__version.capitalize()}\nDescuento: {precioDescuento}\nTotal a pagar: {TotalPagar}"
    
