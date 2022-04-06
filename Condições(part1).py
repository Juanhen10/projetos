import random
pc = random.randint(0,5)
a = int(input('escolha um numero de 1 a 5: '))
print(f'teu numero foi: {a}')
print(f'o numero escolhido foi: {pc}')
if a == pc:
    print(F'e você acertou!!!')
else:
    print(f'tu errou')
