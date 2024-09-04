#   Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
#   no final mostre:
#   a - qual é o total gasto na compra
#   b - quantos produtos custam mais de 1000
#   c - qual é o nome do produto mais barato

total = maisdemil  = 0
produto_mais_barato = ' '
valor_mais_barato = 0
cont = 0

while True:
    nome_produto = str(input('Insira o nome do produto: ')).strip().upper()
    valor_produto = float(input('Insira o valor do produto: '))
    total += valor_produto
    cont += 1
    if valor_produto > 1000:
        maisdemil += 1
    if cont == 1 or valor_produto < valor_mais_barato:
        valor_mais_barato = valor_produto
        produto_mais_barato = nome_produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total gaasto na compra {total}')
print(f'{maisdemil} Quantidade produtos mais de 1000')
print(f'Nome do produto mais barato {produto_mais_barato}')
