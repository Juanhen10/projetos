#crie um programa que leia um númeor inteiro e mostre na tela se ele é PAR ou ímpar
num = int(input('Coloque um número: '))
resto = num % 2
print(f'o númeor foi {num}')
if resto == 0:
    print('Número é par')
else:
    print('Esse numero é impar')
