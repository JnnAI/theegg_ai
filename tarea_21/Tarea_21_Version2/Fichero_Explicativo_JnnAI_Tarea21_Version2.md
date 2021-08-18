![enter image description here](https://github.com/JnnAI/TheEgg/blob/master/Tarea_21/Tarea_21_Version2/Imagen%20del%20programa.PNG)

Tal y como se observa en la nueva imagen, se han modificado varias líneas de código con el fin de solucionar el error al insertar caracteres en una variable numerica.

Para comenzar con la nueva explicación:

Línea 2:
He declarado un valor 0 para la variable 'numero' que va a ser la que recoja el dato de entrada. De esta forma evito que al entrar al bucle While, salga un error de que la variable no ha sido declarada.

Línea 3-16:
En estas líneas se han insertado las nuevas líneas de código para solucionar el error mencionado anteriormente.
Una vez que el programa entra en el While con booleano, he creado un Try con excepción, de forma que el mensaje emergente que salga siempre que haya error sea el de 'Introduce un número...' y este valor sea recogido con un Float.
La excepcion de la linea 7 genera que cuando el valor introducido en la linea anterior no es de tipo numerico, detecta el error y devuelve un mensaje de: 'El valor introducido debe ser un número'. Y comienza de nuevo el bucle, pidiendo un nuevo numero.

En las siguientes lineas hasta la 16 lo que se hace es colocar 2 condiciones, que si se cumple la primera, el programa sale del bucle con un Break y sino, marca error y vuelve a empezar el bucle.

Todo lo demás del programa está igual que la version anterior.
