#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços.
#na sequencia mostre uma listagem de preços organizando os dados em forma tabular:

lista = ('Lapis', 2.00, 'Borracha', 1.00, 'Caderno', 29.00, 'Estojo', 12.60, 'Caneta', 3.70, 'Monitor', 1200.00, 'Computador', 3000)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')