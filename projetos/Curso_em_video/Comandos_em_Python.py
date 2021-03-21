#bibliotecas 
sintaxe para todos os itens da biblioteca
'''import nome da biblioteca'''

sintaxe para um elemnto da biblioteca
''' from nome da biblioteca import nome do comando '''


#funcao inicial 
def main():
    #codigo 
    
main()


print("ola mundo") #print na tela

print(5+7) # nao e necessario declarar var 

print("teste",5) #outro tipo de notacao

'''nome = 'ericles' #declaracao de var para string entre aspas
idade = 22 #nome dar var e valor na forma que deseja por ex: inteiro
peso= 63.5 

print( peso, idade, nome) '''

input # comando de leitura 

#sintaxe
nome = input('qual o seu nome?') 

peso = input('Digite seu peso:') # com aspas simples

idadde = input('Digite sua idade:')

#comandos para declarar variaveis
'''nome_da_var = tipo_var(input('descricao....'))'''

#ex: numero = int(input("qual seu numero"))

# comando para printar dados
'''print("a soma de {} e {} e igual a {}".format(n1,n2,n3))'''
''' semelhante a %d %f etc'''

#teste de converter valores se for possivel
print(ver.isalpha())
print(var.isnumeric())
print(var.isalnum())

# Operadores em python
+ adicao
-subtracao
*multiplicacao
/divisao
//div inteira
**potencia
% resto da divisao

#biblioteca math
ceil usa para arredondar a nota para cima
floor idem para baixo -> flor(var)
pow potencia  -> 
sqrt raiz quadrada -> var = math.sqrt(var2)
trunc elimina todos os numeros antes da virgula -> mesma coisa
factorial fatorial

#biblioteca Random 
gera numeros aleatorios para vetores etc
random.randint(n1, n2) valeres aleatorios  entre n1 e n2
random.random '''numeros aleatorios'''

import emoji

