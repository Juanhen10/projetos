#O ususario vai digitar o comando eo manual vai aparecer quando o usuario digitar "FIM",
# O programa se encerrará. OBS: use cores
def escreva(txt):
    s = ''
    if txt != len(s):
        s = '•'
        a = s * len(txt)
        print(a)
        print(txt)
        print(a)

def pyhelp():
    escreva('\033[41m  Sistema de ajuda! ')
    while True:
        a = input('\033[40mQual função você quer?\033[40m ')
        escreva(' Acessando a função ')
        resp = help(a)
        if a.upper() == 'FIM':
            print('\033[41m')
            escreva('\033[41mAté logo!')
            break

pyhelp()
