#   Faça um programa que leia um número qualquer e mostre o seu factorial.
#   ex: 5! 5x4x3x2x1 = 120

n = int(input('Digite um número para calculo do factorial: '))
c = n
f = 1
print(f'Calculando {n}! factorial...')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f'{f}')






































#   from math import factorial

#   n = int(input('Insira um número: '))
#   print(f'O factorial do número {n} é: {factorial(n)}')

#n = int(input('Digite um número para calculo do factorial: '))
#c = n
#f = 1
#print(f'Calculando {n}! factorial...')
#while c > 0:
#    print(f'{c}', end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f = f * c
#    c -= 1
#print(f'{f}')





