#Faça um programa que tenha uma função chamada escreva()
# que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel.
from time import sleep
def escreva(txt):
    s = ''
    if txt != len(s):
        s = '•'
        a = s * len(txt)
        print(a)
        print(txt)
        print(a)

escreva('Olá mundo')
escreva('Carros')
escreva('SP')
escreva('CAVALO')
