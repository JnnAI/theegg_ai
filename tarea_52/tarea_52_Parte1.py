
def introducirInput():                                              #Introduce un input en formato int(). Un modo de mejorar esta funcion seria introduciendo un filtro que no deje meter ni strings ni floats. Como el enunciado no lo pide, no lo he implementado.
    lista=[]
    validar=True
    print("\nA continuacion se te va a pedir que introduzcas numeros para que sean guardados en una lista.\nEn cuanto se introduzca el valor 0, se dejara de almacenar datos.\n")
    while validar==True:                                            #Bucle infinito hasta que se inserta el elemento 0, el cual no se guarda como valor.

        entrada=int(input("\nIngresa un numero por favor: "))

        if entrada==0:                                              #Si se introduce cero, el booleano se convierte en False y deja de introducir valores
            print("\n")
            print("lista completada!")
            print("\n")
            validar = False

        else:
            print("Numero introducido correctamente.\n")            #Introduce numeros en la lista hasta que entre el valor 0
            lista.append(entrada)

    return lista


def eliminarElementoLista(lista):                                   #Pide un input (numero entero) para buscarlo en la lista y eliminarlo

    numero=int(input("\nIntroduce un numero a eliminar en la lista: "))

    if numero in lista:                                             #Si el elemento esta en la lista, lo elimina y marca que numero es y en que posicion estaba
        indice = lista.index(numero)
        lista.remove(numero)
        print("###############################################################################")
        print("\nEl elemento", numero, "ha sido eliminado de la lista en la posicion", indice)
        print("\n###############################################################################")

    else:                                                           #Si no esta en la lista, aparece el siguiente mensaje.
        print("###############################################################################")
        print("\nNo es posible eliminar el elemento porque no esta en la lista.\n")
        print("###############################################################################")
        
    return lista



def sumatorioElementos(lista):                                      #Bucle que suma todos los elementos de la lista y devuelve el resultado en pantalla

    sumatoria=0
    for i in range(len(lista)):
        sumatoria = sumatoria + lista[i]

    print("\n")
    print("El sumatorio de todos los numeros de la lista es: ", sumatoria)
    print("\n")



def listaSecundaria(lista):                                         #Crea una segunda lista filtrada en base a un numero elegido por el usuario (Se pide al usuario que introduzca un input
                                                                    #En la segunda lista solo se guardan los elementos menores al elementos introducido por el usuario.
    lista2=[]

    entrada2=int(input("Ingresa otro numero para filtrar la primera lista por debajo de ese valor: "))
    print("\n")
    for k in lista:
        if k < entrada2:
            lista2.append(k)

    for j in range(len(lista2)):
        print("El elemento numero", j, "de la nueva lista es:", lista2[j])

    print("\n")
    print("La lista numero 2 completa es: ", lista2)
    
    return lista2



def contarElementosLista(lista):                                    #Cuenta cuantas veces se repite cada elemento en la lista y genera una lista de tuplas con formato: [(elemento1,numero de veces que aparece), (elemento2, numero de veces que aparece), ...]
    resultado=[]
    tupla=()
    for elemento in lista:
            repeticiones = lista.count(elemento)
            tupla=(elemento , repeticiones)
            if tupla in resultado:
                pass
            else:
                resultado.append(tupla)
    print("\n")
    print("###############################################################################\n")
    print("La tupla de elementos repetidos da la lista original es la siguiente: ",resultado)
    print("\n###############################################################################\n")

    return resultado
 

#Programa principal que ejecuta todas las funciones anteriores.
lista1=introducirInput()
listaSinElemento=eliminarElementoLista(lista1)
sumatorio=sumatorioElementos(lista1)
lista2=listaSecundaria(lista1)
resultado=contarElementosLista(lista1)
