#   Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quan o usuario digitar
#   o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e a soma entre eles
#   desconsiderando o flag.
#
#


#print('Código de parada = 999!!!')
#soma = 0
#count = 0
#continuar = 'S'
#while continuar == 'S':
#    n = int(input('Insira um número: '))
#    soma += n
#    count +=1
#    if n == 999:
#        soma = soma - 999
#        count = count -1
#        break#
#
#print(f'soma: {soma}')
#print(f'Quantidade digitada {count}')






print('Entrada de números !!! ')
print('Código de parada 999')
soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'O valor da soma é igual a:  {soma}')
print(f'Foram digitados {cont} números')
