#faça um programa qye leia um ãngulo qulquer e mostre na tela o valor do seno, consseno e tangente
import math
angulo  = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f' O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O Ângulo de {angulo} tem a Tangente de {tangente:.2f}')
