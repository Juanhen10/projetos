#faça um programa que leia  o peso de cinco pessoas. No final mostre qual foi o maior e
#menor pesos lidos
totmaior = 0
totmenor = 0
for a in range(1, 6):
    peso = int(input(f'Qual o peso da {a}º pessoa? KG'))
    if peso > 25:
        totmaior += 1
    elif peso < 25:
        totmenor += 1
print(f'Temos {totmaior} pessoas com pesos maiores')
print(f'E temos temos {totmenor} com pesos menores')
