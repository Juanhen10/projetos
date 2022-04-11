#desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem
#ou não formar um triâgulo.
r1 = float(input('Coloque a primeira reta: '))
r2 = float(input('Coloque a segunda reta: '))
r3 = float(input('Coloque a terceira reta: '))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
