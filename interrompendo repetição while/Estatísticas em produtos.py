from time import sleep
totG = totmaior = totmenor = c = b  = 0
while True:
    print('-'*10)
    print('\033[31mLOJA DO JUANZiN\033[31m')
    print('-'*10)
    produto = str(input('Qual nome do produto? '))
    preço = float(input('Quanto ele custou? R$ '))
    con = str(input('Comprou mais alguma coisa[S/N]: ')).upper().strip()
    b += 1
    if con == 'S':
        totG += preço
        print(totG)
        if preço > 1000:
            c += 1
            print(f'Tivemos {c} produtos maiores que mil!! ')
        if b == 1:
            totmenor = totmaior = preço
        else:
            if preço < totmenor:
                totmenor = preço
                totmenor = produto
                print(totmenor)
    if con == 'N':
        break
print('\033[32mEstou fazendo analise dos seus produtos...um momento.\033[m')
sleep(1)
print('\033[32mAqui está!\033[,')
print(f'\033[31mTotal de compras: \033[36mR${totG}\033[m !')
print(f'\033[33mtivemos \033[32m{c}\033[m produtos acima de R$1000')
print(f'\033[35mEsse produto: \033[31m{totmenor}\033[m foi mais barato!')
