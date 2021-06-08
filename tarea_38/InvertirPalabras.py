def comprobar_input():
    nfrases=input('\nCuantas frases van a ser invertidas? (Introduce un numero): ')
#EL USUARIO INTRODUCE UN VALOR PARA QUE EL BUCLE PUEDA COMENZAR. 
#COMPRUEBA SI EL VALOR INTRODUCIDO ES CORRECTO
#EVITA PODER INTRODUCIR LETRAS PIDIENDO INTRODUCIR NUMERO ENTERO
    while nfrases.isnumeric()==False:
        if nfrases.isnumeric()==True:
            print('\nValor introducido correctamente.\n')
            pass
        else:
            print('\nEl valor necesario a insertar en este input es un NUMERO ENTERO.')
            nfrases=input('Cuantas frases van a ser invertidas? (Introduce un numero): ')
    #DEVUELVE EL VALOR EN FORMATO DE NUMERO ENTERO PARA PODER COMENZAR A INTRODUCIR LAS FRASES
    return nfrases


def inversor_frase(frase):
    #SEPARA LA FRASES EN PALABRAS Y UN BUCLE INVERSO VA COPIANDO LOS VALORES DESDE EL FINAL AL INICIO EN UNA NUEVA LISTA DE PALABRAS
    lista=frase.split()
    lista2=[]
    j=len(lista)-1

    while j>=0:
        lista2.append(lista[j])
        j=j-1
    #LOS VALORES INTRODUCIDOS EN LA LISTA, SE UNEN NUEVAMENTE JUNTANDO LAS PALABRAS INVERTIDAS Y SEPARADAS POR ESPACIOS.
    frase2=" ".join(lista2)
    return frase2


#ESTA FUNCION USA LA CANTIDAD DE FRASES (nfrases) PARA PEDIR LAS FRASES A INVERTIR, INVERTIRLAS Y GUARDARLAS DIRECTAMENTE EN UNA LISTA
def input_bucle(nfrases):
    lista=[]
    i=0
    num=int(nfrases)
    while i < num:
        entrada=input(f'Frase {i+1}: ')
        fraseinversa=inversor_frase(entrada)
        lista.append(fraseinversa)
        i=i+1
    return lista

#UN BUCLE LEE LA LISTA DE FRASES INVERTIDAS Y LAS VA IMPRIMIENDO EN PANTALLA
def resultado(listafrases):
    for i in range(len(listafrases)):
        print(f'Frase inversa {i+1}: ',listafrases[i])

nfrases=comprobar_input()
listafrases=input_bucle(nfrases)
print('\n\n# RESULTADOS #\n')
result=resultado(listafrases)