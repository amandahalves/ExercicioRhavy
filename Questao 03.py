class fila:
  def __init__(self):
    self.pacientes = []
  def leght(self):
    return len(self.pacientes)
  def isEmpty(self):
    return len(self.pacientes)==0
  def enqueue(self,valor):
    if(self.leght())<20:
      self.pacientes.append(valor)
    else:
      print("O valor máximo de pacientes já atingiu")
  def dequeue(self):
    if(not(self.isEmpty())):
      self.pacientes.pop(0)

print("Quantidade máxima de pacientes é 20")
fila = fila()
i=1
while i<=25:
  fila.enqueue(i)
  i = i+1
  print()
print(fila.pacientes)
