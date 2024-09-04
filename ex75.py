#Desenvolva um programa que leia quatro valores pelo teclado e guarde os em uma tupla, no final mostre:
# a - quantas vezes apareceu o valor 9
# b - em que posição foi digitado o primeiro valor 3
# c - quais foram os números pares.


numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

print('Você digitou os números {}'.format(numeros))

#Execução
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 aparece  {numeros.index(3)+1} posição')
else:
    print('O numero 3 não foi digitado')

print('Números pares: ', end='')
for x in numeros:
    if x % 2 == 0:
        print(x, end=' ')