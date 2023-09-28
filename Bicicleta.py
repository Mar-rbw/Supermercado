from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self,aro: float, peso: float, precio: float, marca: int, costoDespachoBase: int = 4000 ):
        super().__init__(costoDespachoBase)
        self.__aro = aro
        self.__peso = peso #400 valor x kilo
        self.__precio = precio
        self.__marca = marca
