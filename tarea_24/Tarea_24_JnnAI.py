#esta primera funcion recoge el valor introducido por el usuario y lo filtra para comprobar que es un numero decimal entero.
#en caso de no ser un numero decimal entero, devuelve un error y vuelve a pedir el numero. Una vez obtenido el numero en su formato correcto, devuelve el numero.
def input_num():
    while True:
        numero = input('Introduce un numero decimal entero, por favor: ')
        try:
            numero=int(numero)
            return numero
        except ValueError:
            print("El numero introducido es incorrecto. Inserta un numero decimal entero por favor")

    return numero


#esta funcion la he hecho porque en la conversion a binario he utilizado listas numericas.
#para devolver el resultado final, lo que hago es convertir la lista numerica con el resultado a formato cadena, y lo imprimo en pantalla.
#la funcion convierte una a una todas las variables numericas a str,  por eso tiene un contador.
def num_to_str(a):
    for i in range (len(a)):
        a[i]=str(a[i])
    return(a)


#esta funcion es la que recoge un numero decimanl entero y lo transforma a binario.
#para convertir un numero a binario hace falta dividirlo entre 2 hasta que el cociente final sea 1. Recoger todos esos restos que se han generado por el camino, y ponerlos en orden inverso
def dec_to_binary(num):
    string_restos=[]                    #inicializo una lista vacia donde voy a ir metiendo todos los restos que salen de las divisiones
    resto=num%2                         #calculo el primer resto del numero insertado
    cociente=int(num/2)                 #calculo el primer cociente del numero insertado. De esta forma puedo entrar ya en mi condicion While
    string_restos.append(resto)         #inserto en mi lista de restos el primer resto.
    
#comienza el bucle que va a ir dividiendo entre 2 todos los cocientes desde el primero. Se consigue una lista de restos y el cociente actualizado en todo momento.
    while cociente>1:                   #dado que el ultimo cociente siempre va a ser 1, es un buen limitador para el while. Aunque al final del bucle hay que añadir un 1 (luego explico porque en la linea 38)
        resto=cociente%2                
        cociente=int(cociente/2)
        string_restos.append(resto)
    
    string_restos.append(1)             #aqui añado un 1 al final de la lista de restos porque el ultimo cociente calculado siempre es 1, pero el bucle while no lo tiene en cuenta, asi que lo añado manualmente.
    inversa=string_restos[::-1]         #este comando invierte el orden de mi lista
    binario=num_to_str(inversa)         #llamo a la funcion que me convierte la lista numerica en cadena de texto
    binario="".join(binario)            #quito todos los espacios entre caracteres de cadena


    return binario                      #devuelvo el valor del numero binario en formato cadena de texto



numero = input_num()                    #llamo a la funcion de insertar numero a convertir
binario=dec_to_binary(numero)           #llamo a la funcion que convierte el numero introducido en binario y me lo devuelve

print('El numero en binario es: ', binario) #imprimo en pantalla el valor del numero convertido.