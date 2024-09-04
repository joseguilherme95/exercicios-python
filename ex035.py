#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ele pode ou não formar um triângulo.

r1 = int(input('Insira o valor da primeira reta: '))
r2 = int(input('Insira o valor da segunda reta: '))
r3 = int(input('Insira o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('É POSSÍVEL CRIAR UM TRIANGULO')
else:
    print('NÃO É POSSÍVEL')