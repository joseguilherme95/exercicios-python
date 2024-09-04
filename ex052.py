#   Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

#NÚMERO PRIMO PODE SER DIVIDIDO 2 VEZES

CONT = 0
n = int(input('Insira um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print(f'{c}')
        CONT += 1
if CONT == 2:
    print('É um Número primo ')




































#n = int(input('Digite um número: '))
#tot = 0
#for c in range(1, n + 1):
#    if n % c == 0:
#        print(f'{c} ')
#        tot = tot + 1
#if tot == 2:
#    print('Número primo !!'#)