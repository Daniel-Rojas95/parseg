class nodo():
   
   def __init__(self, valor):
      self.valor = valor
      self.Izquierda = None
      self.Derecha = None
      pass
   
   def getArbol(self):
        strOut = ""
        strOut += f" NP[{self.valor}] "
        if type(self.Izquierda) != type(None):
            strOut += f" Izquierda[{self.valor}]->[{self.Izquierda}] "
    
        if self.Derecha is not None:
            strOut += f" Derecha[{self.valor}] ->[{self.Derecha}] "
    
        return strOut

def __str__(self):
    return f"valor: {self.valor} "