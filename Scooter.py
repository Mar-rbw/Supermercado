from Transporte import Transporte
from Tecnologia import Tecnologia

class Scooter(Transporte, Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, aro: float, velocidad: int, peso: float, costoDespachoBase: int = 4000):
        Transporte().__init__(self, costoDespachoBase)
        Tecnologia().__init__(self, voltaje, precio, eficiencia, marca)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
        
    def calcularDescuento(self):
        return Transporte.calcularDespacho()
    
    def __str__(self) -> str:
        return f"{Tecnologia().__str__()}\nAro: {self.__aro}\nVelocidad: {self.__velocidad}\nPeso: {self.__peso}"
        
    
PRODUCTO1 = Scooter(30, 90.8, "C", "Sushipleto", 20.1, 100, 100.4, 10000)
print(PRODUCTO1)