from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, aro: float, peso: float, precio: float, marca: str):
        super().__init__()
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    @property
    def _aro(self):
        return self.__aro

    @_aro.setter
    def _aro(self, value):
        self.__aro = value

    @property
    def _peso(self):
        return self.__peso

    @_peso.setter
    def _peso(self, value):
        self.__peso = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

        
    def calcularDespacho(self):
        valorKilo = 400
        valorDespacho =  super().calcularDespacho(self.__peso, valorKilo)
        return valorDespacho
        
    def __str__(self):
        costoDespacho = self.calcularDespacho()
        return f"Aro: {self.__aro}\nPeso: {self.__peso}\nPrecio: {self.__precio}\nMarca: {self.__marca}\nCosto del despacho: {costoDespacho}\nValor total: {costoDespacho + self.__precio}"
