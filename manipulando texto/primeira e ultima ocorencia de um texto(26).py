#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'a'
#em que posicão ela aparece a prmeira vez.
#em que posição ela aparece a ultima vez
frase = str(input('Digite uma frase: ')).upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(F'A ultima vez que aparece a letra A é {frase.rfind("A")+1}')
