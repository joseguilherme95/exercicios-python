#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('Insira um valor em metros: '))
centimetro = metros * 100
milimetros = metros * 1000

print(f'O valor de {metros} metros em centimetros é: {centimetro:0.0f} e em Milimetros é: {milimetros:0.0f}')