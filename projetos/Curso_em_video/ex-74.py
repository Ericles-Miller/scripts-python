from random import randint

maior = menor =0
tups=(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),
      randint(1,100))
maior = menor = tups[0]
for i in range(0,5):
    if tups[i] > maior:
        maior= tups[i]
    else:
        menor = tups[i]

print("O numero maior e:{} \n O numero menor e:{}".format(maior, menor))

