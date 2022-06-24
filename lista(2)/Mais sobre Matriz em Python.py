#Aprimore o desafio anterior, mostrando no final:
#A- A soma de todos os valores pares digitados
#B- A soma dos valores da terceira coluna
#C - O maior valor da segunda linha
num = list()
soma = terC = somas = 0
for c in range(0,9):
    num.append(int(input(f'Digite o número para a posição {c}: ')))
for c, i in enumerate(num):
    if i % 2 == 0:
        soma += i
for c, i in enumerate(num):
    somas = num[2] + num[5] + num[8]
print('►' * 30)
print(f'{num[0]} {num[1]} {num[2]}\n{num[3]} {num[4]} {num[5]}\n{num[6]} {num[7]} {num[8]} ')
print('►' * 30)
print(f'A soma de todos os valores pares é {soma}')
print(f'A soma dos valores na terceira coluna será {somas}')
if num[3] > num[4] and num[3] > num[5]:
    print(f'o número {num[3]} é o maior da segunda linha')
if num[4] > num[3] and num[4] > num[5]:
    print(f'o número {num[4]} é o maior da segunda linha')
if num[5] > num[3] and num[5] > num[4]:
    print(f'o número {num[5]} é o maior')
if num[3] == num[5] == num[4]:
    print('todos valores são iguais')
