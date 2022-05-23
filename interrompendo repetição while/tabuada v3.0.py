#faça um progrma que mostre a tabuada de varios números, um de cada vez, para cada valor
# digitado pelo usuario. O programa será interrompido quando
# o número solicitado for NEGATIVO
f = 0
while True:
    num = int(input('Qual número da tabuada você quer saber? '))
    if num < 0:
        print('Fim da tabuada!')
        break
    for c in range(1, 11):
        f += 1
        print(f'tabuada do {num} é  {num} X {num * c}')
        
