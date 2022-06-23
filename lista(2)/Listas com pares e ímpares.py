#Crie um programa onde o usuario possa digitar sete valores númericos
# e cadstre-os em uma lista unica
#Que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e ímpares em ordem crescente
num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('☼' * 30)
num[0].sort()
num[1].sort()
print(f'o valores em par {num[0]}')
print(f'os valores em impar {num[1]}')
