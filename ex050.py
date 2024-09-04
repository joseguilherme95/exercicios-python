#   Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#   se o valor digitado for impar, desconsidere-o.
n_par = 0
n_impar = 0
contador = 0
numero = 0
for c in range(1, 7):
    numero = int(input('Insira um número: '))
    if numero % 2 == 0:
        n_par += numero
    else:
        n_impar += numero
print(f'A soma dos 6 números, somando apenas os pares é igual a {n_par}')
print(f'A soma dos números impares é {n_impar}')





































#soma_par = 0
#soma_impar = 0
#for c in range(0, 6+1):
#    n = int(input('Digite um número: '))
#    if n % 2 == 0:
#        soma_par += n
#    if n % 2 != 0:
#        soma_impar += n
#print(f'A soma somente dos números pares é de: {soma_par}')
#print(f'Soma dos números impares: {soma_impar}')
#print('fim')