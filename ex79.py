# Crie um programa onde o usuario possa digitar varios valores númericos e cadastre-os em uma lista.
# Caso o número ja exista la dentro, ele não será adicionado.
# no final, serão exibidos todos os valores únicos digitados em ordem crescente.

numeros = list()

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Valor adicionado com sucesso a lista !!')

    else:
        print('Número não pode ser adicionado !!')

    r = str(input('Deseja continuar: [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break


print(numeros)


