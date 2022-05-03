#escreva um program que pergunte a quantidade de KM
#percorridos por um carro alugado e a quantidade de dias pelo
#quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 km rodado
dias = int(input('quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'o total a pagar é de R${pago:.2f}')
