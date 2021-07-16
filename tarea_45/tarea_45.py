#Libreria que sirve para utilizar funciones de medicion de tiempo.
import time

lista=[3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]

#1: CONSTRUYE TU PROPIO ALGORITMO DE ORDENACION
#El algoritmo recorre la lista varias veces, ordenando de izquierda a derecha los elementos.
#Necesita varias pasadas para reordenar la lista

##El bucle con la i se encarga de recorrer la lista y detectar cuando el valor en una posicion es mayor que el de la posicion siguiente
##de esta forma, cuando detecta algo asi, copia el valor de la primera posicion en un comodin, e intercambia los valores entre ambas.

##El bucle con la j, se encarga de hacer recorrer la lista n veces (cantidad de valores de lista) para asegurar que todos los valores estan ordenados.
##UNA FORMA DE OPTIMIZAR EL CODIGO SERIA HACIENDO QUE DETECTE CUANDO ESTA ORDENADA LA LISTA, PARA SALIR DE LOS BUCLES
def ordenar(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1, 0,-1):
            if lista[i-1]>lista[i]:
                comodin=lista[i-1]
                lista[i-1]=lista[i]
                lista[i]=comodin
        
    return lista

lista_ordenada=ordenar(lista)
#print(lista_ordenada)


#2: BUSCA 874 USANDO ALGORITMO SECUENCIAL Y BINARIO
##Esta funcion recorre todas las posiciones de la lista y en cuanto el elemento buscado coincide con uno en la lista, devuelve su posicion
def secuencial(elemento, lista):
    cont1=0
    for i in range(len(lista)):
        cont1=cont1+1
        if lista[i]==elemento:
            posicion=i
            return posicion, cont1
        
##Esta funcion divide por la mitad la lista en la que se busca el elemento, y si el elemento no se encuentra en la posicion del medio, vuelve a dividir el siguiente cacho de lista
##Ha de estar ordenada!!! Sino no funciona
def binaria(elemento, lista):
    cont2=0
    izq = 0
    der = len(lista)-1
    encontrado = False

    while izq<=der and not encontrado:
        medio=(izq+der)//2
        cont2=cont2+1
        if lista[medio]==elemento:
            encontrado=True
            posicion=medio
        elif elemento<=lista[medio]:
            der=medio-1
        else:
            izq=medio+1

    return posicion, cont2

t0=time.time()
busqueda_secuencial, cont1=secuencial(874, lista_ordenada)
#print("\nPosicion del elemento buscado mediante busqueda SECUENCIAL: ", busqueda_secuencial)
t1=time.time()
busqueda_binaria, cont2=binaria(874, lista_ordenada)
#print("\nPosicion del elemento ordenado mediando busqueda BINARIA: ", busqueda_binaria)
t2=time.time()


print("\n")
print("{}  -  {}".format("SECUENCIAL, cantidad de iteracciones realizadas: ", cont1, "Tiempo de busqueda:", t1-t0))
print("{}  -  {}".format("SECUENCIAL, tiempo de busqueda: ", t1-t0))
print("\n")

print("{}  -  {}".format("BINARIA, cantidad de iteracciones realizadas: ", cont2, "Tiempo de busqueda:", t2-t1))
print("{}  -  {}".format("BINARIA, tiempo de busqueda:", t2-t1))
print("\n")
