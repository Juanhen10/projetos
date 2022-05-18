#faça um program que leia  comprimento do cateto oposto e do cateto adjacente de um traingulo retangulo
#calcule e mostre o comprimento da hipotenusa
import math
"""CO = float(input('Quantos mede Cateto Oposto: '))
CA = float(input('Quanto mede o Cateto Adjacente: '))
ho = (CO ** 2 + CA ** 2) ** (1/2)
print(f' a Hipotenusa vai medir {ho:.2f}')"""

co = float(input('Comprimento do catero oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hiponenusa será {hi:.2f}')
