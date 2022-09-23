# Evaluacion_Tema_1

# Link del repositorio
Github: [https://github.com/paulaanb/Evaluacion_Tema_1]

# Ejercicio 1
La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
Ayuda
La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
 
# Ejercicio 2
Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

# Ejercicio 3
Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
·        Todos los números del 0 al 10 [0, 1, 2, ..., 10]
·        Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
·        Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
·        Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
·        Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Concepto útil
Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.


# Ejercicio 4
Crea un script llamado tabla.py que realice las siguientes tareas:
·        Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
·        El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
·        En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
·        El script contendrá un bucle for que itere el número de veces del primer argumento.
·        Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
·        Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.
·        Ejecuta el código y observa el resultado.
·        Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.


# Ejercicio Extra:
Resuelve y entrega este training de CodeWars
https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python

# Solucion Ejercicios 
# Ejercicio 1
    matriz = [ 
        [1, 1, 1, 3],
        [2, 2, 2, 7],
        [3, 3, 3, 9],
        [4, 4, 4, 13]
    ]

    matriz[1][-1] = sum(matriz[1][:-1])
    matriz[3][-1] = sum(matriz[3][:-1])

    print(matriz)

# Ejercicio 2
    cadena = input("Escribe una cadena de texto: ")
    print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10?",
        len(cadena) >= 3 and len(cadena) < 10 )
        if len(cadena) >= 3 and len(cadena) < 10:
            return True
        else:
            return False

# Ejercicio 3
    l1= [1:11]
    l2= [-10:1]
    l3= [0:21]
    l4= [-19:0]
    l5= [0:51]

    def is_sym(arr):
        if len(arr) < 2:
            return True
        elif arr[0] == arr[-1]:
            return is_sym(arr[1:-1])
        else:
            return False
    print(l1)
    print(l2)

    def lista_pares(n,m):
        if n > m:
            return []
        elif n%2==0:
            return [n] + lista_pares(n+1, m)
        else:
            return lista_pares(n+1, m)
    print(l3)
    print (l4)

    def lista_multiplos_de_cinco:
        return:
            True if valor % multiple == 0 
        else:
            False
    multiples_5=[]
    for i in range(0, 51):
    
        if multiple(i, 5):
            multiples_5.append(i)
    print ("Los multiples de 5 son:", multiples_5)

    #Otra forma de hacerlo sin usar recursividad

    print( list( range( 1, 11)))
    print( list( range( -10, 1)))
    print( list( range( 0, 21, 2 ) ) )
    print( list( range( -19, 0, 2 ) ) )
    print( list( range( 0, 51, 5 ) ) )

# Ejercicio 4
    import sys
    print(sys.argv)

    if len(sys.argv) == 3:
        filas = int(sys.argv[1])
        columnas = int(sys.argv[2])

        if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
            print("Error - Filas o columnas incorrectos")
            print("Ejemplo: tabla.py [1-9] [1-9]")
        else:
            for f in range(filas):
                print("")
                for c in range(columnas):
                    print(" * ", end='')

    else:
        print("Error - Argumentos incorrectos")
        print("Ejemplo: tabla.py [1-9] [1-9]")


# Ejercicio Extra

    import codewars_test as test
    from solution import string_to_array

    def string_to_array(s):
        return s.split(" ")