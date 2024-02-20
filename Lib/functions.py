
def linkHijo( nodoPadre, nodoHIjoIz=None, nodoHijoDer=None ):
    if nodoHIjoIz is nor None:
        nodoPadre.Izquierda = nodoHIjoIz
    
    if nodoHijoDer is not None:
        nodoPadre.Derecha = nodoHijoDer
    pass


def LVR( Nodo, inOrderArr):
    nodoPadre = Nodo
    nodoHijo = None


    if nodoPadre.Izquierda is not None:
        nodoHijo = nodoPadre.Izquierda
        inOrderArr.apped( nodoHijo.valor )
        pass

    in