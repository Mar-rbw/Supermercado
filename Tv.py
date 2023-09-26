from Tecnologia import	Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, tamanio: float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.tamanio = tamanio

    def Tv(self, marca: str, voltaje: int, precio: float, eficiencia: str, tamanio: float):
        descuento = super().calcularDescuento
        return descuento
    
    def __str__(self) -> str:
        txt = super().__str__()
        txt += f"\ntamanio = {self.tamanio}"
        return txt

    
    