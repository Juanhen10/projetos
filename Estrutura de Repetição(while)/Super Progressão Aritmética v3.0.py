#Melhore  o desafio061, perguntando para o usuario se ele quer mostrar mais alguns termos
#O programa encerra quando ele disser que quer mostrar 0 termo
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM!')
print(f'Fim da Progressão com {total}.')
