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
                  descuento = precio - (precio * 0.5)
            elif lower == ("c" or "d"):
                  descuento
            elif lower == ("e" or "f"):
                  pass
            else:
                print("No aplica descuento")

    def __str__(self) -> str:
          text = f"Marca: {self.__marca}"
          text += f"\nVoltaje: {self.__voltaje}"
          text += f"\nEficiencia: {self.__eficiencia}"
          text += f"\nPrecio: {self.__precio}"