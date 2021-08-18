
![Imagen del código programado en Python 3.8](https://github.com/JnnAI/TheEgg/blob/master/Tarea_21/ImagenPrograma_Tarea_21.png)

Para comenzar con la explicación, quiero comentar que tengo nociones básicas de C++ y a la hora de hacer el diagrama de flujo de este proyecto, lo hice basándome en lo que sé de ese lenguaje, que después ‘’traduje’’ a Python 3.8, en un entorno de Visual Studio Code.

Después de mucho investigar he visto que hay cosas similares y otras que no tienen nada que ver, por ejemplo:

Líneas 3 a 11: Bucle contra numero erroneo

He programado un bucle para que cada vez que se inserte mal el número inicial, el programa vuelva a la línea que pide dicho número . De esta forma no hay que volver a lanzar el programa en caso de que a la primera se inserte mal el número. En lenguaje C++ hubiera usado un do-if, cosa que en python por lo que veo no existe como tal, por lo que que la forma más rápida que encontré es crear un while con booleano, para que cuando no se cumpla la condición que tiene dentro ( numero entre 0,0001 y 0,9999 ), se repita indefinidamente, hasta que se cumpla.

Línea 14: Mensaje de numero correcto

Una vez que se cumple la condición, aparece un mensaje de que el número es correcto y automáticamente comienzan los cálculos.

Líneas 16-17: Conversion de numerador y denominador a fracción no reducida.

La forma más sencilla para calcula la fracción creo que es convertir el numero decimal en un numero entero multiplicándolo por 10000 al mismo tiempo que se le coloca un denominador de 10000 también (es decir, que tengo una fracción no reducida del numero insertado).

Líneas 19-25: Cálculo de MCD en bucle para reducir la fracción.

En estas líneas lo que hay es un contador que va desde 1 hasta el valor que tiene el numerador, comprobando todas las divisiones que dan resto 0 tanto en el numerador como el denominador.

De esta forma lo que consigo es que cada vez que un mismo número es capaz de dividir a ambas partes de la fracción, la fracción se simplifique haciendo un barrido de todos los números comprendidos entre el 1 y el numerador (que es el que delimita el rango de opciones).

Una vez que el contador ha comprobado y utilizado todos los números posibles, aparece un mensaje (línea 29) que devuelve la fracción irreducible del numero insertado al principio.

Fin del programa.

FUNCIONAMIENTO:

Al ejecutar el programa te pide un número comprendido entre 0.0001 y 0.0009. Si el número es incorrecto, marca mensaje de error y vuelve a pedir el número, y así indefinidamente hasta que se inserte un número correcto.

Una vez que el número introducido está dentro del margen, el programa marca automáticamente un mensaje de que el número es correcto y seguido aparece el resultado de la fracción irreducible del número insertado.

Después de esto, el programa termina y habría que volver a ejecutarlo.

