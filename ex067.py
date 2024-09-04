#   Faça um programa que mostre a tabuada de vários números. um de cada vez, para cada valor digitador.
#   O programa será interrompido quando o valor solicitador for negativo.


print('Valores negativos enceram a tabuada !!')
while True:
    print('-' * 40)
    n = int(input('Digite um número para a tabuada: '))
    if n < 0:
        break
    for x in range(1, 11):
        print(f'{x:2} x {n:2} = {(x * n):2}')
print('PROGRAMA FINALIZADO !!')















#print('Tabuada !!')
#numero = int(input('Tabuada de qual número deseja ?: '))
#
#while numero >0:
#    for c in range(1,11):
#        print(f'{numero} x {c:2} = {numero * c}')
#
#   numero = int(input('Digite outro número: '))
#    if numero <= 0:
#        break











































#print('Taboada de números !!!')
#valor = int(input('Digite um valor: '))
#
#while valor >= 1:
#    for x in range(1, 11):
#        print(f'{x} x {valor} = {x * valor}')
#    valor = int(input('Digite um valor: '))
#    if valor <= 0:
#        break
