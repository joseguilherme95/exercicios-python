#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
# abaixo de 18.5 - abaixo do peso
# entre 18.5 e 25 - peso ideal
# 25 até 30 - sobrepeso
# 30 até 40 - obesidade
# acima de 40 - obesidade mórbida

peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('ABAIXO DO PESO, imc = {:.2f}'.format(imc))
elif imc >= 18.5:
    print('PESO IDEAL, imc = {:.2f}'.format(imc))
elif imc >= 25:
    print('SOBRE PESO, imc = {:.2f}'.format(imc))
elif imc >= 30:
    print('OBESIDADE, imc = {:.2f}'.format(imc))
elif imc > 40:
    print('OBESIDADE MÓRBIDA, imc = {:.2f}'.format(imc))




























#print('=-=-=-=-=- CALCULADORA IMC =-=-=-=-=-=-=-')
#altura = float(input('Digite sua altura: '))
#peso = float(input('Digite o seu peso: '))
#imc = peso / (altura * altura)
#print(imc)
#

#if imc < 18.5:
#    print('ABAIXO DO PESO')
#elif imc <= 25:
#    print('PESO IDEAL !!')
#elif imc <= 30:
#    print('SOBREPESO!')
#elif imc <= 40:
#   print('OBESIDADE !!')
#elif imc > 40:
#    print('OBESIDADE MÓRBIDA')