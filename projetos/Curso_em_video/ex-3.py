#programa que faz a tabuada de um numero n

tabuada = int (input("Digite um numero:"))
res = int
for n in range(0,tabuada):
    res = n * tabuada
    print("{} X {} =".format(n,tabuada),res)

else:
    print("Fim do laco")
    import emoji
print( emoji.emojize("certou miseravi :sunglasses:",use_aliases=True))