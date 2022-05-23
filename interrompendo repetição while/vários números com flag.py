#Crie um progrma que leia varios númeors inteiros pelo teclado. O progrma vai para qquando o usuario
#digitar o valor 99, que é a condição de parada. No final mostre quantos números foram digitados e
#qual foi a soma entre eles.
n = s = c = 0
while True:
    n = int (input('Digite um número: '))
    c += 1
    if n == 999:
        break
    s += n
print(f'A soma dos {c - 1} valores vale {s}')
