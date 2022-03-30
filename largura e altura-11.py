#faça um programa que leia a largura e a altura de uma parede
larg = float(input('Largura da parede? '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'sua parede tem {larg} X {alt} e sua area é de {area}m².')
tinta = area / 2
print(f'para pintar essa parede,você precisará de {tinta}L de tinta')
