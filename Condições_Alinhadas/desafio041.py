#A confereção nacional de natação precisa de um programa que leia o ano de nascimento de
#um alteta e mostre sau categoria, de acordo com a idade:
#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: Junio
#até 20: senior
#acima: master
from datetime import date
idade = int(input('Qual ano de nascimento do atleta: '))
data = date.today().year
s = data - idade
if s <= 9:
    print(f'\033[33mO atleta tem {s} anos, ele é classificado como: \033[32mMIRIM')
elif s <=14:
    print(f'\033[33mO atleta tem {s} anos, ele é clasificado como: \033[32mINFANTIL')
elif s <=19:
    print(f'\033[33mO atleta tem {s} anos, ele é classificado como: \033[32mJUNIOR')
elif s <=20:
    print(f'\033[33mO atleta tem {s} anos, ele é classificado como: \033[32mSENIOR')
else:
    print(f'\33[33mO atleta tem {s} anos, ele é classificado como: \033[32mMASTER')
