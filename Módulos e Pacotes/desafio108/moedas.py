def aumetar(num = 0):
    return num * 1.10

def diminuir(num = 0):
    return num * 0.10


def dobro(num= 0):
    return num * 2

def metade(num = 0):
    return num * 0.50

def moeda(num = 0, moeda = "R$"):
    return f"{moeda}{num:.2f}".replace('.',',')