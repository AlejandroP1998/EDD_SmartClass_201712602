from abb import Arbol
import os
from PIL import Image


def main():
    os.system('cls')
    cerrar = False
    # RAIZ
    arbol = Arbol(201712602, 'Josue')
    # RAMAS Y HOJAS
    arbol.agregar(201712601, "Peach")
    arbol.agregar(201412604, "Ada")
    arbol.agregar(201912607, "Leon")
    arbol.agregar(202012600, "Cuphead")
    arbol.agregar(201612608, "Megaman")
    arbol.agregar(201812612, "Jack")
    arbol.agregar(201512600, "Mario")
    arbol.agregar(201612619, "Daxter")
    arbol.agregar(201712617, "Sonic")
    while(cerrar == False):
        print('Menu principal')
        print('1. Agregar')
        print('2. Eliminar')
        print('3. Grafo')
        print('4. Profundidad del arbol')
        print('5. Salir')
        opcion = input('Escriba la opcion que desee: ')
        if opcion == "1":
            carne = int(input('Ingrese el carne del estudiante \n'))
            nombre = input('Ingrese el nombre del estudiante \n')
            arbol.agregar(carne, nombre)
        elif opcion == "2":
            busqueda = int(input('Ingrese el carne del estudiante a eliminar \n'))
            arbol.eliminar(busqueda)
        elif opcion == "3":
            arbol.grafo()
            f = open('grafo.dot', 'a')
            f.write('}'+os.linesep)
            f.close()
            os.system("dot -Tpng grafo.dot -o grafo.png ")
            img = Image.open('grafo.png')
            img.show()
            print('El grafo se genero correctamente \n')
        elif opcion == "4":
            p = arbol.profundidadA(arbol.raiz)
            print('La profundidad del arbol es: '+str(p))
        elif opcion == "5":
            cerrar = True
            os.system('exit()')
        else:
            main()


main()
