#   Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi a maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou não
# continuar a digitar valores.

soma = 0
maior = 0
menor = 0
cont = 0

continuar = 'S'

while continuar == 'S':
    n = int(input('Insira os valores: '))
    cont += 1
    soma += n
    if cont == 1:
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    continuar = str(input('Deseja Continuar ? [S/N]:')).upper().strip()

print(f'A média é igual a {soma / cont}')
print(f'O valor da soma é igual a {soma}')
print(f'O maior número inserido é: {maior}')
print(f'O menor número inserido é: {menor}')

































#continuar = 'S'
#
#soma = count = maior = menor = 0#
#
#
#while continuar == 'S':
#    numero = int(input('Insira um número: '))
#    count += 1
#    soma += numero#
#
#
 #   if count == 1:
  #      maior = numero
  #      menor = numero
  #  else:
   #     if numero > maior:
    #        maior = numero
    #    elif numero < menor:
     #       menor = numero
    #continuar = str(input('Deseja continuar ? [S/N]: ')).strip().split()[0].upper()

#print(f'Foram digitados {count} números e a média deles é de {soma / count}')
#print(f'O maior valor digitado foi {maior}')
#print(f'O menor valor digitado foi {menor}')