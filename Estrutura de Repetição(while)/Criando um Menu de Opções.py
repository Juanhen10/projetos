#crie um program que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
#Seu program devera realizar a opereção solicitada em cada caso.
from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
a = 0
sleep(1)
while a !=5:
    print('''agora escolha uma das opções abaixo:  
    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ]sair do programa      ''')
    a = int(input('Qual opção você escolheu: '))
    if a == 1:
        soma = num1 + num2
        print(f'A soma entre \033[32m{num1}\033[m e \033[32m{num2}\033[m é \033[32m{soma}')
    elif a == 2:
        m = num1 * num2
        print(f'\033[31mA multiplicação entre \033[35m{num1} e \033[35m{num2} é \033[34m{m}')
    elif a == 3:
        if num1 > num2:
            maior = num1
            print(f'o \033[38m{num1}\033[m entre \033[37m{num1}\033[m e \033[37m{num2}\033[m é o maior')
        elif num2 > num1:
            maior = num2
            print(f'o {num2} entre {num1} e {num2} é o maior')
        else:
            print('Os dois são iguais')
    elif a == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor'))
    elif a == 5:
        print('Finalizando')
    else:
        print("Opção invalida. Tente novamente")
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
