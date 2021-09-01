class Nodo:
    def __init__(self, carne, nombre):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.carne = carne
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None