#Crie um programa onde o usuario possa digitar cincovalores númericos e cadastre em uma lista.
# ja na posição correta
# no final mostre a lista ordenada na tela

numeros = list()

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {numeros}')