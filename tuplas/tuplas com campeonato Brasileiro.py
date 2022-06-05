#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato Brasileiro de Futebol, na
# Ordem de colocação. Depois mostre:
# A - apenas os 5 priemiros colocados.
# b - os últimos 4 colocados da tabela.
# C - Uma lista com com os times em ordem alfabetica
# D - Em que posição na tabela está o  time do São Paulo
time = (" ",'Corinthians','Palmeiras','São Paulo','Atletico Mineiro','Botafogo','Santos','Fluminense','Coritiba','America-MG',
        'Avai','Internacioonal','Athletico-PR','Bragantino','Flamengo','Goias','Cuiaba','Atletico-GO',
        'Juventude','Ceara SC','Fortaleza')
print(f'\033[32m=' * 50)
print(f'\033[36messes são os time do brasileirão 2022!')
for pos, co in enumerate(time):
    print(f'{pos} -- {co}')
print(f'\033[32m=' * 50)
print(f'\033[33mos 5 primeiros colocados são {time[1:5]}\033[m')
print(f'\033[32m=' * 50)
print(f'\033[31mos 4 ultimos são {time[-4:]}\033[m')
print(f'\033[32m=' * 50)
print('\033[35mem ordem alfabetica os time ficarão',sorted(time))
print(f'\033[32m=' * 50)
for pos, time in enumerate(time):
    if pos == 2:
        print(f'\033[38mO \033[31mSão paulo\033[m se encontra na {pos}º posição! ')







