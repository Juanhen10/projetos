#Crie um programa que leia o nome completo de uma pessoa e mostre
#Nome com todas as letras maiusculas
#O nome com todas minusculas
#Quantas letras ao todo(sem considera espaço)
#Quantas letras tem o primeiro nome.
nome = str(input('Nome completo: ')).strip()
u = nome.upper()
l = nome.lower()
n = len(nome) - nome.count(' ')
n1 = nome.find(' ')
print(nome)
print(u)
print(l)
print(n)
print(n1)
