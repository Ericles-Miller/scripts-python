#soma dos numeros pares de 0 a 50 e impares

soma = 0
soma2 = 0


for i in range(0,51):
    if i%2==0:
        soma = soma +i

else :
    soma2= soma2 + i

print("A soma dos numeros pares: {}\n A soma dos numeors impares: {}".format(soma,soma2))