#Crie um programa que tenha uma tupla totalmente preenchida com uma contágem por extenso de zero até vinte
# seu programa deverá ler um número pelo teclado, entre 0 a 20 e mostra-lo por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
           , 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    entrada = int(input('Insira um número entre 0 e 20: '))
    if 0 <= entrada <= 20:
        break
    print('Por favor digite um número entre 0 e 20 !!')



entrada = numeros[entrada]
print('Você digitou o número {}'.format(entrada))
