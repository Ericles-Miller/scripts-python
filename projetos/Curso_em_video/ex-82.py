#criar uma lista q receba n numeros e criar duas listas seguintes em q uma tera pares e poutras impares

lista_geral = list()
lista_par = list()
lista_impar = list()

while True:
    
    lista_geral.append(int(input("Digite um numero:"))) 
    ops= str(input("Continuar?[s/n]"))
    
    if ops == 'n':
        break
#fim laco

for i in lista_geral:
    
    if  i%2 ==0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
#fim laco

print(lista_geral)
print(lista_par)
print(lista_impar)
    

