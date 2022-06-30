#Crie um programa onde 4 jogadores joguem em um dado e tenham resultados aleatorios.
# Guarde esses resultados em dicionario. No final, coloque esse dicionario em ordem
# sabendo que o vencedor tirou o maior número
from random import randint
from time import sleep
from  operator import itemgetter
jogo = {'Juan': randint(1,6),
        'victor': randint(1,6),
        'Isa': randint(1,6),
        'Vitoria': randint(1,6)}
ranking = []
print('As jogadas foram:')
jogar = 't'
for k, v in jogo.items():
    print(f'\033[32m{k}\033[m jogou \033[31m{v}\033[m no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'{i+1}ºLugar: {v[0]} com {v[1]}.')
    sleep(1)
