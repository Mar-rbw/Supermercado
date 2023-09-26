from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, nombreConsola: str, version: str):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def Consola(self, nombreConsola: str, version: str, marca: str, voltaje: int, precio: float, eficiencia: int):
        pass

    def calcularDescuento(self):
        pass
    ## Como le hacemos con el agregarle el 5 % usando poo 
    def __str__(self) -> str:
        txt =  super().__str__()
        txt += f"\nNombre: {self.__nombreConsola}\nVersion: {self.__version}"