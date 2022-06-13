#Faça um programa qye leia 5 valores númericos e guarde em uma lista
#No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lis = []
maior = men = 0
for c in range(0,5):
       lis.append(int(input(f'Digite um valor para a posição {c}: ')))
       if c == 0:
              maior = men = lis[c]
       else:
              if lis[c] > maior:
                     maior = lis[c]
              if lis[c] < men:
                     men = lis[c]
print(f'Você digitou ps valores {lis} ')
print(f'o maior valor foi {maior} nas posições', end='')
for i, v in enumerate(lis):
       if lis[i] ==maior:
              print(f' {i}...',end='')
print()
print(f'o menor valor foi {men} nas posições ', end='')
for i, v in enumerate(lis):
       if v == men:
              print(f'{i}...', end='')
print()
