#Escreva um programa que pergunte o salario de um funcionario e calcule o seu valor de aumento
#Para salarios superiores a r$1250,00 calcule um aumento de 10%
# para os inferiores ou iguais o aumento será de 15%
salario = float(input('Insira o salario: '))
aumento_10 = salario * 10 / 100
aumento_15 = salario * 15 / 100

if salario > 1250:
    print(f'O valor do salário com aumento será de: {salario + aumento_10}')
else:
    salario <= 1250
    print(f'O Valor do salário com aumento será de: {salario + aumento_15, aumento_15}')
























#salario = float(input('Insira o valor do seu salário: '))
#aumento_10 = ((salario * 10) / 100) + salario
#aumento_15 = ((salario * 15) / 100) + salario

#if salario > 1250:
#    print(f'Seu aumento será de 10% e o valor novo será de {aumento_10}')
#else:
#    salario <= 1250
#    print(f'Seu aumento será de 15% e o valor novo será de {aumento_15}')
#print('FIM')