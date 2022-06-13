#Crie um programa onde o usuario possa digitar varios valores númericos e cadastre- os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
# No final, será exibidos todos os valores únicos digitados, em ordem crescente
resp = 'Ss'
num = list()
while resp in 'Ss':
   n = int(input('Digite um valor '))
   if n not in num:
      num.append(n)
      print('Valor adcionado...')
   else:
      print('Valor duplicado! não vou adicionar...')
   resp = str(input('Quer continuar? [S/N]: ')).strip().upper().strip()[0]
print(f'A lista dos números é {num}')
num.sort()
