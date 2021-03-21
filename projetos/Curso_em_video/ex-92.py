dados = dict()

dados['nome']= str(input("Digite seu nome:"))
dados['idade']= int(input('Digite sua idade:'))
dados['ctps']= int(input("Digite sua carteira de trabalho:"))

if dados['ctps'] !=0:
    dados['ano_d_contrato']=str(input("Qual foi o ano de contrato:"))
    dados['salario']= float(input("Digite sue salario:"))

dados['aposenta'] = 60 - dados['idade']


print(f"O funcionario {dados['nome']} aposentara em {dados['aposenta']} anos de idade com o salario de {dados['salario']} reais!")

