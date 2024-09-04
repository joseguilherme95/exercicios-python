#   Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista
#   A - Quantas pessoas cadastradas
#   b - Uma listagem com as pessoas mais pesadas.
#   c - Uma listagem com as pessoas mais leves.

#   ao todo voce cadastrou x pesoas
#   o maior peso foi de 100kg peso de joao e hélio
#   o menor peso foi de 70 kg de maria e ana

pessoas = list()
listatemporaria = list()
menor = maior = 0

while True:
    listatemporaria.append(str(input('Insira o nome: ')))
    listatemporaria.append(int(input('Insira o peso: ')))

    if len(pessoas) == 0:
        maior = menor = listatemporaria[1]

    if listatemporaria[1] > maior:
        maior = listatemporaria[1]
    elif listatemporaria[1] < menor:
        menor = listatemporaria[1]

    pessoas.append(listatemporaria[:])
    listatemporaria.clear()

    continuar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()
    if continuar in 'nN':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso cadastrado foi de {maior}kg e as pessoas foram: ', end='' )
for x in pessoas:
    if x[1] == maior:
        print(f'{x[0]},')



print(f'O menor peso cadastrado foi {menor}kg e as pessoas foram: ',end='')
for y in pessoas:
    if y[1] == menor:
        print(f'{y[0]},')
