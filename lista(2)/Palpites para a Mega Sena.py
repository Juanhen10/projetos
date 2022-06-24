#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogos, cadastrado tudo em uma lista composta
from random import randint
from time import sleep
lista = []
dados = []
print('-'* 30)
print('Tente a sorte')
print('-' * 30)
jogo = int(input('Quantos jogos: '))
tot = 1
while tot <= jogo:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    dados.append(lista[:])
    lista.clear()
    tot +=1
print(f'\033[31mSorteando. Boa Sorte!\033[m')
sleep(1)
for i, l in enumerate(dados):
    sleep(1)
    print(f'\033[32mJogo {i}: {l}\033[m')

