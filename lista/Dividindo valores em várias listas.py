#crie um programa que vai ler varios numeros e colocar em uma lista
#Depois disso, crie duas listas extras que vão con ter apenas os valores pares e os valores impare digitados.
#respectivamente.
#Ao final, mostre o conteudo das tres listas geradas
num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('•'* 30)
print(f'a Listaa completa é {num}')
print(f'a lista com pares é {par}')
print(f'a lista dos impares é {impar}')
print('•'* 30)
