import re
import operator
import requests
from bs4 import BeautifulSoup
import lxml

url="https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/"

'''
# Si queremos ver la respuesta que ha dado el servidor al hacer la petición lo podremos hacer con status_code, también lo podemos usar para parar la ejecución sino recibimos un estado válido como por ejemplo el 404 o 500.
print(respuesta.status_code)

# Para ver el contenido utilizaremos text, aquí se guarda todo el html de la página.
print(respuesta.text)

# Con header veremos las cabeceras que nos devuelve la página, esta puede contener cookies, información sobre que tipo de servidor están usando, el tipo de contenido (json, html, texto), etc.
print(respuesta.headers)

# Aquí podemos ver la cabecera de la petición, es decir, la que enviamos nosotros.
print(respuesta.request.headers)

# Para ver el método que hemos usado lo haremos con method, en nuestro caso get que también se ve en la llamada de la función.
print(respuesta.request.method)
'''

#se hace la peticion a la web
req = requests.get(url)

#los codigos de estado en una peticion a una web indican si se ha completado satisfactoriamente la solicitud HTTP 
#para una solicitud satisfactoria, el valor es entre 200-299. En nuestro caso, el valor 200 nos devuelve si es OK o no lo es
codigo_estado= req.status_code

if codigo_estado == 200:

    #pasar el contenido HTML de la web a un objeto BeautifulSoup
    contenido_web=BeautifulSoup(req.text, "lxml")

    clases=contenido_web.find_all('div', class_="post-content description cf")
    #print(clases)     #comprobacion de que ha cogido bien las clases desde la web.
    
    for i in clases:
        parrafos=i.find_all('p')
 
    texto_sin_filtrar=i.text.strip()
    #print(texto_sin_filtrar)

    #se empieza a recortar toda la informacion que no nos sirve, es decir, quito el parrafo superior
    comienzo=re.split('3. El mejor calefactor para una congelación\n', texto_sin_filtrar)
    comienzo.pop(0)
    #print(comienzo)
    parrafo="".join(comienzo)

    #una vez quitado el primer parrafo, se quita el segundo
    fin=re.split('\nAh, por cierto…', parrafo)
    fin.pop(1)
    #print(parrafo2)
    texto1="".join(fin)

    #se quitan todos los saltos de linea, que estan dentro del texto al haberlo convertido de la web a este programa.
    texto_filtrado=re.split('\n', texto1)

    #ya tengo el texto que necesito para analizar
    #SI HICIERA FALTA COGER UN TEXTO DIFERENTE, HABRÍA QUE CAMBIAR LOS DELIMITADORES DE TEXTO DE "comienzo" y "fin"
    texto="".join(texto_filtrado)
    #print(texto_final)

else:
    print("El codigo de estado de la web es: ", codigo_estado)



#EN CASO DE QUE SE QUIERA METER EL TEXTO DIRECTAMENTE COMO VARIABLE, DESCOMENTAR LA SIGUIENTE LINEA Y COMENTAR DE AQUI HACIA ATRAS HASTA LAS LIBRERIAS.
'''
texto= "En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento? Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo. Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda. El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno. Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie. Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."
'''

#con el comando "." se encuentran todos los caracteres de la cadena por individual
#con el comando "\s" se encuentran todos los espacios
#los datos se guardan en cada variable asignada en formato lista, de forma que usando len(cadena_analizada) se obtiene la cantidad de letras del texto
def contador_caracteres(texto):
    caracteres=re.findall(".", texto)
    espacios=re.findall("\s", texto)
    n_car=len(caracteres)
    n_car_esp=len(caracteres)-len(espacios)


    a=print("\nCantidad de caracteres individuales del texto, sin contar espacios: ", n_car)
    b=print("\nCantidad de caracteres individuales del texto, contando espacios: ", n_car_esp)

    return a,b


#de la misma manera, con el comando "\w+" se cuentan automaticamente la cantidad de palabras enteras que hay en el texto
#este comando cuenta una o mas letras juntas, buscando y almacenando las palabras que encuentra (cualquier (una o mas) cadena alfanumerica)
def contador_palabras(texto):

    palabras=re.findall("\w+", texto)
    n_palabras=len(palabras)

    return print("\nCantidad de palabras en el texto: ", n_palabras, '\n'), palabras



def ranking_palabras(texto, lista_palabras):
    #se pasan las listas a mayusculas todas de forma que no haya error a la hora de comparar ambas.
    #se declara la variable contador_palabras para ir almacenando los valores de palabras repetidas.
    lista_mayus=[i.upper() for i in lista_palabras]
    texto_mayus=texto.upper()
    contador_palabras=[]
    for palabra in lista_mayus:
        coincidencia=re.findall(f"\\b{palabra}\\b", texto_mayus)
        contador_palabras.append(len(coincidencia))

    #metodo para crear un diccionario a partir de dos listas de valores.
    #De esta forma la cantidad de veces que se repite una palabra queda asignada a la palabra en sí que se repite.
    diccionario=dict(zip(lista_mayus, contador_palabras))
    #metodo para ordenar diccionario teniendo en cuenta los valores. Si se quisiera ordenar con las claves, solamente haria falta el metodo "sorted()".
    diccionario_ordenado=sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)

    #se imprime por pantalla el diccionario ordenado de palabras repetidas
    for clave, valor in diccionario_ordenado:
        print('La palabra "', clave, '" sale', valor, 'veces.')


caracteres_sin_espacios, caracteres_con_espacios=contador_caracteres(texto)
numero_palabras, lista_palabras=contador_palabras(texto)
ranking=ranking_palabras(texto, lista_palabras)



