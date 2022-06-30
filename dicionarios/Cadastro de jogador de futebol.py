#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feito em cada partida.
# No final tudo isso será guardado em um diocionario, incluindo o total de gols feitos durante o campeonato
dados = {}
cont = 0
print(f'\033[34m▬\033[m' * 30)
dados['jogador'] = str(input('Qual jogador? '))
dados['Partidas'] = int(input('Quantas partidas: '))
print(f'\033[34m▬\033[m' * 30)
for c in range(dados['Partidas']):
    dados['gols'] = int(input(f'Quantos gols na {c+1}º partida: '))
    dados['ass'] = int(input(f'Quantas assistencias na {c+1}º partida: '))
    print(f'\033[31m▬\033[m' * 30)
    dados['totG'] = dados['Partidas'] + dados['gols']
    dados['totA'] = dados['Partidas'] + dados['ass']
    cont += 1
print('•' * 30)
print(tot.append(dados.copy()))
print('•' * 30)
print(f'nos dados jogador = {dados["jogador"]}')
print()
print('•' * 30)
print(f'O jogador \033[32m{dados["jogador"]}\033[m em \033[31m{dados["Partidas"]}\033[m partidas ')
print(f'fez \33[35m{dados["totG"]-1}\033[m gols e \033[33m{dados["totA"]-1} assitencias\033[m')
print('•' * 30)
