![enter image description here](https://github.com/JnnAI/TheEgg/blob/master/Tarea_22/CapturaTarea_22Jnn.png)

NOTA: El programa esta desarrollado con Python 3 a traves de Visual Studio Code.

A continuación comienzo con la explicación del programa que resuelve el algoritmo del lechero.
He colocado los datos del enunciado directamente en el programa de forma que se puedan editar para probar diferentes resultados. El programa no pide la inserción manual de parámetros para ahorrar tiempo, pero en caso de que sea necesario, lo puedo implementar.




Línea 22:
Se define la función con las 4 variables que se cree que hacen falta para llevar a cabo el problema, las cuales son:
capacidad que tiene el camión (capacidad_camion), los pesos de las vacas (pesos_vacas) en formato lista, los litros de leche (litros_leche) que produce cada una, y el numero de vacas que hay en total (n).

Fila 26-30:
El primer paso dentro de la función es la de crear e inicializar una matriz del tamaño [x+1][y+1] donde x es la cantidad de vacas, y la y es el peso máximo que puede llevar el camión.
De esta forma, la lista de pesos de vacas corresponde a uno de los ejes de la matriz, y el peso máximo que puede llevar el camión (desde 0 hasta el peso máximo, con un contador que suma de 1 en 1) al segundo eje de la matriz.
Y diremos... porque la matriz es de [x+1][y+1] y no de [x][y] pues la respuesta es porque la matriz que vamos a inicializar tiene los valores iniciales (peso vacas y peso maximo de camion) en la fila 1 y en la columna 1, de forma que necesitamos ampliarla una fila y una columna por cada lado.
Resumiendo, desde la fila 26 a la 30 se inicializa una matriz con valores nulos.

Linea 34:
A partir de esta linea comienzan los bucles de la funcion.
El for que se encuentra en esta linea se encarga de incrementar el contador i de 1 en 1 hasta completar n+1 valores. De esta forma recorremos la lista de vacas de 1 en 1.

Linea 38:
Este segundo for se encuentra anidado dentro del primero, de forma que hasta que este segundo no acaba, el primero no incrementa el valor de su contador.
Este segundo for lo que hace es recorrer la columna de pesos maximos que puede llevar el camion a traves del contador w. Ademas tiene 3 condiciones dentro:

- Linea 41
		Si ambos contadores son cero, la matriz en esa posición coge el valor de cero también.
- Linea 45
		Si la anterior no se cumple, comprueba esta siguiente.
		Si el peso de la vaca en la posicion anterior es menor o igual al peso de la vaca en la posicion actual, la matriz se rellena en esa posición con el valor que sea mas grande entre el valor actual o la suma de valores hasta el momento. De esta forma la matriz siempre va a estar rellena con el valor más alto posible.
- Linea 49
	Si no se cumple ninguna de las anteriores, la matriz se rellena con el valor de la posición anterior.

Linea 52:
La matriz devuelve el valor en la posición designada

Linea 57:
Se insertan los datos directamente dentro del programa de forma que en caso de querer editarlos esten disponibles sin necesidad de meterlos manualmente.

Linea 63:
En esta linea se imprime en pantalla el resultado conseguido con la funcion del lechero.
Lineas mas adelante se encuentran otros 4 bloques de datos con sus respectivas impresiones de pantalla, por tener mas variedad.

Muchas gracias!
