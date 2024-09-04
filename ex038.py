#   Esccreva um programa que leia dois números inteiros, compare-os mostrando na tela uma mensagem
#   O primeiro valor é maior.
#   O segundo valor é maior
#   não existe valor maior, os dois são iguais.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

if n1 > n2:
    print(f'Primeiro valor {n1} é maior que o segundo valor {n2} !')
elif n2 > n1:
    print(f'Segundo valor {n2} é maior que o primeiro valor {n1}')
else:
    print('OS VALORES SÃO IGUAIS !!!')



















#n1 = float(input('Digite um número: '))
#n2 = float(input('Digite outro número: '))
#
#if n1 > n2:
#    print(f'O número {n1:.1f} é maior que o número {n2:.1f}')
#elif n2 > n1:
#    print(f'O número {n2:.1f} é maior que o número {n1:.1f}')
#else:
#    print('Os números são iguais !!!')