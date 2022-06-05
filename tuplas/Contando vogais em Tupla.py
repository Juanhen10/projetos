#Crie um progrma que tenha uma tupla com varias palavras (não usar acentos)
# Depois disso, você deve mostra, para cada paçavra quais suas vogais
palavras = ('carro',
            ' jogo',
            'casa',
            'Bolsa',
            'bala',
            'linda',
            'lobo',
            'cavalo',
            'rato',
            'tigre')
for pos in palavras:
    print(f'\nNa palavra {pos} temos as vogais:', end=' ')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(f"\033[32m{letra}\033[m",end=' ')
