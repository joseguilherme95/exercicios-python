#   Crie um programa que leia vários números inteiros pelo teclado. programa so vai parar quando o usuario digitar
#   o valor 999 que é a condição de parada.no final mostre quantos números foram digitados. e qual foi a soma entre eles.
#   desconsiderando o 999

n = int(input('Insira o número: '))
count = 0
soma = 0

if n == 999:
    print('FIM')
while n != 999:
    count += 1
    soma += n
    n = int(input('Insira o número: '))

print(f'A soma dos números é {soma}')
print(f'Foram digitados {count} números ')