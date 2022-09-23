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

#Otra forma de hacerlo sin usar recursividad usando range()

print( list( range( 1, 11)))
print( list( range( -10, 1)))
print( list( range( 0, 21, 2 ) ) )
print( list( range( -19, 0, 2 ) ) )
print( list( range( 0, 51, 5 ) ) )

#Otra forma de hacerlo usando recursividad.(No puedo comprobar que el codigo funciona porque mi ordenador no compila.)
def lista_recursividad(n, m):
    return 1 if n == 0 else  [n] + lista_recursividad(n+1, m)
def lista_recursividad(self):
    self.assertEqual(0,lista_recursividad(21))
    self.assertEqual(-19,lista_recursividad(0))
    self.assert(1,11)
    self.assert(-10,1)
    self.assertmultiples_5.append(0,51)
    