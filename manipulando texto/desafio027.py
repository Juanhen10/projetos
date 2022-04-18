#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
#o ultimo nome separadamente
n = str(input("Qual seu nome? "))
nome = n.split()
print(f'seu primeiro nome é {nome[0]}')
print(f'seu ulmimo nome é {nome[len(nome)-1]}')
