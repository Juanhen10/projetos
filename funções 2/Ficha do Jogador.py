#Faça um programa que tenha uma função chamada ficha(),
# que receba dois parametros opcionais: O nome de um jogador e quantos gols ele marcou
# O Programa devera ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente
def ficha(nome = '', gols = 0 ):
    if nome not in '' or gols > 1:
        print(f'o jogador, {nome} fez {gols} gols')
    if nome == '':
        print(f'o jogador <jogador desconhecido> fez {gols}')

ficha('juan', 28)
ficha('', 5)
ficha()
