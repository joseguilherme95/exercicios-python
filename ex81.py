#   Crie um programa que vai ler vários numeros e colocar em uma lista, depois disso mostre:
#   Quantos números foram digitados.
#   A lista de valores ordenada de forma decrescente
#   se o valor 5 foi adicionado e se está ou nao na lista
lista = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
if 5 in lista:
    cinco = 'SIM'
else:
    cinco = 'NÃO'


print(f'Foram Digitados {len(lista)} números na lista !!')
lista.sort(reverse=True)
print(f'A lista de forma decrescente {lista}')
print(f' O valor 5 está na lista ? {cinco}')
