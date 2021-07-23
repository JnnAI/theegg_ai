#Con esta libreria se mide el peso de cada mensaje en Bytes.
import sys

# CREAR DICCIONARIO. Coge el mensaje y crea un diccionario usando el metodo LZ77. Devuelve el diccionario de compresion generado para:
# poder crear a partir de este el mensaje codificado.
# poder desencriptarlo mas adelante.
#
# EDIT: bucle que busca coincidencias en el texto anterior (texto_procesado). 
# EDIT: cuando encuentra coincidencias aumenta el tamaño de la ventana para encontar coincidencias más grandes
# EDIT: cuando ya no se encuentran más coincidencias añade una entrada al diccionario con: 
# - el índice menos el tamaño de la ventana (m)
# - el tamaño de la ventana (n)
# - la última letra del fragmento (s)

def crear_diccionario(mensaje):
    
    diccionario = list()
    texto_procesado = "" # texto que ya se ha comprobado
    indice = 0 # índice de comienzo del fragmento que se está comprobando
    
    while indice < len(mensaje):

        ventana = 1 # tamaño del fragmento que se quiere comprobar
        fragmento = mensaje[indice: indice + ventana] # trocito de texto que vamos a buscar dentro del texto procesado
        indice_coincidencia = texto_procesado.rfind(fragmento) # el último índice de la coincidencia del fragmento en el texto procesado. Si no se encuentra, es -1. Ejemplo: "Mi casa, tu casa".rfind("casa") = 12
        m = 0 # valores del diccionario
        n = 0 # valores del diccionario
        s = fragmento[-1] # valores del diccionario

        while indice_coincidencia != -1 and indice + ventana < len(mensaje):
            ventana += 1
            fragmento = mensaje[indice: indice + ventana]
            m = indice - indice_coincidencia # coge las posiciones hacia atrás hasta donde comienza la repetición
            n = len(fragmento) - 1 # coge las posiciones hasta el caracter que no se repite
            s = fragmento[-1] # coge el último caracter del fragmento
            indice_coincidencia = texto_procesado.rfind(fragmento) # añade un caracter más al fragmento para ver si también se repite


        texto_procesado = texto_procesado + fragmento # guarda el texto que ya se ha comprobado
        diccionario.append((m, n, s)) # añade la entrada al diccionario
        indice = indice + ventana # continúa analizando el resto del mensaje

    return diccionario




# COMPRIMIR. Genera el mensaje comprimido para poder visualizarlo y medir cuanta memoria consume.

def comprimir(diccionario):
    # bucle que recorre diccionario en la posicion del medio de cada valor. Si es 0, copia la letra, si es mayor que 0, genera clave para esa combinacion y copia la clave en lugar de las letras
    clave = list(range(len(diccionario))) # Genero una tupla con valores del 0 al largo total del diccionario. Para cada posicion corresponde una clave para encriptar el mensaje
    mensaje_comprimido = ""
    cont_clave = -1
    for s in diccionario:
        if s[1] == 0:
            mensaje_comprimido = mensaje_comprimido + s[2]
            cont_clave += 1
        else:
            mensaje_comprimido = mensaje_comprimido + str(clave[cont_clave])
            cont_clave += 1

    return mensaje_comprimido



# DESCOMPRIMIR. Coge el diccionario generado anteriormente y vuelve a crear el mensaje original basandose en el. No hay perdida de informacion.

def descomprimir(diccionario):
    mensaje_descomprimido = ""

    ## Un bucle recorre el diccionario.
    ## EL DICCIONARIO TIENE EL SIGUIENTE ORDEN DE VARIABLES POR CADA POSICION: (m, n, s) "Haciendo referencia a las variables usadas en el video explicativo del enuncuado de la tarea"
    # Si m=0, se copia el valor de s en esa posicion al mensaje descomprimido.
    # Si m!=0, se retrocede en el mensaje desencriptado y se copia la secuencia que se repite en esa posicion del diciconario.
    for s in diccionario:
        if s[0] != 0:
            paso_atras = len(mensaje_descomprimido) - s[0]
            paso_avance = paso_atras + s[1]
            mensaje_descomprimido += mensaje_descomprimido[paso_atras:paso_avance]     #juega con los valores de m y n en el diccionario.
        
        mensaje_descomprimido = mensaje_descomprimido + s[2]
    
    return mensaje_descomprimido


# PROGRAMA PRINCIPAL

##Utilizar estos mensajes predefinidos si se quiere evitar tener que meter un mensaje por el usuario. (DESCOMENTAR SOLAMENTE UNO)
##En caso de usar uno de estos mensajes, hace falta comentar las lineas del bucle while, desde la 95-107.
#mensaje = "ABRACADABRARRAY"
#mensaje = "Pablito clavo un clavito, que clavito clavo Pablito?"


def input_mensaje():
    print("\n\n")
    mensaje=input("Introduce una cadena de texto de maximo 30 caracteres por favor: ")
    n_caracteres=len(mensaje)
    while True:
        if n_caracteres <1 or n_caracteres >30:
            print("El mensaje debe contener solamente 30 caracteres.")
            print("\n")
            mensaje=input("Introduce una cantidad de 30 caracteres por favor: ")
            n_caracteres=len(mensaje)
        else:
            break
    return str(mensaje)



mensaje=input_mensaje()
diccionario = crear_diccionario(mensaje)
comprimido = comprimir(diccionario)
descomprimido = descomprimir(diccionario)

espacio_mensaje = sys.getsizeof(mensaje)
espacio_mensaje_comprimido = sys.getsizeof(comprimido)
espacio_mensaje_descomprimido = sys.getsizeof(descomprimido)

print("\n")
print("~~ RESULTADOS ~~")
print("\n")
print("El mensaje inicial es:", mensaje)
print("Ocupa", espacio_mensaje, "bytes.")
print("\n")
print("El mensaje comprimido es:", comprimido)
print("Ocupa", espacio_mensaje_comprimido, "bytes.")
print("\n")
print("El mensaje descomprimido es:", descomprimido)
print("Ocupa", espacio_mensaje_descomprimido, "bytes.")
print("\n")
print("El diccionario utilizado es:", diccionario)
print("\n")

