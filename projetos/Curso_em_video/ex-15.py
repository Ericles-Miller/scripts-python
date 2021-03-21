#locadora de carros

km = int (input("Quantodade de Km rodados:"))
dias = int(input("Quantodade de dias de locacao do carro:"))

preco_final = dias* 60 + km *0.15

print("O carro percorreu a quantidade de {}Km.\n A quantidade de dias de locacao foi:{}.\nO valor final a ser pago e: {}".format(km,dias,preco_final))