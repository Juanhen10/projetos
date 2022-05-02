#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre
#A media de idade do grupo
#qual é o homem mais velho
#quantas mulheres tem menos de 20 anos
totmaior = 0
nomevelho = 0
somaidade = 0
mediaidade = 0
totmulher20 = 0
for a in range(1, 5):
    print(f'--------- {a}º PESSOA -------')
    nome = str(input('Nome: '))
    idade = int(input(f'idade: '))
    sexo = str(input(f'sexo(M ou F): ')).strip()
    somaidade += idade
    if a == 1 and sexo in 'Mm':
        totmaior = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'Essa é a idade média do grupo {mediaidade}')
print(f'Esse é o homem mais velho do grupo {nomevelho} com {totmaior} anos')
print(f'Ao todo são {totmulher20} com menos de 20 anos')
