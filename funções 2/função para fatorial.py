#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor logico(opcional) indicando se será mostrado ou não na tela,
# o processo de cálculo do fatorial
def fatorial(num= 1, show = 0):
    '''

    :param num: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: false
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f , end=' ')
    print()
    return f


f1 = fatorial(5,show=True)
f2 = fatorial(3)
f3 = fatorial(4)
print(f'Os resultados foram  {f1}, {f2} e {f3}')
