#Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade)
# em um dicionarios, se por acaso a CTPS for diferente de zero
# o dicionario recebera também o ano de contratação e o salario.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime
dados = {}
ano = datetime.today().year
dados['nome'] = str(input('Digite seu nome:'))
dados['anoNASC'] = int(input('Ano de nascimento: '))
dados['cpts'] = int(input('Carteira de Trabalho: '))
dados['idade'] = ano - dados['anoNASC']
if dados['cpts'] > 0:
    dados['salario'] = float(input('Qual salario?R$ '))
    dados['anoC'] = int(input('Quantos anos de contratado: '))
    dados['aposentadoria'] = ano - dados['anoC']
    if dados['anoC'] >= 35:
       dados['aposentadoria'] = (dados['idade'] - dados['aposentadoria']) + dados['idade']
       print(f'os dados foram {dados}')
       print(f'nome = {dados["nome"]}')
       print(f'idade = {dados["idade"]}')
       print(f'cpts = {dados["cpts"]}')
       print(f'Contratação = {dados["anoC"]}')
       print(f'Slario = {dados["salario"]}')
       print(f'aposentadoria = {dados["aposentadoria"]}')
    elif dados['anoC'] < 35:
        dados['aposentadoria'] = (dados['idade'] - dados['aposentadoria']) + dados['idade']
        print(f'os dados foram {dados}')
        print(f'nome = {dados["nome"]}')
        print(f'idade = {dados["idade"]}')
        print(f'cpts = {dados["cpts"]}')
        print(f'Contratação = {dados["anoC"]}')
        print(f'Slario = {dados["salario"]}')
        print(f'aposentadoria = {dados["aposentadoria"]}')
else:
    if dados['cpts'] == 0:
        print('Arrume um emprego se não vai demorar para você aposentar!')
        print(f'os dados foram {dados}')
        print(f'nome = {dados["nome"]}')
        print(f'idade = {dados["idade"]}')
        print(f'cpts = {dados["cpts"]}')
