#•	Los Transportes tienen un costo adicional en relación al despacho.
# El costo base del despacho es de $4000 sumado al valor por kg.

class Transporte:
    def __init__(self, costoDespachoBase: int=4000):
        #Debe ser inmutable
        self.__costoDespachoBase = costoDespachoBase
    
    def calcularDespacho(self, peso, valorKilo):
        valorDespacho = self.__costoDespachoBase + (peso * valorKilo)
        return valorDespacho