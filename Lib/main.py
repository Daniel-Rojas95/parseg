from Lib import *

inOrderArr=[]
postOrderArr=[]
preOrderArr=[]

nodo1 = nodo(1)
nodo2 = nodo(2)
nodo3 = nodo(3)
nodo4 = nodo(4)
nodo5 = nodo(5)
nodo6 = nodo(6)
nodo7 = nodo(7)



linkHijo(nodo1, nodo2, nodo3)
linkHijo(nodo2, nodo4, nodo5)
linkHijo(nodo3, nodo6, nodo7)

LVR ( nodo1, inOrderArr )
LRV ( nodo1, postOrderArr)
VLR ( nodo1, preOrderArr)

print( "preOrder" )
print(  preOrderArr )
print( "postOrder" )
print( postOrderArr )
print( "inOrder" )
print( inOrderArr )

print(".............................")

arrnodos=[16,5,7,12,9,20,18,3,10,14]
nodoRaiz= None



for i in range(0, len(arrnodos), 1):
    if i == 0:
        nodoRaiz = nodo( arrnodos [i])
    else:
        nodosOrdenados(nodoRaiz, nodo (arrnodos[i]))
    
    pass
