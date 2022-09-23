# Evaluacion_Tema_1

# Link del repositorio
Github: [https://github.com/paulaanb/Evaluacion_Tema_1]

# ¿De que trata esta evaluacion?
Ejercicio 1
La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
Ayuda
La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
 

Ejercicio 2
Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

Ejercicio 3
Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
·        Todos los números del 0 al 10 [0, 1, 2, ..., 10]
·        Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
·        Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
·        Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
·        Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Concepto útil
Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.


Ejercicio 4
Crea un script llamado tabla.py que realice las siguientes tareas:
·        Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
·        El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
·        En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
·        El script contendrá un bucle for que itere el número de veces del primer argumento.
·        Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
·        Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.
·        Ejecuta el código y observa el resultado.
·        Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.


Ejercicio Extra:
Resuelve y entrega este training de CodeWars
https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python
