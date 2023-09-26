class Transporte:
    def __init__(self, costoDespachoBase: int = 4000):
        #Debe ser inmutable
        self.__costoDespachoBase = costoDespachoBase

    def get_costoDespachoBase(self):
        return self.__costoDespachoBase
    
    def calcularDespacho(self, peso):
        despacho = self.__costoDespachoBase * peso  # el costo de despacho por kilogramos del producto
        return despacho	