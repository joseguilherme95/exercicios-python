#   Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de 3
#   e que se encontram no intervalo entre 1 até 500

soma = 0
contador = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f'A soma dos valores é {soma}')
print(f'Foram somados {contador} números')



























#soma_impar = 0

#cont = 0
#for c in range(1, 501, 2):
 #   if c % 3 == 0:
 #       cont += 1
 #       soma_impar += c
#print(f'Soma dos multiplos = {soma_impar}')
#print(f'Valores solicitados {cont}')
