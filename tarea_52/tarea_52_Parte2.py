
#Si se quiere activar el input que pide los nombres de los cursos, se ha de descomentar la siguiente funcion y comentar las lineas 29 y 30
#Ahora mismo estan activadas 2 listas predefinidas de nombres, para agilizar el programa sin necesidad de pensar nombres a introducir
"""
def introducirInput(curso):                                              #Introduce un input en formato str(). Un modo de mejorar esta funcion seria introduciendo un filtro que no deje meter ni strings ni floats. Como el enunciado no lo pide, no lo he implementado.
    lista=[]
    validar=True
    print("\nA continuacion se va a pedir que ingreses los nombres de los alumnos de",curso,"de uno en uno.\nAl introducir la secuencia ?x? se dejara de almacenar nombres.\n")
    while validar==True:                                            #Bucle infinito hasta que se inserta la combinacion ?x?, la cual no se guarda como valor.

        entrada=str(input("\nIngresa uno a uno los nombres de pila: "))

        if entrada=="?x?":                                          #Si se introduce ?x?, el booleano se convierte en False y deja de introducir nombres
            print("\n")
            print("lista completada!")
            print("\n")
            validar = False

        else:
            print("Nombre introducido correctamente.\n")            #Introduce nombres en la lista hasta que entre el valor ?x?
            lista.append(entrada)

    return lista
primaria="primaria"
secundaria="secundaria"
listaPrimaria=introducirInput(primaria)
listaSecundaria=introducirInput(secundaria)

"""
listaPrimaria=["Jon", "Josune", "Jon", "Idoia", "Sandra", "Jesus", "Laura", "Laura", "Jon", "Yas", "Jose", "Jose"]
listaSecundaria=["Yas", "Jonan", "Jose", "Eneko", "Teresa", "Jonan", "Teresa", "Teresa", "Jon", "Idoia", "Jon", "Laura"]

def buscar_iguales(lista1, lista2):                     #Esta funcion busca en dos listas. Por cada una genera una lista de tuplas con [(nombre1,repeticiones_nombre1), (nombre2,repeticiones_nombre2),...]
    resultado=[]
    tuplaNombres1=()
    tuplaNombres2=()
    nombresPrimaria=[]
    nombresSecundaria=[]
    for nombre in lista1:
        repetido=lista1.count(nombre)
        tuplaNombres1=(nombre, repetido)
        if tuplaNombres1 in resultado:
            pass
        else:
            resultado.append(tuplaNombres1)
            nombresPrimaria.append(tuplaNombres1)

    for nombre in lista2:
        repetido=lista2.count(nombre)
        tuplaNombres2=(nombre, repetido)
        if tuplaNombres2 in resultado:
            pass
        else:
            resultado.append(tuplaNombres2)
            nombresSecundaria.append(tuplaNombres2)

    return resultado, nombresPrimaria, nombresSecundaria    #Devuelve una lista con los nombres de los niños de todos los cursos, la lista de Primaria y la de Secundaria


def obtener_nombres(resultado):                             #De la lista de tuplas, extrae solamente los nombres. Los clasifica entre nombres repetidos y sin repetir
    listaNombresRepetidos=[]
    listaNombresSinRepetir=[]
    for elemento in resultado:
        posicion=elemento[1]
        if posicion>1:
            listaNombresRepetidos.append(elemento[0])
        else:
            listaNombresSinRepetir.append(elemento[0])
    return listaNombresRepetidos, listaNombresSinRepetir


def lista_desde_tupla(lista1, lista2):                      #Genera una lista de nombres usando la lista de tuplas, aislando los nombres de Primaria y Secundaria
    nombresPrimaria=[]
    nombresSecundaria=[]
    for i in lista1:
        nombresPrimaria.append(i[0])
    for j in lista2:
        nombresSecundaria.append(j[0])
    return nombresPrimaria, nombresSecundaria


def repetidos_entre_cursos(nombresPrimaria, nombresSecundaria): #Busca que nombres se repiten entre los alumnos de ambos cursos
    repetidosEntreCursos=[]

    for nombre in nombresPrimaria:
        if nombre in nombresSecundaria:
            if nombre in repetidosEntreCursos:
                pass
            else:
                repetidosEntreCursos.append(nombre)

    return repetidosEntreCursos


def no_repetidos_en_secundaria(nombresPrimaria, nombresSecundaria): #Busca que nombres de Primaria no se repiten en Secundaria
    noRepetidosEnSecundaria=[]
    
    for nombre in nombresPrimaria:
        if nombre in nombresSecundaria:
            pass
        else:
            noRepetidosEnSecundaria.append(nombre)
    return noRepetidosEnSecundaria

###PROGRAMA PRINCIPAL
#Adquisicion de la listas filtradas mediante las funciones anteriores
listaTotal, nombresPrimaria, nombresSecundaria = buscar_iguales(listaPrimaria, listaSecundaria)
listaTotalRepetidos, listaTotalSinRepetir = obtener_nombres(listaTotal)
nombresRepetidos=repetidos_entre_cursos(listaPrimaria, listaSecundaria)
noRepetidosEnSecundaria=no_repetidos_en_secundaria(listaPrimaria, listaSecundaria)

#Enunciado 1:
print("\nLa lista de nombres entre Primaria y Secundaria (sin repeticiones, es decir, solo salen una vez) es:\n", listaTotalSinRepetir)

#Enunciado 2:
print("\nLos nombres que se repiten entre Primaria y Secundaria son los siguientes:\n", nombresRepetidos)

#Enunciado 3:
print("\nLos nombres de Primaria que no se repiten en Secundaria son los siguientes:\n", noRepetidosEnSecundaria)
print("\n")
