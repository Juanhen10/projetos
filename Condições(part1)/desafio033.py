# Faça um program que leia três numeros e mostre qual é o maior e qual é o menor
num1 = int(input('Coloque primeiro número: '))
num2 = int(input('Coloque o segundo número: '))
num3 = int(input('Coloque o terceiro numero: '))
print(f'os números escolhidos foram {num1, num2, num3}')
menor = num1
#Verificando que é o menor
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3

#verificando que é maior
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
