
'''
ALGORITMO DEL LECHERO.

En las siguientes lineas se explica que significa cada variable:

- Número de elementos totales, en este caso, numero de vacas (n)
- Pesos de las n vacas que hay (pesos_vacas, valores en forma de lista)
- Capacidad maxima que puede llevar el camion (capacidad_camion)
- Peso (w, marca el peso maximo que se puede alcanzar hasta el momento. Va creciendo a medida que el programa recorre la lista)

EJEMPLO:
    # n = 12 (la cantidad de vacas que hay disponibles para llevar en el camion)
    # capacidad_camion = 800 (en kg, es la carga maxima que puede soportar el camion para transportar la mejor combinacion de vacas)
    # pesos_vacas = [peso de la vaca 1, peso de la vaca 2, peso de la vaca 3... hasta llegar al numero de vacas totales que marca n]
    # litros_leche = [litros que produce la vaca 1, litros que produce la vaca 2...]

Se va a utilizar una matriz para controlar los valores de las listas, de modo que el eje X+ de la matriz corresponde al peso maximo que puede abarcar el camion (capacidad_camion)
y el eje Y- corresponde a la cantidad de elementos que vamos a manejar, en este caso (n).
'''

def lechero(capacidad_camion, pesos_vacas, litros_leche, n):


# Inicializa la matriz poniendo ceros en todas las casillas, de modo que el valor inicial asignado a cada una es 0.
    filas=n+1
    columnas=capacidad_camion+1
    Matriz=[None]*filas
    for x in range(filas):
        Matriz[x]=[None]*columnas


 # Avanza a lo largo de la lista con el contador i, hasta el total de elementos n+1. (Termina en n+1 porque las listas empiezan en la posicion cero hasta n-1)
    for i in range(n+1):                                                   


 # Aumenta el peso actual de cada elemento (w) en 1 hasta llegar a la capacidad máxima (W) de peso +1
        for w in range(capacidad_camion+1):    

             # Si ambos contadores son cero (situacion inicial), el valor de la lista es cero tambien, ya que no ha tenido tiempo de incrementarse para avanzar                                           
            if i==0 or w==0:                                               
                Matriz[i][w] = 0

            # Si el peso del elemento anterior es igual o menor al actual, se coge el máximo entre el anterior y el sumatorio de todos hasta ahora
            elif pesos_vacas[i-1] <= w:    
                Matriz[i][w] = max(litros_leche[i-1] + Matriz[i-1][w-pesos_vacas[i-1]],  Matriz[i-1][w])

            # Si no, se siguen copiando los valores anteriores en la casilla actualizada.
            else:
                Matriz[i][w] = Matriz[i-1][w]                                         

    return Matriz[n][capacidad_camion] #Devuelve el valor que tiene la matriz en la posicion designada entreo llaves




#Datos ejemplo 1
n = 6
capacidad_camion = 700
pesos_vacas = [360,250,400,180,50,90]
litros_leche = [40,35,43,28,12,13]

print(lechero(capacidad_camion, pesos_vacas, litros_leche, n))


#Datos ejemplo 2
n2 = 7
capacidad_camion2 = 1000
pesos_vacas2 = [223,243,100,200,155,300,150]
litros_leche2 = [30,34,28,45,31,50,29]

print(lechero(capacidad_camion2, pesos_vacas2, litros_leche2, n2))


#Datos ejemplo 3
n3 = 10
capacidad_camion3 = 2000
pesos_vacas3 = [340,355,223,243,130,240,260,155,302,130]
litros_leche3 = [45,50,34,39,29,40,30,52,31,46]

print(lechero(capacidad_camion3, pesos_vacas3, litros_leche3, n3))


#Datos ejemplo 4
n4 = 9
capacidad_camion4 = 775
pesos_vacas4 = [345,335,200,343,110,280,360,180,245]
litros_leche4 = [46,68,25,58,59,45,30,55,41]

print(lechero(capacidad_camion4, pesos_vacas4, litros_leche4, n4))


#Datos ejemplo 5
n5 = 10
capacidad_camion5 = 2800
pesos_vacas5 = [440,455,123,213,330,400,260,145,350,150]
litros_leche5 = [65,52,38,43,30,41,32,58,51,29]

print(lechero(capacidad_camion5, pesos_vacas5, litros_leche5, n5))