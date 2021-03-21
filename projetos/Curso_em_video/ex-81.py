
lista=[]
while True:
    lista.append(int(input("Digite um numero:")))
    len(lista)
    ops= str(input("Continuar[s/n]"))
    if ops =='n':
        break
#fim laco
n2 = int(input("Digite o numero dessejado:"))

if n2 in lista:
    print(f"O valor {n2} buscado existe!")
else:
    print("O valor buscado nao existe!")

lista.sort(reverse = True)

print(lista)
print(f"{len(lista)}")