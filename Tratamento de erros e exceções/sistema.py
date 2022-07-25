def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        try:
            a = str(input(msg)).strip()
            if a.isnumeric() or a.strip() == '':
                valor = int(a)
                ok = True
            else:
                print(f'\033[31mERRO! Digite um valor valido\033[m')
        except KeyboardInterrupt:
            print(f'O usuario optou por não digitar!')
            break
        except (ValueError, TypeError):
            print(f'\033[31mTivemos um problema com o tipo de dado que você digitou\033[m')
        if ok:
            break
    return valor

def leiaFloat(msg):
    valido = False
    valor = 0
    while not valido:
        try:
            entrada = str(input(msg)).replace(',', '.').strip()
            if entrada.isalpha() or entrada.strip() == '':
                print(f'\033[31mERRO: \"{entrada}\" é invalido\033[m ')
                valido = True
                valor = float(entrada)
        except KeyboardInterrupt:
            print(f'O usuario optou por não digitar!')
            break
        except (ValueError, ZeroDivisionError):
            print(f'\033[31mTivemos um problema com o tipo de dados que você digitou\033[m')
        if valido:
            break
    return valor

c = ('\033[m', #sem cor
     '\033[0;30;41m', # 1 - fonte: preta; fundo: vermelho
     '\033[0;30;42m', # 2 - fonte: preta; fundo; verde
     '\033[0;30;43m', # 3 - fonte: preta; fundo; amarela
     '\033[0;30;44m', # 4 - fonte: preta; fundo; azul
     '\033[0;30;45m', # 5 - fonte: preta; fundo roxo
     '\033[7;30m',    # 6 - branco
     '\033[40;32m',   # 7 - preto com verde
     '\033[40;35m')   # 8 - preto com roxo

def linha():
    print('•' * 40)

def escreva(txt, cor = 0):
    tam = len(txt) * 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')

def escreva2(txt, cor = 0):
    print(c[cor],end='')
    print(f' {txt}')
    print(c[0], end='')

def fim(cor = 0):
    print(c[cor], end='')
    print(f'$' * 30)
    print(f'VOLTE SEMPRE!!'.center(30))
    print(f'$' * 30)
    print(c[0], end='')
