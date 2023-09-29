from Tecnologia import	Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, tamanio: float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamanio = tamanio
    
    def Tv(self, marca: str, voltaje: int, precio: float, eficiencia: str, tamanio: float):
        pass
    
    def calcularDescuento(self):
        return super().calcularDescuento()

    def __str__(self) -> str:
        return f"{super().__str__()}\nTamaño: {self.__tamanio}\nDescuento: {calcularDescuento()}"

    
producto1 = Tv( 30, 5000.2, "C", "Sega", 30.2)
print(producto1)
