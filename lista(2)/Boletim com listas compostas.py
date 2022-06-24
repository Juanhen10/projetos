  #crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta
#No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada
#aluno individualmente
lista = []
while True:
    alunos = str(input('Digite o nome do aluno: '))
    nota = int(input('Qual a primera nota? '))
    nota2 = int(input('Qual a segunda nota? '))
    resp = str(input('Quer continuar?[S/N]'))
    media = (nota + nota2) / 2
    lista.append([alunos,[nota, nota2],media])
    if resp in 'Nn':
        break
print('▬' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'* 35)
    opc = int(input('Mostrat notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizado...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< Volte sempre>>>>')
