
def linkHijo( nodoPadre, nodoHIjoIz=None, nodoHijoDer=None ):
    if nodoHIjoIz is not None:
        nodoPadre.Izquierda = nodoHIjoIz
    
    if nodoHijoDer is not None:
        nodoPadre.Derecha = nodoHijoDer
    pass


def LVR( Nodo, inOrderArr) :
    if nodo is not None:
        nodoPadre = Nodo
        LVR ( nodoPadre.izq, inOrderArr )
        inOrderArr.append( nodoPadre.valor )
        LVR ( nodoPadre.Der, inOrderArr)

    return inOrderArr 


   