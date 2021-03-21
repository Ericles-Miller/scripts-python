#criar uma lista e colocar separadamente os n pares e impares

lista = [[],[]]


for i in range (0,5):
    n = int(input("Digite um numero:"))
    if n % 2 == 0:
        lista[0].append(n)
     #   l_par.clear()
    else:
        lista[1].append(n)
       # l_impar.clear()
lista[0].sort()
lista[1].sort()
print(lista)