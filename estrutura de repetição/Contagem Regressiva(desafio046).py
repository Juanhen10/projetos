#Faça um programa que mostre na tela uma contagem regresiva para o estouros de fogos de artificios
#indo de 10 até 0 com uma pausa de 1 sgundo entre eles
from time import sleep
sleep(1)
print('\033[31mAtenção!\033[m')
sleep(1)
print('Iremos começar a contagem regressiva para os estouro de fogos de artificios!')
for c in range(10, 0, -1):
    sleep(1)
    print(f'{c}')
