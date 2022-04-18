#escreva um progrma que liea dois número inteirotps e cp,áre=os, mostrando na tela uma mensagem
#o primeiro valor é maior; o segundo valor é maior; não existe valor maior, os dois são iguais
num1 = int(input('\033[31mDigite o primeiro valor:\033[m '))
num2 = int(input('\033[32mDigite o segundo valor:\033[m '))
if num1 > num2:
    print(f'\033[31mO primeiro {num1} valor é maior!')
elif num2 > num1:
    print(f'\033[32mO segundo {num2} valor é o maior!')
else:
    print(f'\033[36mNão existe maior, os dois são iguais!')
