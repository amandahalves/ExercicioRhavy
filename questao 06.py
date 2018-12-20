fila = []

def Entra_avião(fila,v):
    fila.append(v)
    return fila

def Sai_avião(fila):
    fila.pop(0)
    return fila

def lista(fila):
    for aviao in fila:
        print(i)

def Avioes(fila):
    return len(fila)

for i in range(4):
  a = input("Diga o nome do avião e o seu ano: ")
  Entra_avião(fila,a)

print()


print(fila)
print("Seu primeiro avião já está pronto para a decolagem")
print("O tamanho da sua fila é:",(len(fila)))
print("Seu primeiro avião:",fila[0])
