#crie um program que elia duas notas de um aluno e calulcule a sua media, mostrando
#uma mensagem no final, de acordo com a media atingida:
#media abaixo de 5.0: reprovado:
#media esntre 5.0 e 6.9: recuperação
#nedua 7.0 ou superior: aprovado
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
a = nota1 + nota2
res = a / 2
print(f'Sua nota foi {res}')
if res < 5.0:
    print(f'\033[31mREPROVADO!\033[m')
elif res <= 6.9:
    print(f'\033[33mRECUPERAÇÃO\033[m')
elif res >= 7.0:
    print(f'\033[32mAPROVADO\033[m')
