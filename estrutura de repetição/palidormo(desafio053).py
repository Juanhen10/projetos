#crie um programa que leia uma frase qualquer e diga se ela é um palidromo
#desconsiderando os espaços
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inversi = ''
for letra in range(len(junto)-1, -1, -1):
    inversi += junto[letra]
    print(f'O inverso de {junto} é {inversi}')
if inversi == junto:
    print('É um palídormo!')
else:
    print('A frase digitada não é palídromo')
