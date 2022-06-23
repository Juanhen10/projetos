#Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre
# A- quantas pessoas foram cadastradas
# B - Uma listagem com as pessoas mais pesadas
# C - uma listagem com as pessoas mais leves
cont = 0
seg = list()
dados = list()
maior = menor = 0
while True:
    seg.append(str(input('Qual seu nome? ')))
    cont += 1
    seg.append(int(input('Digite seu peso: ')))
    if len(dados) == 0:
        maior = menor = seg[1]
    else:
        if seg[1] > maior:
            maior = seg[1]
        if seg[1] < menor:
            menor = seg[1]
    dados.append(seg[:])
    seg.clear()#limpa os dados
    resp = str(input('Quer continuar? [s/n]: ')).strip().upper().split()[0]
    if resp in 'Nn':
        break
print('▬'* 30)
print(f'os dados foram {dados}')
print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'O maior pesos foi de {maior}KG. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]',end= '')
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
