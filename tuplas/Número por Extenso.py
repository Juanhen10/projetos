# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# seu programa devera ler um número peçp teclado e mostra-lo por extenso
nome = ('zero','um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
        'quize','dezesseis','dezessete','dezoito','dezenove','vinte')
pc = int(input('Selecione um número entre 0 e 20: '))
while True:
    if pc > 20:
        pc = int(input('tente de novo, um número 0 e 20: '))
    for pos, num in enumerate(nome):
        if pc == pos:
            print(f'\033[35mo número foi \033[31m{pos}\033[m \033[35me ele em extenso ficará \033[32m{num}\033[m')
    break
