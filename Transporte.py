class Transporte:
    
    COSTO_DESPACHO_BASE: int = 4000
    
    def __init__(self):
        pass
    
    def calcularDespacho(self, peso, valorKilo):
        valorDespacho = self.COSTO_DESPACHO_BASE + (peso * valorKilo)
        return valorDespacho