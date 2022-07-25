#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
#de um número de tipo valido. Aproveite e crei também uma função leiaFloat() com a mesma funcionalidade
from sistema import leiaInt, leiaFloat

i = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite o Real: ')
print(f'O valor inteiro é {i} e o valor Real é {r}')
