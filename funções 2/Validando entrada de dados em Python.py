#crie um programa que tenha a função() leiaInt(), que vai funcionar de forma semelhante á função input
# No python, só que fazendo a validação para aceitar apenas um valor numerico
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! digite um número valido. \033[m')
        if ok:
            break
    return valor



n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
