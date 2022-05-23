#Faça um programa que jogue par ou impar com o computador
# O jogo será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas
# que ele conquistou no final do jogo.
from random import randint
num = totv = soma = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0 , 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            totv +=1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            totv += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar de novo!')
print(f'Você perdeu e ganhou {totv}')
