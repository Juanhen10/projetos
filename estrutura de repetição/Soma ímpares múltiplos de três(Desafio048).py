#faça um programa que calcule a soma enre todos os numeros impares que são
#multiplos de três e que se encotram no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}')
