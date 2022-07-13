#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto, NEGADO, OPCIONAL ou OBRIGATORIO
# nas eleições
from datetime import datetime
idade = int(input('Que ano você nasceu?: '))
def voto(ano= 0):
    ano = datetime.today().year
    r = ano - idade
    if r >= 18 and r < 65:
        return print(f'com {r} anos: O voto é Obrigatorio')
    elif r < 16:
        return print(f'com {r} anos:Não precisa votar')
    elif r == 16 or r == 17 or r > 65:
        return print(f'com {r} anos:Voto opcional')


voto()
