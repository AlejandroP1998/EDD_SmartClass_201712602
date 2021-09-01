from nodo import Nodo
import os

class Arbol:
    # Funciones privadas
    def __init__(self, carne, nombre):
        self.raiz = Nodo(carne, nombre)

    def __agregar_recursivo(self, nodo, carne, nombre):
        if carne < nodo.carne:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(carne, nombre)
            else:
                self.__agregar_recursivo(nodo.izquierda, carne, nombre)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(carne, nombre)
            else:
                self.__agregar_recursivo(nodo.derecha, carne, nombre)

    def grafo(self):
        f = open('grafo.dot', 'w')
        f.write('digraph G{'+os.linesep)
        f.close()
        self.grafico(self.raiz)

    def grafico(self, nodo):
        f = open('grafo.dot','a')
        if nodo.izquierda is not None:
            f.write(str(nodo.carne)+' [ label="'+str(nodo.carne)+'\l'+nodo.nombre+'"]')
            f.write(str(nodo.izquierda.carne)+' [ label="'+str(nodo.izquierda.carne)+'\l'+nodo.izquierda.nombre+'"]')
            f.write(str(nodo.carne)+'->'+str(nodo.izquierda.carne)+os.linesep)
            self.grafico(nodo.izquierda)
        if nodo.derecha is not None:
            f.write(str(nodo.carne)+' [ label="'+str(nodo.carne)+'\l'+nodo.nombre+'"]')
            f.write(str(nodo.derecha.carne)+' [ label="'+str(nodo.derecha.carne)+'\l'+nodo.derecha.nombre+'"]')
            f.write(str(nodo.carne)+'->'+str(nodo.derecha.carne)+os.linesep)
            self.grafico(nodo.derecha)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.carne, nodo.nombre, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.carne, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.carne, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.carne == busqueda:
            return nodo
        if busqueda < nodo.carne:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, carne, nombre):
        self.__agregar_recursivo(self.raiz, carne, nombre)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

    def profundidadA(self,nodo):
        
        def profundo(nodo):
            if nodo is None:
                return 0
            if nodo.izquierda is not None or nodo.derecha is not None:
                return max(profundo(nodo.izquierda),profundo(nodo.derecha))+1
            else:
                return 0
        if nodo is None:
            return 0
            
        return profundo(nodo)+1
            
        

    def eliminar(self, data):
        self.raiz = self.eliminarN(self.raiz,data)
    def eliminarN(self,nodo,data):
        if nodo is None:
            print('nodo no encontrado')
        elif data < nodo.carne:
            iz = self.eliminarN(nodo.izquierda,data)
            nodo.izquierda = iz
        elif data > nodo.carne:
            der = self.eliminarN(nodo.derecha,data)
            nodo.derecha = der
        else:
            p = nodo
            if p.derecha == None:
                nodo = p.izquierda
            elif p.izquierda == None:
                nodo = p.derecha
            else:
                p = self.cambiar(p)
            p = None
        return nodo
    def cambiar(self,nodo):
        p = nodo
        a = nodo.izquierda
        while a.derecha != None:
            p = a
            a = a.derecha
        nodo.carne = a.carne
        nodo.nombre = a.nombre
        if p == nodo:
            p.izquierda = a.izquierda
        else:
            p.derecha = a.izquierda
        return a
