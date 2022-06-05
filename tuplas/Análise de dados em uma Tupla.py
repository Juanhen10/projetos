#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla, no final mostre
# a - Quantas vezes apareceu o valor 9.
# b - Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))
s = (num1, num2, num3 , num4)
print(f'O valor 9 apareceu {s.count(9)}')
if 3 in s:
    print(f'O número 3 aparece na {s.index(3)+1}º posição')
else:
    print('o valor 3 não foi digitado')
print('Os valores pares digitados foram', end =' ')
for n in s:
    if n % 2 ==0:
        print(f'{n}', end='')
        