/////////////////////////////////////////////////////////////////
manipulacao de strings 
print(""" casascascascsa""") usado para textos longos
frase = '' -> frase normal
print(fras[9)] -> caractere na posicao 9
print(frase[9:13]) pega os caracteres do 9 ao 12(uma casa antes)
print(frase[9:21:2]) -> PERCORRE A STRING PULANDO DIAS CASAS
print(frase(:5) -> percorre de 0 a pos 5
print(frase(15:) ->comeca na pos especificada e termina ate o final da string
#comprimento da string 
lean(frase) 
#quantidade de vezes que um caractere apareceu
print(frase.count('o'))
print(frase.count('o',0,13)
#qtd a silaba ba na string
print(frase.find('ba')  -- obs(se nao existir essa silaba return -1)
#existe tal palavra na string
print("curse" in frase)
#troca de palavra por outra dentro da string
print(frase.replace("teste","teste2")
#transformar em maiusculas ou minusculas
print(frase.upper()
print(frase.lower()
print(frase.capitalize -> deixa so a primeira maiscula
print(frase.title ->capitaliza palavra por palavra
print(frase.strip -> remove os espacos vazios
print(frase.rstrip ->lado direito(os ultimos vazios)
print(frase.lstrip ->lado esquerdo(os ultimos vazios)
frase.split() ->elimina os espacos e divide as palvras em outras strins 
'-'frase.join -> processo reverso acima

#comandos de desvio
If else

#sintaxe
if ver == x:
    print("sfsdfsdfsfsfs")
else: print("gdgdgdfgdfg")

else if 

#comando de repeticao for
for var in range(0,3)
ex:
for i in range(0,3):
    print("oiiiieee")

obs:A identacao pertencente ao for deve ficar dentro dele para ser consodereado 
pertencente a ele para nao pertencer a ele deve-se colocar alinhado a ele
exe

for i in range(0,10)
    print("pertence ao for")

print("Nao pertence ao for")
''' quando precisar percorrer por passos  '''

for i in range(i,numero de saltos, p)
ex:
for i in range(0 ,2 ,10)
    print(i)
    
#comando de repeticao while

''' while c< x 
    faca
'''

ex: 
    while  i<10 
        print

#while com break(do while)


#tuplas
OBS: AS TUPLAS SAO IMUTAVEIS DEIFERENTES DO VETORES
AS TUPLAS RECEBEM DADOS DE VARIAVEIS DISTINTTAS

TUPLA = ('eu','fulano', 'ciclano') ou sem parenteses
num = (int(input("Numero:")),int(input("numero")), ...)
print(TUPLA) mostra o TUPLA int  eiro(sem precisar de contador) 
print(TUPLA[i]) ou print(TUPLA[numero])
print(TUPLA[1:5]) da posicao 1 ate a 5
print(TUPLA[:2]) da posicao 0 ate antes de 2
print(TUPLA[2:]) da posicao 2 ate antes de fim
print("O nome de fulano e: {tupla[i]}") para usar no print  

obs: Quando for percorre temos duas opcoes:
for cont in range(0,len(TUPLA)):
    print("dadsadasdsad")
ou 
for cont in TUPLA

for cont in enumerate(TUPLA)  usa para enumerar 

unundo tuplas
a= (2,4,5)
b= (5,5,9)
c= b+a

comandos de tuplas
print(c.count(numero)) numero de vezes que aparecera o numero exigido
print(c.index(numero))  posicao do numero exigido
del(c) apaga a tupla inteira
 
#listas 
obs: as listas sao mutaveis

lista= [1,2,3,4,5] com colchete para diferenciar da TUPLA
print(lista[3])

#comandos
lista.insert(0,valor) -> serve para adicionar itens na lista em determinada posicao
del lista[posicao] -> apaga um elemento da lista
lista.pop[pos] -> apaga um elemnto da lista
lista.remove(nome do valor) -> apaga determinado item da lista desejado pelo usuario
lista.append(valor) -> add valores na lista

#criando listas a partir do range

valores= lista(range(4,11)) -> add valores de 4 a 11  nas posicoes 
de 0 a 6(vai de 0a 6 pq sao a quntidades de numeros estabelecida pelo range )
valores.sort() -> ordena os valores em ordem crescente
valores.sort(reverse = True) -> ordena de forma decrescente

''' percoreendo valores na lista'''
for v in valores:  -> 
for c, v in enumerate(valores): -> mostra os lementos da lista e sua posicao
lista [-1] final da lista
len(lista) percorre as pos da lista de determinado valor determinado pelo len
''' recebendo valores pelo usuario'''
for i in range(0, n):
    valores.append(int(input('digite um numero:')))

'''MANIPULACAO DE LISTAS'''
OBS: QUANDO EU IGUALO UMA LISTA A OUTRA ( A=B) ELAS SAO IGUAIS PARA QUALQUER MUDANCA
ex: a = [1,2,3,4,5]
b=a
b[2] = 20 
esse valor na posicao 2 aplicara para a lista a tambem
ex na pratica:
a = [1,2,3,4,5]
b=a
b[2] = 20
print(f"lista A:{a}") (f significa formatado)
print(f"lista B:{b}")

'''fazendo uma copia mas sem ligacao '''
a = [1,2,3,4,5]
b=a[:]

'''condicoes em python'''
if 5 in lista -> se existe tal valor em lista


#dicionarios ou structs

dados= { dados dentro}

add elementos
ex: dado[nome] = 'mario'
deletando elementos da struct
ex: del dados['idade']
ex:
print(dados['nome'])
OBS: OS DADOS PODEM SER SALVOS IGUAIS A STRUCT NO C
ex:
filme = {
    'title':"valor"
     'ano': 1999
    diretor: fulano de tal
}

#acessasndo valores da struct
print(filme.values())
#acessando as var da struct
print(filme.keys())
# acessando osm dois
print(filme.items())

#percorrendo as structs
for k, v in filmes.itens():
    print(f"o {k} e {v}") #vai mostrar k as var e o v os valores dela
por casa
for k in filme.keys(): #mostra as var da struct

for k in filme.values(): #mostra os valores

for k , v in filmes.itens(): # mostra tudo
#struct dentro de lista
print(locadora[0]['ano'])
brasil = []
estado1= {'uf':"dadasda","sigla":"rj"}
estado2 = {mesma coisa}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[i]['sigla'])
#recebendo dados do teckado

estado1['utf']=str(input("adssfsdfds"))

#fazendo uma copia do dicionario
brasil.append(estado1.copy())


#----------Funcão----------

#declarar função
def nome_da funcao(paraametros):