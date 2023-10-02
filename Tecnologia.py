class Tecnologia():
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str) :
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca
        
    
    def calcularDescuento(self):
            nivelEficiencia = self.__eficiencia.upper()
            if nivelEficiencia in ["A", "B"]:
                  descuento = 0.5
                  descuentoAplicado = self.__precio * 0.5

                  totalPagar  = self.__precio * (1 - descuento)
                  return descuentoAplicado, totalPagar
            
            elif nivelEficiencia in ["C", "D"]:
                  descuento = 0.3
                  descuentoAplicado = self.__precio * 0.3
                  totalPagar  = self.__precio * (1 - descuento)
                  return descuentoAplicado, totalPagar
            
            elif nivelEficiencia in ["E", "F"]:
                  descuento = 0.1
                  descuentoAplicado = self.__precio * 0.1
                  totalPagar  = self.__precio * (1 - descuento)
                  return descuentoAplicado, totalPagar
            else:
                print("No aplica descuento")
            
            
    def __str__(self) -> str:
          return f"Marca: {self.__marca}\nVoltaje: {self.__voltaje}\nEficiencia: {self.__eficiencia}\nPrecio: {self.__precio}"