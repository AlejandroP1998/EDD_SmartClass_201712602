from Estructuras.Pagina import Pagina
from Estructuras.ArbolB import Arbol_B
from Grafo.Grafo import  Grafo

if __name__ == '__main__':
    valor = "039"
    valor = int("039")
    print(type(valor))
    arbolB = Arbol_B(5)
    arbolB.insertar(1)
    arbolB.insertar(2)
    arbolB.insertar(3)
    arbolB.insertar(4)
    arbolB.insertar(5)
    arbolB.insertar(6)
    arbolB.insertar(7)
    arbolB.insertar(8)
    arbolB.insertar(9)
    arbolB.insertar(10)
    arbolB.insertar(11)
    arbolB.insertar(12)
    
    g = Grafo()
    g.generarGrafo(arbolB.raiz)
