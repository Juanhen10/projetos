#Crie um programa que crie um matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta
num = list()
for c in range(1,10):
    num.append(int(input(f'Digite o número para a posição {c}º: ')))
print('►' * 30)
print(f'[{num[0]}] [{num[1]}] [{num[2]}]\n[{num[3]}] [{num[4]}] [{num[5]}]\n[{num[6]}] [{num[7]}] [{num[8]}] ')
print('►' * 30)
