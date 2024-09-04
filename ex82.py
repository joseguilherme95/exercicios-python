#   Crie um programa que vai ler varios numeros e colocar em uma lista.
#   Depois disso crie duas listas extras que vão conter apenas os valores pares, e o valorees impares digitados, respectivamente
#   no final mostre o conteudo das 3 listas geradas.

lista = []
lista_par = []
lista_impar = []


while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 != 0:
        lista_impar.append(n)
    r = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break
lista.sort()
print(f'Lista Completa {lista}')
print(f'Lista par {lista_par}')
print(f'Lista Impar {lista_impar}')


