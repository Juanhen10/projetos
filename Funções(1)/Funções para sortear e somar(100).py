#Faça um programa que tenha uma lista chamada números e duas funções.
#Chamadas sorteia() e somaPAR(). A primeira função vai sortear 5 números e coloca-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior
from random import randint
from time import sleep

numeros = []
def sorteia():
    sleep(0.4)
    print('Números sendo sorteados...')
    for c in range(0,5):
        sleep(0.4)
        c = randint(0,10)
        numeros.append(c)
        print(f'{c} ', end='')
    print()

def soma():
    soma = 0
    par = 0
    for i,v in enumerate(numeros):
        if v % 2 == 0:
            par += v
            soma += v
    print(f'A soma dos valores pares é: {soma}')


sorteia()
soma()
