dados = dict()
lista = list()
lista_f= list()
lista_I= list()
media = 0
while True:   
    dados['nome']= str(input("Digite seu nome:"))
    dados['idade']= int(input("Digite sua idade:"))
    dados['sexo']= str(input("Digite seu sexo:"))
    if dados['sexo']== 'f':
        lista_f.append(dados['nome'])
    lista.append(dados.copy)

    ops=int(input("Digite a opcao:"))
    if ops == 0:
        break  
print(lista_f)

for i in dados:
    media+= dados['idade'] 

media = media/len(dados)

for i in dados:
    if dados['idaade'] < media:
        lista_I.append(dados['nome'])

#print(dados)
#lista.append(dados.copy())
