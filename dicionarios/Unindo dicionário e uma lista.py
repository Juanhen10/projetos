#Crie um programa que leia nome, sexo e idade de varias pessoas,
# guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
# No final, mostre:
# A - Quantas pessoas foram cadastradas.
# B - A media de idade do grupo.
# C - Uma lista com todas as mulheres.
# D - uma lista com todas as pessoas com idade acima da media.
dados = {}
lis = []
cont = 0
media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    cont += 1
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite M ou F')
    dados['idade'] = int(input('Idade: '))
    media += dados['idade']
    lis.append(dados.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper().split()[0]
        if resp in 'SN':
            break
        print('Erro!Responda S ou N.')
    if resp == 'N':
        break
soma = media / len(lis)
print(f'foram cadastradas {cont} pessoas')
print(f'A media das idades {media/cont:5.2f} anos')
print(f'As mulheres cadastradas foram:', end='')
for p in lis:
    if p['sexo'] in 'Ff':
        print(f' [{p["nome"]}] ', end='')
print()
print('Pessoas acima da media: ', end='')
for p in lis:
    if p['idade'] >= soma:
        print("    ", end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('FIM')
