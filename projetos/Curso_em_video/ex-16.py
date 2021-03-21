#programa que le um numero real e mostra a sua parte inteira

import math 
num = float(input("Numero:"))
num2 = math.trunc(num)

print("Numero {}. Sua parte inteira {}".format(num, num2))

