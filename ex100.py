#   faça um programa que tenha uma lista chamada números e duas funções chamada sorteia e somapar. A primeira função
#   vai sortear 5 numeros e vai colocalos dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores
#   pares sorteados pela funcao anterior

from random import randint
numeros = list()

def sorteia():
    cont = 0
    while cont <= 5:
        valor = randint(1, 10)
        numeros.append(valor)
        cont += 1
    print(numeros)

def somapar():
    soma = 0
    for c, v in enumerate(numeros):
        if v % 2 ==0:
            soma += v

            print(f'{v}', end=' ')
    print()
    print(f'Somando somente os valores pares temos {soma}')

sorteia()
somapar()