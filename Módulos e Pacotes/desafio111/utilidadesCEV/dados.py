
def resumo(num = 0):
    print('=' * 30)
    print(f'RESUMO DO VALOR.'.center(30))
    print('=' * 30)
    print(f'Preço analisado: {moeda(num)}')
    print(f'=' * 30)
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'aumentado em 20%: \t{aumetar(num, True)}')
    print(f'diminuir em 10%: \t{diminuir(num, True)}')
    print('=' * 30)
