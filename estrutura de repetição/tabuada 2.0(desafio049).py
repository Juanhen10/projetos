# Refaça o Desafio 009, mostrando tabuada de um número que o usuario escolher, só que agora
# utilizando um laço for
num = int(input('Escolha um número para a tabuada: '))
for c in range(11):
    a = num * c
    print(a)
