#Desenvolva uma logica que leia o peso e altura de uma pessoa
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18,5: Abaixo do peso
#entre 18,5 e 25: peso ideal
#25 até 30:Sobrepeso
#30 até 40:Obesidade
#Acima de 40: Obesidade morbita
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
res = peso / altura**2
print(f'{res:.2f}')
if res < 18.5:
    print('\033[32mEstá Abaixo do Peso')
elif res <=25:
    print(f'\033[33mPeso ideal')
elif res <=30:
    print(f'\033[34mSobrepeso')
elif res <=40:
    print(f'\033[35mObesidade')
elif res >=40:
    print(f'\033[31mObediade móbida')
