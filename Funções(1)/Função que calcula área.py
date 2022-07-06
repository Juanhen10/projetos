#faça um progrma que tenha uma função chamda aréa(), que receba as dimensoões de um terreno retangular
#(largura e comprimento) e mostre a area do terreno
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
def area():
    s = l * c
    print(f'a area de um terreno {l}X{c} é de {s:.1f}m²')
area()
