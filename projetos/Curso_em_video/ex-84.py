#ler peso e nome de x pessoas e guardar numa lista.quantas foram cadastradas as mais oesadads e leves

lista= []
matriz = []
maior= menor = 0
while True:
    lista.append(str(input("Digite seu nome:")))
    lista.append(int(input("Digite seu peso:")))
    if len(matriz) == 0:
        menor = maior = lista[1]
    elif maior < lista[1]:
        maior = lista[1]
    elif menor > lista[1]:
        menor = lista[1]
    matriz.append(lista[:])
    lista.clear()

    ops=str(input("Continuar?[s/n]"))
    if ops == 'n' or ops =='N':
        break
#fim laco



print(matriz)
print(len(matriz[1]))
print(maior)
print(menor)

