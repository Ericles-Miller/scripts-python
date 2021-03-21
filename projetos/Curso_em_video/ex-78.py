#cadastrar numeros em uma lista. os numeros nao podem repetir
lista=[]

while True:
    n= int(input("Digite um numero:"))
    if n in lista:
        print("O valor ja exite na lista!")
    else:
        lista.append(n)
    ops=str((input("Deseja add outro valor a lista?[s/n]")))
    if ops == 'n':
        break
print(lista)
    
    