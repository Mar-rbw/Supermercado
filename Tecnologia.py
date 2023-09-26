class Tecnologia():
    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str) :
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def Tecnologia(self ,marca: str, voltaje: int, precio: float, eficiencia: str):
            pass
        
    #Debe devolver float
    def calcularDescuento(self, eficiencia, precio):
            lower = eficiencia
            if lower == ("a" or "b"):
                  descuento = precio * 0.5
                  total = precio - descuento
                  return total
            elif lower == ("c" or "d"):
                  descuento = precio * 0.3
                  total = precio - descuento
                  return total
            elif lower == ("e" or "f"):
                  descuento = precio * 0.1
                  total = precio - descuento
                  return total
            else:
                print("No aplica descuento")

    def __str__(self) -> str:
          text = f"Marca: {self.__marca}"
          text += f"\nVoltaje: {self.__voltaje}"
          text += f"\nEficiencia: {self.__eficiencia}"
          text += f"\nPrecio: {self.__precio}"