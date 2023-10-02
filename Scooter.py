from Transporte import Transporte
from Tecnologia import Tecnologia

class Scooter(Transporte, Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, aro: float, velocidad: int, peso: float):
        super().__init__()
        Tecnologia.__init__(self, voltaje, precio, eficiencia, marca)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

    @property
    def _aro(self):
        return self.__aro

    @_aro.setter
    def _aro(self, value):
        self.__aro = value

    @property
    def _velocidad(self):
        return self.__velocidad

    @_velocidad.setter
    def _velocidad(self, value):
        self.__velocidad = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value

        
    def calcularDespacho(self):
        valorKilo = 300
        valorDespacho =  super().calcularDespacho(self.__peso, valorKilo)
        return valorDespacho
        
    def calcularDescuento(self):
        return super().calcularDescuento()
    
    def __str__(self):
        precioDescuento, totalPagarDescuento = self.calcularDescuento()
        costoDespacho = self.calcularDespacho()
        TotalDespachoDescuento = totalPagarDescuento + costoDespacho
        return f"{super().__str__()}\nAro: {self.__aro}\nVelocidad: {self.__velocidad}\nPeso: {self.__peso}\nDescuento: {precioDescuento}\nCosto del despacho: {costoDespacho}\nValor Total: {TotalDespachoDescuento}"
    