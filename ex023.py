#Faça um programa que leia um número 999 e mostre na tela cada um dos dígitos separados.
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

numero = int(input('Insira um número: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10






#u = numero // 1 % 10
#d = numero // 10 % 10
#c = numero // 100 % 10
#m = numero // 1000 % 10


print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')