#**Compresión LZ77**

El codigo se divide en varias funciones:

**Crear diccionario:**
Crea un diccionario del mensaje recogido por el input.
El diccionario almacena las combinaciones de letras repetidas a modo de claves, de forma que una frase con silabas repetidas entre si, convierte las silabas que se repiten en texto mas corto, consiguiendo que el mensaje ocupe menos espacio.

**Comprimir:**
Comprime el mensaje con el metodo LZ77.

**Descomprimir:**
Descomprime el mensaje anterior usando el diccionario generado en la compresión. Sin él, sería imposible descomprimir el mensaje.

**Input_mensaje:**
Recoge el input que se va a usar para comprimir, en formato String.

