#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input('Coloque um ano: '))
if ano % 4 and ano % 100 !=0 or ano % 400 == 0 :
    print(f'Esse ano: {ano}. é Bissexto')
else:
    print(f'Esse ano: {ano}. não é bissexto')
