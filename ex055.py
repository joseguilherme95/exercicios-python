#   Crie um programa que leia o peso de cinco pessoas, no final mostre qual foi o maior
#   e qual foi o menor peso lidos.

maior_peso = 0
menor_peso = 0


for c in range(1, 6):
    peso = float(input('Insira o peso: '))
    if maior_peso == 0:
        maior_peso = peso
        menor_peso = peso
    if peso > maior_peso:
            maior_peso = peso
    elif peso < menor_peso:
            menor_peso = peso

print(f'Maior peso = {maior_peso}')
print(f'Menor peso = {menor_peso}')