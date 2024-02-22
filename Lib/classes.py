class nodo():
   
    def getArbol(self):
        strOut = ""
        strOut += f" NP[{self.valor}] "
        if type(self.Izquierda) != type(None):
            strOut += f"[{self.valor}]->[{self.Izquierda}]"
    
        if self.Derecha is not None:
            strOut += f" [{self.valor}] ->[{self.Derecha}] "
    
        return strOut

def __str__(self):
    return f"Valor: {self.valor}"