#MEDIANTE ESTA FUNCION SE VA A COPIAR UNA DE LAS CADENAS Y SE VA A IR RECORTANDO DE DERECHA A INQUIERDA Y VICEVERSA, BUSCANDO COINCIDENCIAS
def conseguir_maxima_coincidencia(cadena_1, cadena_2): 
    #COPIA EN 'TROZO' UNA DE LAS CADENAS PARA PODER TRANSFORMARLA AL GUSTO
    trozo = cadena_2
    #INDICE QUE MARCA UN INICIO PARA RECORTAR LA FRASE
    indice_inicio = 0
    #LONGITUD DE UNA DE LAS CADENAS
    longitud = len(cadena_2)
    while longitud > 0:                                         #SIEMPRE QUE LA LONGITUD DE LA CADENA SEA MAYOR A CERO, SE REPITE EL BUCLE
        while indice_inicio + longitud <= len(cadena_2):        #
            indice_final = indice_inicio + longitud
            trozo = cadena_2[indice_inicio: indice_final]       #EL TROZO DE CADENA SE REDUCE A LAS VARIABLES DE INICIO Y FIN
            if trozo in cadena_1:
                return trozo                                    #SI EL TROZO DE LA CADENA 2 SE ENCUENTRA DENTRO DE LA CADENA 1, DEVUELVE EL RESULTADO
            indice_inicio = indice_inicio + 1                   #SI NO SE HA DEVUELTO EL RESULTADO, EL INDICE DE INICIO SE INCREMENTA PARA SEGUIR REDUCIENDO EL TROZO DE CADENA
        longitud = longitud - 1                                 #SI LO ANTERIOR NO DEVUELVE RESULTADO, SE REDUCE LA CADENA POR EL EXTREMO CONTRARIO
        indice_inicio = 0                                       #RESETEA EL INDICE DE INICIO PARA PODER VOLVER A REDUCIR POR EL INICIO DESDE 0
    return ""

#EN EVZ DE PONER UN INPUT SE COLOCAN LAS CADENAS DIRECTAMENTE DE FORMA QUE SE AGILIZA EL PROCESO Y SE EVITAN ERRORES AL INTRODUCIR DATOS
cadena_1 = "ATGTCTTCCTCGA"
cadena_2 = "TGCTTCCTATGAC"

#COMPARACION DE AMBAS CADENAS Y RECOGIENDO EL VALOR DE RESULTADO
resultado = conseguir_maxima_coincidencia(cadena_1, cadena_2)

#CONDICION QUE IMPRIME EN PANTALLA EL RESULTADO DE LA CADENA MAS LARGA COINCIDENTE, O UN MENSAJE DE QUE NO HAY COINCIDENCIAS
if resultado == "":
    print("Las cadenas no coinciden")
else:
    print("La coincidencia más grande es: " + resultado)
