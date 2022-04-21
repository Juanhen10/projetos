#Faça um program qye leia o ano de nascimento de um jovem e informe, de acordo com a idade:
#Se ele ainda vai vai se alistar ao serviço militar
#se é a hora de se alistar
#se já passou do tempo do alistamento.
#Seu programa tambe deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
data = int(input('Coloque o ano que nasceu: '))
ano = date.today().year
idade = ano - data
print(f'Quem nasceu em {data} tem {idade}anos')
if idade <= 17:
    saldo = 18 - idade
    print(f'Você ainda vai se alistar falta {saldo}.')
elif idade == 18:
    print('É hora de se alistar')
elif idade > 18:
    saldo = idade - 18
    print(f'Já passou da hora de se alistar, você está atrasado {saldo}anos')
