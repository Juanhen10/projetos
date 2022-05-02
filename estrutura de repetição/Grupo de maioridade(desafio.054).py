#crie um programa que leia o ano de nascimento de sete pessoas.
#NO final, mostre quantas pessoas ainda não atigiram a maioridade e quantas
#já são maiores
from datetime import date
totmaior = 0
totmenor = 0
for a in range(1,8):
    idade = int(input(f'Em que ano a {a}º nasceu? '))
    atual = date.today().year
    ano = atual - idade
    if ano >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores')
print(f'E tivemos {totmenor} pessoas menores')
