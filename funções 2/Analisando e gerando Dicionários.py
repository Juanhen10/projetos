#Faça um programa que tenha uma função notas() que pode receber varias notas de alunos
# e vai retornar um dicionario com as seguintes informaçoes
# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situação(opcional)
#Adcione tambem as docstrings da função
def notas(*n , sit=False):
    '''

    :param n: número de notas
    :param sit: sitação(opcional)
    :return: dicionario
    '''
    dici = {}
    dici['total'] = len(n)
    dici['maior'] = max(n)
    dici['menor'] = min(n)
    dici['media'] = sum(n) / len(n)
    if sit:
        if dici['media'] > 5:
            dici['situação'] = 'Boa'
        elif dici['media'] < 5:
            dici['situação'] = 'Ruim'
        else:
            dici['situação'] = 'Recuperação'
    return dici

resp = notas(9,10,5.5,2.5,8.5, sit=True)
print(resp)
