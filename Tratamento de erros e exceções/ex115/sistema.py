#CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS PELO SEU NOME E IDADE
# EM UM ARQUIVO DE TEXTO SIMPLES.
# O SISTEMA SÓ VAI TER 2 OPCÇÕES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS
from lib1.interface.desafio115a import *
from lib1.arquivo.desafio115b import *
from time import sleep

arq = 'nomeidade.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['para mostrar a lista das pessoas', 'para criar novo cadastro','para sair'])
    if resposta == 1:
        # opção de listar um conteudo de m arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('\033[31mSaindo do Sistema...até logo\033[m')
        break
    else:
        print(f'\033[31mERRO! digite uma opção válida!\033[m')
    sleep(2)

