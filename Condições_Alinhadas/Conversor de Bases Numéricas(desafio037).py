#escreva um programa que leia um numero inteiro qualquer e peça para ususario escolher qual será
#será a base de conversão
# 1 para binario
# 2 - para octal
# 3 - hexadecimal
from time import sleep
num = int(input('Escolha um número: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
a = int(input('Escolha uma forma, \033[31m1 para binaria\033[31m, \033[32m2 para octal\033[m e \033[36m3 hexadecimal\033[m:  '))
if 1 == a:
    print('\033[32mprocessando...\033[m')
    sleep(3)
    print(binario)
elif 2 == a:
    print('\033[32mprocessando...\033[m')
    sleep(3)
    print(octal)
elif 3 == a:
    print('\033[32mprocessando...\033[m')
    sleep(3)
    print(octal)
elif a > 3:
    print('\033[32mProcessando...\033[m')
    sleep(3)
    print('\033[31mDesculpe mas o número tem que ser de 1 á 3\33[m')
