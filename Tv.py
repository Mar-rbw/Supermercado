from Tecnologia import	Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, tamanio: float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamanio = tamanio

    @property
    def _tamanio(self):
        return self.__tamanio

    @_tamanio.setter
    def _tamanio(self, value):
        self.__tamanio = value

    
    def calcularDescuento(self):
        return super().calcularDescuento()
    

    def __str__(self) -> str:
        precioDescuento, TotalPagar = self.calcularDescuento()
        return f"{super().__str__()}\nTamaño: {self.__tamanio}\nDescuento: {precioDescuento}\nTotal a pagar: {TotalPagar}"

