#faça um programa que leia algo pelo teclado
#e mostre na tela o seu tipo primitivo e todas as informações
#possiveis sobre ele.
dado = input('digite algo: ')
"""print('o tipo primitivo é ', type(dado))
#print('é um numero? ', dado.isnumeric())
#print('tem espaço? ', dado.isspace())
#print('é um alfabeto?', dado.isalpha())
#print('é minuscula?', dado.islower())
####resolução"""
print(f'está em minuscula? {dado.islower()}\n está em numerica? {dado.isnumeric()} ')
