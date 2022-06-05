#Crie um progrma que vai gerar cinco números aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de números
#gerados e tambem indique o menor e maior valor que estão na tupla
import random
a = random.randint(1,20)
b = random.randint(1,20)
c = random.randint(1,20)
d = random.randint(1,20)
e = random.randint(1,20)
num = (a,b,c,d,e)
print(f'os números sorteados foram: {num}')
if a > b and a > c and a > d and a > e:
    print(f'O maior número foi {a}')
if b > a and b > c and b > d and b > e:
    print(f'o maior número foi o {b}')
if c > a and c > b and c > d and c > e:
    print(f'O maior número foi o {c}')
if d > a and d > b and d > c and d > e:
    print(f'o maior número foi o {d}')
if e > a and e > b and e > c and e > d:
    print(f'o maior número foi o {d}')
else:
    if a < b and a < c and a < d and a < e:
        print(f'o menor número foi o {a}')
    if b < a and b < c and b < d and b < e:
        print(f'o menor número foi o {b}')
    if c < a and c < b and c < d and c < e:
        print(f'o menor número foi o {c}')
    if d < a and d < b and d < c and d < e:
        print(f'o menor número foi o {d}')
    if e < a and e < b and e < c and e < d:
        print(f'o menor número foi o {e}')
