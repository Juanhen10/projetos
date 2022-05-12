#Faça um progrma que leia um número qualquer e mostre o seu fatorial
n = int(input('Digite um número paracalclar seu Fatorial: '))
cont = n
fato = 1
print(f'Calculando {n}! = ', end="")
while cont > 0:
    print(f'{cont} ', end='')
    print(' x ' if cont > 1 else ' = ', end='' )
    fato *= cont
    cont -= 1
print(f'{fato}')
