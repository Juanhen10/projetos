#elabore um programa que calculer o valor a ser pago por um produto
#considerando o seu preço normal e condição de pagamento:
#A vista cheue/dinheiro 10% de desconto
#a vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
produto = float(input('Quanto custa o produto? R$ '))
forma = str(input('Qual forma de pagamento? '))
valor = produto
dinheiro = valor * 0.90
cartao = valor * 0.95
cartao2x = valor / 2
cartao3x = valor + (valor * 20 / 100)
if 'dinheiro' == forma:
    print(f'o produto em forma de dinheiro, custará R${dinheiro}')
elif 'cartao' == forma:
    print(f'o produto em forma de cartão custará R${cartao}')
elif 'cartao2x' == forma:
    print(f'o produto em 2x no cartão custará R${cartao2x}')
elif 'cartao3x' == forma:
    totalpatc = int(input('Quantas parcelas? '))
    parcela = valor / totalpatc
    print(f'o produto em 3x no cartão custára R${cartao3x:.2f}')
