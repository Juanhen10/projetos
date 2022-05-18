#Professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('terceiro Aluno: '))
n4 = str(input('Quarto aluno:  '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'o aluno escolhido foi {escolhido}')
