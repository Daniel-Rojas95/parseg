
def linkHijo( nodoPadre, nodoHIjoIz=None, nodoHijoDer=None ):
    if nodoHIjoIz is not None:
        nodoPadre.Izquierda = nodoHIjoIz
    
    if nodoHijoDer is not None:
        nodoPadre.Derecha = nodoHijoDer
    pass


def LVR( nodo, inOrderArr) :
    if nodo is not None:
        nodoPadre = nodo
        LVR ( nodoPadre.izq, inOrderArr )
        inOrderArr.append( nodoPadre.valor )
        LVR ( nodoPadre.Der, inOrderArr)

    return inOrderArr 



def LRV( nodo, postOrderArr) :
    if nodo is not None:
        nodoPadre = nodo
        LRV ( nodoPadre.izq, postOrderArr )
        LRV ( nodoPadre.Der, postOrderArr )
        postOrderArr.append( nodoPadre.valor )

    return postOrderArr




def VLR( nodo, preOrderArr) :
    if nodo is not None:
        nodoPadre = nodo
        preOrderArr.append( nodoPadre.valor )
        VLR ( nodoPadre.izq, preOrderArr )
        VLR ( nodoPadre.Der, preOrderArr )
    return preOrderArr
        

###Nodos Ordenados
def nodosOrdenados( nodoPadre, nuevonodo ):
    if nuevonodo.valor < nodoPadre.valor: #Izquierda
        if nodoPadre.Izquierda is None:
            nodoPadre.Izquierda = nuevonodo
        else:
            nodosOrdenados(nodoPadre.Derecha, nuevonodo)
pass

#fin  de nuevos nodos


def printArbol( nodo ):
    if nodo is not None:
        nodoPadre = nodo
        print( nodoPadre.getArbol() )
        printArbol ( nodoPadre.Izquierda )
        printArbol (nodoPadre.Derecha )
    return 0