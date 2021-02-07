import numpy
import random
import string

#Funcion que pide y recoge el mensaje que se va a encriptar
def introduce_mensaje():
    cadena =input("Introduce un mensaje para cifrar:")
    mensaje = cadena.upper()
    return mensaje
#Aqui se podrian implementar condiciones de forma que no se puedan meter valores que no se deban



#En este programa, la frase de entrada se separa en grupos de 5 letras. Si el ultimo grupo no tiene 5 letras, esta funcion lo completa con una X por cada hueco faltante.
def anadir_X (mensaje):
    size=5
    #mensajesinespacios=mensaje.replace(' ','')     #esta linea se omite porque al principio elimine todos los espacios, pero luego al desencriptarlo, no se pueden volver a colocar
    #si se quisieran omitir los espacios simplemente hay que activar esa linea y reasignar los nombres dentro de esta funcion tal que asi:
            '''def anadir_X (mensaje)
                  size=5
                   mensajesinespacios=mensaje.replace(' ','')
                   resto=len(mensajesinespacios)%5
                  nuevomensajesinespacios=mensajesinespacios + (size-resto)*'X'
                  return (nuevomensajesinespacios)
            '''
    resto=len(mensaje)%5
    cantidad_x=size-resto
    nuevomensaje=mensaje + (cantidad_x)*'X'
    return(nuevomensaje, cantidad_x)

#Funcion que retira las X que añade la funcion de anadir_X. Esta se usa al final, al devolver el mensaje desencriptado.
def retirar_x(mensaje, cantidad_x):
    nuevomensaje=mensaje[:-cantidad_x]
    return nuevomensaje



#Esta funcion convierte la frase de entrada en un string separado en letras de 5 en 5 (siguiendo el procedimiento del solitario)
#Si se quisiera modificar la largura de los grupos de letras, solamente habria que modificar el valor "size".
def divide_mensaje(nuevomensajesinespacios, size):
    array = []
    for index in range(0, len(nuevomensajesinespacios), size):
        mensajeen5 = nuevomensajesinespacios[index : index + size]
        array.append(mensajeen5)
    return array
   



#Funcion que crea una cadena de letras aleatorias de la misma longitud que la cadena original
def letras_aleatorias(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))




#Funcion que convierte las letras de la cadena insertada en numeros. Para ello convierte el string que recoge en cadena a traves de .join
#Utiliza el comando ord que llama al codigo ascii para convertir A en numero. Como el codigo ascii empareja el valor de A con 65, se divide entre %32 para conseguir que A sea 1, B=2...
def convertir_en_numeros(cad):
    separador=''
    cadena=separador.join(cad)
    codificado=[]
    for letra in cadena:
        codificado.append(ord(letra)%32)

    return(codificado)


#print(cadena_numerica)
#print(KEY_numerica)


#Suma los dos strings de numeros que se generan del mensaje original y del mensaje de letras aleatorias. Se usa para encriptar
def suma_strings(string1, string2):

    string = []
    for i in range (len(string1)):
        suma=int(string1[i])+int(string2[i])
        if suma > 26:
            resultado=suma-26
        else:
            resultado=suma
        string.append(resultado)
    return string


#Resta los dos strings de numeros que se generan del mensaje original y del mensaje de letras aleatorias. Se usa para desencriptar
def resta_strings(string1, string2):

    string = []
    for i in range (len(string1)):
        resta=int(string1[i])-int(string2[i])
        if resta < 0:
            resultado=resta+26
        else:
            resultado=resta
        string.append(resultado)
    return string


#Del mismo modo que la funcion de conversion a numeros, el comando chr utiliza el lenguaje ascii para crear letras a partir de numeros
#He añadido la comilla dentro del ord porque sino, el progama generaba letras y caracteres raros. Al añadir ese signo, sale todo correcto. 
#Mas adelante en el resultado final, estas comas aparecen en el mensaje, de forma que se usa un replace para quitarlas.
def convertir_en_letras(numerica):

    string = []
    for i in numerica:
      string.append(chr(ord('`') + i)) #para recobrar un caracter de su ordinal ASCII, se utiliza chr, por lo que en esta linea el contador va cambiando letra a letra e introduciendolo todo en un string nuevo que es devuelto mediante el return
    
    return string




#print(cadena_sumada)
#print(cadena_cifrada)
#print(cadena_cifrada_2)



#Funcion que recoge todas las funciones anteriores y encripta el mensaje que se introduce en la terminal.
#Devuelve el mensaje encriptado, la clave para desencriptarlo y el numero de X que hay que quitar del mensaje final (de las que se añaden al principio al encriptarlo).
def encriptar_mensaje(mensaje):

 
    mensaje_unido, cantidad_x=anadir_X(mensaje)
    mensaje_dividido=divide_mensaje(mensaje_unido, 5)
    KEY = letras_aleatorias(len(mensaje_unido)).upper()
    KEY_en_5 = divide_mensaje(KEY, 5)
    cadena_numerica=convertir_en_numeros(mensaje_dividido)
    KEY_numerica=convertir_en_numeros(KEY_en_5)

    cadena_sumada=suma_strings(cadena_numerica, KEY_numerica)
    cadena_cifrada=convertir_en_letras(cadena_sumada)
    cadena_cifrada_2="".join(cadena_cifrada)
    cifrada=cadena_cifrada_2.upper()
    cifrada=divide_mensaje(cifrada, 5)

    return cifrada, KEY, cantidad_x


mensaje = introduce_mensaje()
cifrar, KEY, cantidad_x=encriptar_mensaje(mensaje)
cifrado=" ".join(cifrar)
print('El mensaje cifrado es el siguiente:', cifrado)

#Desencripta el mensaje recogiendo el mensaje encriptado, la clave de desencriptacion y la cantidad de X que hay que quitar para limpiar el mensaje.
def desencriptar_mensaje(mensaje, KEY, cantidad_x):
    
    mensaje_numeros = convertir_en_numeros(mensaje)
    KEY_numeros = convertir_en_numeros(KEY)

    cadena_restada=resta_strings(mensaje_numeros, KEY_numeros)
    cadena_letras=convertir_en_letras(cadena_restada)
    cadena_letras_2="".join(cadena_letras)
    desencriptado=divide_mensaje(cadena_letras_2, 5)
    #retirarX=retirar_x(desencriptado, cantidad_x)
    desencriptado_2="".join(desencriptado)
    result=desencriptado_2.replace("`", " ")
    result_2=retirar_x(result, cantidad_x)


    return result_2



desencriptado=desencriptar_mensaje(cifrar, KEY, cantidad_x)
print('El mensaje descifrado es el siguiente:',desencriptado)