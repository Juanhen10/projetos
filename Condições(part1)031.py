#desenvolva um programa que pergunte a distancia de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
#e R$0,45 para viagens mais longas
km = float(input('Qual distancia percorrida: '))
passagem = km * 0.50
passagem2 = km * 0.45
if km <= 200:
    print(f'Tua viagem custará {passagem}, por não ter utrapassado 200km')
else:
    print(f'Sua passagem custará {passagem2} por utrapassar 200km')
