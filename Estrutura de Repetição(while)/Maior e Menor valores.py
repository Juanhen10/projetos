#Crie um program que leia varios números inteiros pelo teclado. No final
#mostr a media entre todos os valores e qual foi  o maior e o menor valores lidos. O
#Progrema deve perguntar ao usuarios se ele quer ou não continuar a digitar valores
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continiar [S/N]: ')).upper().strip() [0]
media = soma / quant
print(f'Você digitou {quant} e a media foi {media:.1f}')
print(f'O  maior valor foi {maior} e o menor foi {menor}. ' )
