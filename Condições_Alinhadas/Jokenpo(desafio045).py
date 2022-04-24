#crie um programa que faça o computador jogar Jokenpo com você
import random
jokenpo = str(input('Escolha \033[31mPEDRA\033[m, \033[32mTesoura\033[m ou \033[33mPapel\033[m: '))
papel = 1
pedra = 2
tesoura = 3
pc = random.randint(1,3)
if pc == papel:
    print('Escolhi PAPEL!')
elif pc == pedra:
    print('Escolhi PEDRA!')
elif pc == tesoura:
    print('Escolhi TESOURA!')
if jokenpo == 'papel' and pc == pedra:
    print('Você ganhou')
elif pc == papel and jokenpo == 'pedra':
    print('Eu ganhaei')
elif jokenpo == 'tesoura' and pc == papel:
    print('Você ganhou')
elif pc == tesoura and jokenpo == papel:
    print('Eu ganhei')
elif jokenpo == 'pedra' and pc == tesoura:
    print('Você ganhou')
elif pc == pedra and jokenpo == 'tesoura':
    print('Eu ganhei')
elif jokenpo == 'papel' and pc == tesoura:
    print('Você ganhou')
elif pc == papel and jokenpo == 'tesoura':
    print('Eu ganhei')
else:
    print('Deu empate haha')
