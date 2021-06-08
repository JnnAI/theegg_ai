def comprobar_input():
    entrada=input('\nIntroduce un numero entre 1 y 1.000.000 para buscar su palindromo-primo mas cercano: ')
#INTRODUCE UN VALOR PARA PODER COMENZAR A COMPROBAR SI ESTA INTRODUCIDO CORRECTAMENTE O NO
    if entrada.isnumeric()==True:               #SI EL VALOR ES NUMERICO, COMPRUEBA SI ESTA DENTRO DEL RANGO ADMITIBLE 1-100000
        if int(entrada)>=1 and int(entrada)<=1000000:
            print('Valor introducido correctamente.')
        
        #SI POR UN CASUAL NO ESTUVIERA DENTRO DE ESE RANGO, REPITE UN BUCLE QUE PIDE LA REINSERCION DE LA VARIABLE
        while int(entrada)<1 or int(entrada)>1000000:
            print('\nValor necesario entre 1 y 1.000.000, por favor.')
            entrada=input('Introduce un numero entre 1 y 1.000.000 para buscar su palindromo-primo mas cercano: ')

    #SI EL VALOR INTRODUCIDO ES UNA LETRA, REPITE UN BUCLE HASTA QUE EL VALOR ES NUMERICO
    while entrada.isnumeric()==False:
        print('\nValor necesario EN FORMATO NUMERICO ENTERO.')
        entrada=input('Introduce un numero entre 1 y 1.000.000 para buscar su palindromo-primo mas cercano: ')
            
    return int(entrada)         #DEVUELVE EL VALOR NUMERICO DENTRO DEL RANGO 1-100000 RECOGIDO POR LA FUNCION


def primo_si_no(numero):
    numero = int(numero)        #CONVIERTE EL VALOR STRING DE LA ENTRADA EN NUMERO PARA PODER HACER CALCULOS NUMERICOS
    n=2                         #SE USA N=2 PORQUE AL CALCULAR PRIMOS EL NUMERO 1 NO SE CUENTA

    #CONDICION QUE SI EL VALOR ES 1, DEVUELVE DIRECTAMENTE EL RESULTADO QUE ESTE REPRESENTA, EN CASO CONTRARIO, CALCULA EL PRIMO MAS CERCANO
    if numero==1:
        print('El numero NO es primo ya que 1 NO se considera primo.')
        return False
    #CALCULA SI ES PRIMO. SI NO LO ES, DEVUELVE False, SINO True
    else:
        for i in range(n, numero):
            if numero % i == 0:
                #print('El numero NO es primo ya que', n, 'es divisor de', numero)
                return False
            else:
                return True
                
 

#ESTA FUNCION INVIERTE EL VALOR DE ENTRADA EN FORMATO STRING ANTES DE CONVERTIRLO A NUMERICO PARA HACER CALCULOS
def palindromo_si_no(numero):
    inverso=numero[::-1]
    numero=int(numero)
    inverso=int(inverso)
    #SI EL NUMERO ES 1, DEVUELVE RESULTADO PARA 1 DIRECTAMENTE.
    if numero==1:
        print('El numero NO es palindromo ya que 1 NO se considera palindromo.')
        pass
    #SI EL NUMERO INTRODUCIDO ES IGUAL A SU INVERSO, ESTE NUMERO ES PALINDROMO. CASO POSITIVO DEVUELVE True, NEGATIVO False
    elif numero==inverso:
        #print('El numero es palindromo')
        return True
    else:
        #print('El numero NO es palindromo')
        return False

#EMPLEA LAS FUNCIONES ANTERIORES PARA CALCULAR PRIMOS Y PALINDROMOS.
#ITERA DESDE EL NUMERO INTRODUCIDO EN EL INPUT HASTA ENCONTRAR EL SIGUIENTE NUMERO PRIMO Y PALINDROMO
#DEVUELVE EL RESULTADO DE LA FUNCION PARA QUE ESTE PUEDA SER IMPRESO EN PANTALLA
def buscador_primo_palin_peque(entrada):
    i=int(entrada)
    while i>0:
        primo=primo_si_no(i)
        palindromo=palindromo_si_no(str(i))
        if primo==False or palindromo==False:
            i=i+1
        elif primo==True and palindromo==True:
            resultado=i
            return resultado
    
    

valor=comprobar_input()
resultado=buscador_primo_palin_peque(valor)
print('\nEL NUMERO PRIMO Y PALINDROMO MAS CERCANO A', valor, 'ES: ', resultado, '\n\n')