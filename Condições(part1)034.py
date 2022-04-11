#escreva um programa que pergunte o slario d um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1,250,00, calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Qual seu Salario? '))
a = salario * 1.10
b = salario * 1.15
if a > 1250:
    print(f'Teu salario teve aumento de 10% ele ficará {a:.2f} ')
else:
    print(f'Teu salario teve aumento de 15% ele ficará {b:.2f} ')
