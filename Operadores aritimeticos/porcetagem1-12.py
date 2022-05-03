#faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print(f'o Produto que custava {preço}, na promoção de 5% vai custar {novo}')
