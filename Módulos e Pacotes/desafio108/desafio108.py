#Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga
# mostrar os valores como um valor monetário formatado
from moedas import dobro,diminuir,metade,aumetar, moeda
while True:
    num = float(input('Digite um preço:R$ '))
    print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
    print(f'Diminuindo o dineiro em 10%: {moeda(diminuir(num))}')
    print(f'A Metade do dinheiro é: {moeda(metade(num))}')
    print(f'Ao aumentar o dinheiro em 10%: {moeda(aumetar(num))}')
    while True:
        resp1 = str(input('Quer continuar? [S/N]')).upper()
        if resp1 in 'SN':
            break
        print('Digite [S] / [N]')
    if resp1 == 'N':
        break


