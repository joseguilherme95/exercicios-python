#   Crie um programa onde o usuario possa digitar sete valores númericos e cadastre-os em uma lista única
#   que mantenha separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.
#   obs: apenas 1 lista com duas listas internas.
## Minha Solução !!!
#num = []
#lista_par = []
#lista_impar = []
#for x in range(0,6):
#    num.append(int(input('Insira um número: ')))
#    if num[x] % 2 == 0:
#        lista_par.append(num[x])
#    elif num[x] % 2 != 0:
#        lista_impar.append(num[x])
#num.sort()
#lista_impar.sort()
#lista_par.sort()
#print(f'Lista Completa: {num}')
#print(f'Lista par: {lista_par}')
#print(f'Lista impar: {lista_impar}')

num = [[], []]

for x in range(0, 7):
    valor = int(input('Insira um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 != 0:
        num[1].append(valor)
num.sort()
num[0].sort()
num[1].sort()

print(f'Lista completa: {num}')
print(f'Lista par: {num[0]}')
print(f'Lista impar: {num[1]}')
