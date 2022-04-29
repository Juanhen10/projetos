#Desenvolava um programa que leia o priemiro termo e a razão
#de uma PA. No final, mostre os 10 primeirostermos de progressão
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo, razão):
    print(f'{c}', end= " >")
print('Acabou!')
