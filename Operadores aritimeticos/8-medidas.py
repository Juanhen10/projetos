#escreva um programa que leia um valor  em metros e exiba convertido em centímetros e milimetros
medida = float(input("uma distancia em metros: "))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida /10
hm = medida /100
km = medida /1000
print(f'A medida {medida}m corresponde a \n{cm}cm e {mm}mm')
print(f'a medida corresponde a {dm}dm\n{dam}dam\n{hm}hm\n{km}km')
