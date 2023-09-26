from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, nombreConsola: str, version: str):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def Consola(self, nombreConsola: str, version: str, marca: str, voltaje: int, precio: float, eficiencia: int):
        pass