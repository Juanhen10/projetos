#crie um programa que simule o funcionamento de um caixa eletronico
#No inicio, pergunte ao usuario qual será o valor sacado(numero inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues.
saque = int(input('Qual valor você quer sacar? R$'))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
            
