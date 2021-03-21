vel = int(input("Digite a velocidade do carro"))

if  vel >80:
    multa = (80 - vel)*(-7)
    print("O valor a ser pago e:{}",format(multa))

else:
    print("Velocidade abaixo do limite")