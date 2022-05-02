
#faça um programa que leia  o peso de cinco pessoas. No final mostre qual foi o maior e
#menor pesos lidos
totmaior = 0
totmenor = 0
for a in range(1, 6):
    peso = float(input(f'Qual o peso da {a}º pessoa? KG'))
    if a == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi \033[34m{maior}KG\033[m ')
print(f'O menor peso lido foi de \033[32m{menor}KG\033[32m')
