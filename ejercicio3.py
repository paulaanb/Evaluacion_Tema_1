l1= [1:11]
l2= [-10:1]
l3= [0:21]
l4= [-19:0]
l5= [0:51]

print( list( range( 1, 11)))
print( list( range( -10, 1)))
print( list( range( 0, 21, 2 ) ) )
print( list( range( -19, 0, 2 ) ) )
print( list( range( 0, 51, 5 ) ) )

def is_sym(arr):
    if len(arr) < 2:
        return True
    elif arr[0] == arr[-1]:
        return is_sym(arr[1:-1])
    else:
        return False
def lista_pares(n,m):
    if n > m:
        return []
    elif n%2==0:
        return [n] + lista_pares(n+1, m)
    else:
        return lista_pares(n+1, m)
