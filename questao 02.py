class fila: 
  def __init__(self):
    self.Elementos = []
  def lenght(self):
    return len(self.Elementos)
  def isEmpyt(self):
    return len(self.Elementos)==0
  def Enqueue(self,valor):
    self.Elementos.append(valor)
  def Dequeue(self):
      if(not(self.isEmpyt())):
        self.Elementos.pop(0) 

Fila = fila()
Fila.Enqueue(3)
print(Fila.Elementos)