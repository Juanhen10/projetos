#faça um programa que leia um numero inteiro e diga se ele
# é primo ou não um número primo
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end="")
        tot +=1
    else:
        print("\033[31m", end='')
    print(f'{c}', end=" ")
print(f'\033[35mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso que ele é PRIMO')
else:
    print('Por isso ele não é primo')
