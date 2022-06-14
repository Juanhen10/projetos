#Crie um programa que vai ler varios números e colocar em uma lista.
#depois disso, mostre:
# A- Quantos números foram digitados.
# B- A lista de valores ordenanda de forma decrescente
# C- Se o valor 5 foi digitado e está ou não na lista
cont = 0
num = a = list()
resp = 's'
while resp in 'Ss':
    num =(int(input('Digite os números: ')))
    cont += 1
    resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    a.append(num)
print('♦'* 30)
print(f'Voce digitou {cont} numeros')
print(f'Os número em ordem decrescente fica {sorted(a, reverse= True)}')
if num == 5:
    print('O número 5 foi adicionado na lista')
else:
    print('Número 5 não foi adicionado')
    print('♦' * 30)
    
