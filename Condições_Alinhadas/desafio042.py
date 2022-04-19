#Reforça o desafio 035 do triangulos acrescmtando o recirso de mostrar que tipo de triagulo
#será formado
#EQUILATERO: todos os lados iguais
#ISOSCELES: dois lados iguais
#ESCALENO: todos os lados diferentes
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs segmentos acima PODEM FORMAR triângulo!!')
else:
    print('\033[31mOs segmentos acima NÃO PODEM formar um triângulo')
if r1 == r2 == r3 :
    print('São \033[32mESQUILÁTERO\033[m Todos os lados iguais')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('São \033[32mIsosceles\033[m dois lados iguais')
else:
    print('São \033[32mESCALENO\033[m Todos os lados diferentes')
