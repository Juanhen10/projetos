#Desafio107 crie um módulo chmado moeda.py
# que tenha as funções aumentar(), diminuir(), dobro() e metade()
from moedas import dobro,diminuir,metade,aumetar
while True:
    num = int(input('Digite um preço:R$ '))
    print(f'O dobro do dinheiro é {dobro(num)}')
    print(f'Diminuindo o dineiro em 10%:R${diminuir(num)}')
    print(f'A Metade do dinheiro é: {metade(num)}')
    print(f'Ao aumentar o dinheiro em 10%: R${aumetar(num)}')
    while True:
        resp1 = str(input('Quer continuar? [S/N]')).upper()
        if resp1 in 'SN':
            break
        print('Digite [S] / [N]')
    if resp1 == 'N':
        break

