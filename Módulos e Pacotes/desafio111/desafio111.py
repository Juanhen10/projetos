#Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado.
#Transfira todas as funções utilizadas nos desafio 107,108 e 109 para o primeiro paco e mantenha tudo funcionando.
from time import sleep
from utilidadesCEV import moedas
while True:
    num = float(input('Digite um preço:R$ '))
    sleep(0.5)
    moedas.resumo(num)
    while True:
        resp1 = str(input('Quer continuar? [S/N]')).upper()
        if resp1 in 'SN':
            break
        print('Digite [S] / [N]')
    if resp1 == 'N':
        break