#escreve um programa queleia a velocidade de um carro.
#se ele utrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#a multa vai custar RS$7,00 por cada Km acima do limite
carro = float(input('Quantos KM o carro percorreu? '))
a = 80
s = (carro * 0.7)
if carro <= a:
    print('Não sera multado.')
else:
    print('VOCÊ FOI MULTADO!!!!')
    print(f'Sua multa será de R${s:.2f}')
