#   Aprimore o desafio anterior, mostrando no final:
#   A- A SOMA DE TODOS OS VALORES PARES DIGITADOS
#   B - A SOMA DOS VALORES DA TERCEIRA COLUNA
#   C - O MAIOR VALOR DA SEGUNDA LINHA

#   Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
#   no final mostre a matriz na tela, com a formatação correta
#   A - A SOMA DE TODOS OS VALORES PARES DIGITADOS
#   B - A SOMA DOS VALORES DA TERCEIRA COLUNA
#   C - O MAIOR VALOR DA SEGUNDA LINHA

#Matriz com 3 linhas e 3 valores dentro dele
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para [{linha}:{coluna}]: '))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

    print()
print('=-'*30)

print(f'A soma dos valores pares é {spar}')

for l in range(0, 3):
    scol += matriz[l][2]

print(f'A soma dos valores da 3° Coluna é: {scol}')

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')