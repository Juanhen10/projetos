#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro  a mais.
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108
from moedas import dobro,diminuir,metade,aumetar, moeda
while True:
    num = float(input('Digite um preço:R$ '))
    print(f'O dobro de {moeda(num)} é {dobro(num, True)}')
    print(f'A Metade do dinheiro é: {metade(num, True)}')
    print(f'Diminuindo o dineiro em 10%: {diminuir(num, True)}')
    print(f'Aumentando o dinheiro em 20%: {aumetar(num, True)}')
    while True:
        resp1 = str(input('Quer continuar? [S/N]')).upper()
        if resp1 in 'SN':
            break
        print('Digite [S] / [N]')
    if resp1 == 'N':
        break
