#Crie um program que leia varios numeros inteiros pelo teclado. O programa vai parar quando
#o usuario digitar o valor 999, que é a condição de parada. No final mostre quantos números foram
#digitados e qual foi a soma entre eles
n = 0
soma = 0
cont = 0
n = int(input('Me fale outro número[999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Me fale outro número[999 para parar]: '))
print(f'Voc~e digitou {cont} e a soma entre eles foi {soma}')
