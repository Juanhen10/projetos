#faça um programa que leia o nome e media de um aluno, guardando também a situação em um dicionario.
# No final mostr o conteudo da estrutura na tela.
sit = {}
sit['nome'] = str(input('nome: '))
sit['nota'] = float(input('media do aluno: '))
print(f'nome é igual {sit["nome"]}')
print(f'a media é igual {sit["nota"]}')
if sit['nota'] < 5:
    print('Você reprovou')
if sit['nota'] > 5:
    print('Você foi aprovado')
    
