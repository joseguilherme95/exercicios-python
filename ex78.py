# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = []
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

    if c == 0:
        maior = menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
    elif lista[c] < menor:
        menor = lista[c]


print(f'O Maior valor digitado foi:  {maior} e a sua posição foi: ', end='')
for posmaior, i in enumerate(lista):
    if maior == lista[posmaior]:
        print(f'{posmaior+1}..')

print(f'O menor valor digitado foi: {menor} e a sua posição foi: ', end='')
for posmenor, j in enumerate(lista):
    if menor == lista[posmenor]:
        print(f'{posmenor+1}..', end='')