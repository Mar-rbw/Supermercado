from Transporte import Transporte
from Tecnologia import Tecnologia

class Scooter(Transporte, Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, aro: float, velocidad: int, peso: float, costoDespachoBase: int = 4000):
        super().__init__(costoDespachoBase)
        Tecnologia.__init__(self, voltaje, precio, eficiencia, marca)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
        
    def calcularDespacho(self):
        valorKilo = 300
        totalDespacho =  super().calcularDespacho(self.__peso, valorKilo)
        return totalDespacho
        
    def calcularDescuento(self):
        return super().calcularDescuento()
    
    def __str__(self):
        precioDescuento, totalPagarDescuento = self.calcularDescuento()
        costoDespacho = self.calcularDespacho()
        TotalDespachoDescuento = totalPagarDescuento + costoDespacho
        return f"{super().__str__()}\nAro: {self.__aro}\nVelocidad: {self.__velocidad}\nPeso: {self.__peso}\nDescuento: {precioDescuento}\nCosto del despacho: {costoDespacho}\nValor Total: {TotalDespachoDescuento}"
        

PRODUCTO1 = Scooter(30, 90.8, "C", "Sushipleto", 20.1, 100, 100.4, 10000)
print(PRODUCTO1)
