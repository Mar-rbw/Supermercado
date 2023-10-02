class Tecnologia():
      def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str) :
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca


      @property
      def _voltaje(self):
          return self.__voltaje
      
      @_voltaje.setter
      def _voltaje(self, value):
          self.__voltaje = value
      
      @property
      def _precio(self):
          return self.__precio
      
      @_precio.setter
      def _precio(self, value):
          self.__precio = value
      
      @property
      def _eficiencia(self):
          return self.__eficiencia
      
      @_eficiencia.setter
      def _eficiencia(self, value):
          self.__eficiencia = value
      
      @property
      def _marca(self):
          return self.__marca
      
      @_marca.setter
      def _marca(self, value):
          self.__marca = value
      
      def get_aro(self):
          return self.__aro

      def get_peso(self):
          return self.__peso

      def get_precio(self):
          return self.__precio

      def get_marca(self):
          return self.__marca

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
    