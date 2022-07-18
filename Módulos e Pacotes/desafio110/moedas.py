def aumetar(num = 0, formato = False):
    res = num * 1.20
    return res if formato is False else moeda(res)

def diminuir(num = 0, formato = False):
    res = num * 0.10
    return res if formato is False else moeda(res)


def dobro(num= 0, formato = False):
    res = num * 2
    return res if formato is False else moeda(res)

def metade(num = 0, formato = False):
    res = num / 2
    return res if formato is False else moeda(res)

def moeda(num=0, moeda = "R$"):
    return f"{moeda}{num:.2f}".replace('.',',')


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
