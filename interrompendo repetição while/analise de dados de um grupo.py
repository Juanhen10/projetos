#Crie um programa que leia a idade e o sexo de varias pessoas.
# A cada pessoa cadastrada, o progrma deverá perguntar se
# o ususario quer ou não continuar.
# NO final mostre:
#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrado
#Quantas mulheres tem menos de 20 anos
s = i = m = c = 0
while True:
    sexo = str(input('Qual seu sexo? [M/F]: ')).upper().strip()
    idade = int(input('Qual sua idade? '))
    con = str(input('Você quer continuar? [S/N]: ')).upper().strip()
    while con == 'S':
        con = s
        if idade > 18:
                m += 1
        if sexo == 'M':
                s +=1
        if sexo == 'F' and idade < 20:
                i += 1
    if con == 'N':
        print('Fim do programa')
        print(f'Tem {m} pessoas com mais de 18 anos!')
        print(f'Temmos {s} do sexo masculino')
        print(f'temos {i} mulheres com menos de 20 nos')
        break
        
