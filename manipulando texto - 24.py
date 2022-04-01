#crie um programa que leia o nome de uma cidade e diga se ela começa com nome 'santo'
cidade = str(input('Qual nome da cidade? ')).strip()
print(cidade[:5].upper() == 'SANTO')
