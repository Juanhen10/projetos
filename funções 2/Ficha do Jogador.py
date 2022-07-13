#Faça um programa que tenha uma função chamada ficha(),
# que receba dois parametros opcionais: O nome de um jogador e quantos gols ele marcou
# O Programa devera ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente
def ficha(nome = '', gols = 0):
    print(f'o Jogador {nome} fez {gols} gols no campeonato ')


jogador = str(input('Nome do jogador: '))
g = str(input('Gol do jogador: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == '':
    ficha(gols= g)
else:
    ficha(jogador, g)
