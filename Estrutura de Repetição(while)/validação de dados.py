#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
#'M" e 'F'. CCawso esteja errado, pela a digitação novamente até ter um valor correto

sexo = str(input('Qual seu sexo[M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('\033[31m-------COMANDO ERRADO INSIRA [M/F]----------\033[31m')
    sexo = str(input('\033[31mDigite novamente[M/F]: \033[m')).upper()
else:
    print('\033[32mComando Valido, Obrigado.\033[m')
