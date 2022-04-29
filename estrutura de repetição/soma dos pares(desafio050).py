#Desenvolva um programa que leia seis numeros inteiros e mostre a soma
#apenas daqueles que forem pares. Se o valor for impar desconsidere-0
from random import randint
soma = 0
for c in range(1,7):
    a = randint(1,50)
    print(a, end= " ")
    if a % 2 == 0:
        soma +=a
        print('Esse numero é par')
print(f'E a soma deles são {soma}')
