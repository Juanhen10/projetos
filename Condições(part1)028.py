#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
#e peça oara o usuario tentar descobrir qual foi o númeor escolhido pelo computador. 
#o programa deverá escrever na tela se o usuario venceu ou não
import random
pc = random.randint(0,5)
a = int(input('escolha um numero de 1 a 5: '))
print(f'teu numero foi: {a}')
print(f'o numero escolhido foi: {pc}')
if a == pc:
    print(F'e você acertou!!!')
else:
    print(f'tu errou')
