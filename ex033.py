#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 = float(input('Insira o 1º Número: '))
n2 = float(input('Insira o 2º Número: '))
n3 = float(input('Insira o 3º Número: '))
maior = 0
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print('Maior número é: {:.0f} '.format(maior))
print('Menor número é: {:.0f} '.format(menor))




















#n1 = float(input('Insia o 1º número: '))
#n2 = float(input('Insira o 2º número: '))
#n3 = float(input('Insira o 3º número: '))

#if n1 > n2 and n1 > n3:
#    print('{} é o maior!'.format(n1))
#elif n2 > n1 and n2 > n3:
#    print('{} é o maior !'.format(n2))
#else:
#    print('{} é o maior !!!'.format(n3))

#if n1 < n2 and n1 < n3:
#   print('{} é o menor'.format(n1))
#elif n2 < n1 and n2 < n3:
#    print('{} é o menor'.format(n2))
#else:
#    print('{} é o menor.'.format(n3))