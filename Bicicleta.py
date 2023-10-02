from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, aro: float, peso: float, precio: float, marca: str):
        super().__init__()
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca
        
    def calcularDespacho(self):
        valorKilo = 400
        valorDespacho =  super().calcularDespacho(self.__peso, valorKilo)
        return valorDespacho
        
    def __str__(self):
        costoDespacho = self.calcularDespacho()
        return f"Aro: {self.__aro}\nPeso: {self.__peso}\nPrecio: {self.__precio}\nMarca: {self.__marca}\nCosto del despacho: {costoDespacho}\nValor total: {costoDespacho + self.__precio}"
