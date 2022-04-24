#elabore um programa que calculer o valor a ser pago por um produto
#considerando o seu preço normal e condição de pagamento:
produto = float(input('Quanto custa o produto? '))
forma = str(input('Qual forma de pagamento? '))
valor = produto
dinheiro = valor * 0.90
cartao = valor * 0.95
cartao2x = valor / 2
cartao3x = (valor / 3) + (valor * 1.20)
'''print(dinheiro)
print(cartao)
print(cartao2x)
print(cartao3x)'''
if 'dinheiro' == forma:
    print(f'o produto em forama de dinheiro, custará R${dinheiro}')
elif 'cartao' == forma:
    print(f'o produto em forma de cartão custará R${cartao}')
elif 'cartao2x' == forma:
    print(f'o produto em 2x no cartão custará R${cartao2x}')
elif 'cartao3x' == forma:
    print(f'o produto em 3x no cartão custára R${cartao3x:.2f}')
