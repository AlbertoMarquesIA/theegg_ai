# ENUNCIADO DE LA TAREA 21
Crea un programa que dado un número entre 0,0001 y 0,9999 (y de no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.

Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.

Nota: el programa no debe avisar al usuario con mensajes como "Introduzca un número". Debe leer directamente el número que introduzca el usuario. De igual modo, sólo debe mostrar la fracción irreducible encontrada, nada más. Tampoco debe hacer ninguna pausa antes ni después de la ejecución.

# SOLUCIÓN

Para resolver este ejercicio, se ha optado por crear dos funciones, una encargada de conseguir los divisores de un valor introducido y otra funcion encargada de conseguir el Divisor Común Máximo, de ahora en adelante referido como DCM.
En el programa principal, se pide introducir un valor y de este, y de la única constante en este ejercicio, el 10000 (esto ocurre por los limites en los valores, maximo entre 0,0001 y 0,9999), se obtienen sus divisores y a continuación en DCM. Para finalizar, se divide el valor inicial entre el DCM y se visualiza el resultado en forma de fracción.

# CÓDIGO

El problema se ha resuelto usando Python 3.9.0 y el IDE Visual Studio Code en OSx.

La solucion se encuentra en el fichero "Tarea_21.py" dentro de la carpeta "Tarea_21" y consta de dos  funciones y el programa principal, el cual se ejecuta en un bucle infinito.

En cuanto a la forma de uso, el programa simplemente espera a que el usuario introduzca un valor y responde con la fraccion irreducible. En caso de introducir un valor que no este dentro de los valores 0,0001 y 0,9999 el programa volverá a pedir que se introduzca otro valor. En caso de introducir caracteres o nada salta un mensaje de error.

Nota: Para poder ejecutar el ejercicio en linea a traves de Google Colab. (https://colab.research.google.com/drive/1nzUy3KWzlqXGSt3UD_tNfXdkpEu-DwTa?usp=sharing)