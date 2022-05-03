#conversor de moeda
real = float(input('qunatos dinheiro você tem na carteira?R$ '))
dolar = real / 4.98
euro = real /5.50
libra = real / 6.57
print(f'com R${real :.2f} você pode comprar US${dolar :.2f}')
print(f'com R${real :.2f} você pode comprar EUR${euro :.2f}')
print(f'com R${real :.2f} você pode comprar E${libra :.2f}')
