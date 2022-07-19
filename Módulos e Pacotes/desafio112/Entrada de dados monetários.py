#Dentro do pacote utilidadesCeV que criamos no desafio 111,
# tem um modo chamado dado. Crie uma função chamado leiaDinheiro()
# que seja capaz de funcionar como a função input()
# mas com uma validação de dados para aceitar apenas valores que sejam monetários
from time import sleep
from utilidadesCEV import moedas
from utilidadesCEV import dados
while True:
    num = dados.leiadinheiro('Digite um preço:R$')
    sleep(0.5)
    moedas.resumo(num)
    while True:
        resp1 = str(input('Quer continuar? [S/N]')).upper()
        if resp1 in 'SN':
            break
        print('Digite [S] / [N]')
    if resp1 == 'N':
        break
