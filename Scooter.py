from Transporte import Transporte

class Scooter(Transporte):
    def __init__(self,aro: float, peso: float, precio: float, marca: int, costoDespachoBase: int = 4000 ):
        super().__init__(costoDespachoBase)
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    