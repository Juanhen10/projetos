#melhore o jogo do desafio 028 onde o computar "pensa" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinha até acertar
#mostrando no fianl quanto paçpites foram necessarios para vencer.
from random import randint
pc = randint(0,10)
a = int(input('escolha um numero de 0 a 10: '))
a = 0
tot = 0
while a != pc:
    print('\033[31m----- ERROU! -----\033[m')
    again = int(input('\033[31mTente de novo:\033[31m '))
    a += 1
    if a == pc:
        tot += 1
        print(f'\033[32mVocê acertou! com {a} tentativas\033[m')
    else:
        print('Eu ganhei!!')
        
