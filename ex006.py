#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Insira um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print(f'Dobro = {dobro}, Triplo = {triplo}, Raiz = {raiz:0.1f}.')