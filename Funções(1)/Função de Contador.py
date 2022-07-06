#Faça um programa que tinha uma função chamada contador() que receba três parametros:
# inicio,fim e passo e ralize a contagem
# Seu programa tem que realizar três contagens atráves da função criada:
# A- De 1 até 10, de 1 em 1
# B- de 10 a´te 0, de 2 em 2
# C - de uma contagem personalizada
from time import sleep
num = 0
def contador():
    print(f'pulando de um em um')
    for c in range(1,11):
        #sleep(0.7)
        print(f'{c} ',end='')
    print()
    print(f'-' * 30)
    print('Pulando de 2 em 2 de 10 até 0')
    for d in range(0,11,2):
        #sleep(0.7)
        print(f'{d} ',end='')
    print()
    print(f'-' * 30)
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('A contagem personalizada será...')
    sleep(0.8)
    print(f'Contagem de {inicio} até {fim} contando de {passo}')
    for c in range(inicio, fim, passo):
        sleep(0.8)
        print(f'{c} ', end='')
    if passo ==0:
        passo = 1
        print('A contagem personalizada será...')
        sleep(0.8)
        print(f'Contagem de {inicio} até {fim} contando de {passo}')
        for c in range(inicio, fim, passo):
            sleep(0.8)
            print(f'{c} ', end='')
    if passo < 0:
        passo *= -1
        for c in range(inicio, fim, passo):
            sleep(0.8)
            print(f'{c} ', end='')


print(f'-'*30)
contador()
