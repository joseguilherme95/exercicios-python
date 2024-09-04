#   Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
#   Seu programa tem que analisar todos os vaalores e dizer qual deles é o maior.

from time import sleep

def maior(* núm):
    cont = maior = 0
    print(f'Analisando os valores passados !!!')
    for valor in núm:
        print(f'{valor}', end=' ')
        sleep(0.2)
        if cont == 0:
            maior = valor
        if valor > maior:
            maior = valor
        cont += 1
    print()
    print(f'O maior valor passado foi: {maior}')


        
maior(10, 2, 3, 8, 9)