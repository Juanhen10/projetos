#Esreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#O programa vai perguntar o VALOR DA CASA, o SALARIO do comprardpr e em QUANTOS ANOS ele vai pagar
#Calcule o valor da prestação mensal. Savendo que ela não pode exceder 30% do Salario
#ou então o emprestimo será negado
casa = float(input('\033[36mQual valor da casa? R$'))
salario = float(input('\033[36mQual Salario? R$'))
anos = int(input('\033[36mQuantos anos irá pagar? '))
Prestação_Mensal =casa / (anos * 12)
a = salario * 30 / 100
print(f' \033[31mO valor da Prestação ficará \033[32mR${Prestação_Mensal:.2f}\033[m')
print(f'\033[31mVerificando se o salario excedeu 30%...\033[32mR${a}\033[m')

if  salario <= Prestação_Mensal:
    print('\033[31mEmprestimo negado\033[m')
else:
    print('\033[32mEmprestimo aprovado\033[m')
