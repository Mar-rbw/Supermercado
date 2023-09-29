class Tecnologia():
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str) :
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def Tecnologia(self ,marca: str, voltaje: int, precio: float, eficiencia: str):
            pass
    
    def calcularDescuento(self):
            nivelEficiencia = self.__eficiencia.upper()
            if nivelEficiencia in ["A", "B"]:
                  descuento = 0.5
                  precioDescuento = self.__precio * 0.5
                  print(f"Precio del descuento: {precioDescuento}")
                  descuentoAplicado  = self.__precio * (1 - descuento)
                  print(f"Precio aplicado al producto: {descuentoAplicado}")
                  print(f"Ecuacion {descuento}: {self.__precio} - {precioDescuento} = {descuentoAplicado}")
                  return descuentoAplicado
            
            elif nivelEficiencia in ["C", "D"]:
                  descuento = 0.3
                  precioDescuento = self.__precio * 0.3
                  print(f"Precio del descuento: {precioDescuento}")
                  descuentoAplicado  = self.__precio * (1 - descuento)
                  print(f"Precio aplicado al producto: {descuentoAplicado}")
                  print(f"Ecuacion {descuento}: {self.__precio} - {precioDescuento} = {descuentoAplicado}")
                  return descuentoAplicado
            
            elif nivelEficiencia in ["E", "F"]:
                  descuento = 0.1
                  precioDescuento = self.__precio * 0.1
                  print(f"Precio del descuento: {precioDescuento}")
                  descuentoAplicado  = self.__precio * (1 - descuento)
                  print(f"Precio aplicado al producto: {descuentoAplicado}")
                  print(f"Ecuacion {descuento}: {self.__precio} - {precioDescuento} = {descuentoAplicado}")
                  return descuentoAplicado
            else:
                print("No aplica descuento")
            
            
    def __str__(self) -> str:
          text = f"Marca: {self.__marca}"
          text += f"\nVoltaje: {self.__voltaje}"
          text += f"\nEficiencia: {self.__eficiencia}"
          text += f"\nPrecio: {self.__precio}"
          return text
    
PRODUCTO1 = Tecnologia(30, 90.8, "C", "Sushipleto")
PRODUCTO1.calcularDescuento() 