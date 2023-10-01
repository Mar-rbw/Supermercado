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
                  print(f"Precio del descuento: {descuentoAplicado}")
                  totalPagar  = self.__precio * (1 - descuento)
                  print(f"Precio aplicado al producto: {totalPagar}")
                  print(f"Ecuacion {descuento}: {self.__precio} - {descuentoAplicado} = {totalPagar}")
                  return descuentoAplicado, totalPagar
            
            elif nivelEficiencia in ["C", "D"]:
                  descuento = 0.3
                  descuentoAplicado = self.__precio * 0.3
                  print(f"Precio del descuento: {descuentoAplicado}")
                  totalPagar  = self.__precio * (1 - descuento)
                  print(f"Descuento aplicado al producto: {totalPagar}")
                  print(f"Ecuacion {descuento}: {self.__precio} - {descuentoAplicado} = {totalPagar}")
                  return descuentoAplicado, totalPagar
            
            elif nivelEficiencia in ["E", "F"]:
                  descuento = 0.1
                  descuentoAplicado = self.__precio * 0.1
                  print(f"Precio del descuento: {descuentoAplicado}")
                  totalPagar  = self.__precio * (1 - descuento)
                  print(f"Descuento aplicado al producto: {totalPagar}")
                  print(f"Ecuacion {descuento}: {self.__precio} - {descuentoAplicado} = {totalPagar}")
                  return descuentoAplicado, totalPagar
            else:
                print("No aplica descuento")
            
            
    def __str__(self) -> str:
          text = f"Marca: {self.__marca}"
          text += f"\nVoltaje: {self.__voltaje}"
          text += f"\nEficiencia: {self.__eficiencia}"
          text += f"\nPrecio: {self.__precio}"
          return text
    
""" PRODUCTO1 = Tecnologia(30, 90.8, "C", "Sushipleto")
PRODUCTO1.calcularDescuento()  """