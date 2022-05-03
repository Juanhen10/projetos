#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
temperatura_em_ºC = float(input('Coloque a temperatura: '))
conversão = (temperatura_em_ºC * 9/5) + 32
print(f'a temperatura está em {temperatura_em_ºC}ºC convertendo em fahrenheit ficara em {conversão}ºf')
