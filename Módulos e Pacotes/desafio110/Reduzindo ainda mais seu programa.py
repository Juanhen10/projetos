#Adicione ao módulo moeda.py criado nos desafios anteriores,
# função chamada resumo(), que mostre na tela algumas informações
# geradas pelas funções que já temos no módulo criado até aqui
from time import sleep
from moedas import resumo

while True:
    num = float(input('Digite um preço:R$ '))
    sleep(0.5)
    resumo(num)
    while True:
        resp1 = str(input('Quer continuar? [S/N]')).upper()
        if resp1 in 'SN':
            break
        print('Digite [S] / [N]')
    if resp1 == 'N':
        break
