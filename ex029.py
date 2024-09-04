#Escreva um programa que leia a velocidade de um carro
#se ele ultapassar 80KM/H mostre uma mensagem dizendo que ele foi multado
# a multa vai custar 7,0 por cada km acima do limite
velocidade = float(input('Qual a velocidade do carro ?: '))

if velocidade > 80:
    print('Você foi multado !!')
    multa = (velocidade - 80) * 7.0
    print(f'Valor da multa é de {multa:.2f}')
else:
    print('Você não foi multado !!')

























#velocidade = float(input('Insira a velocidade do veiculo: '))
#multa = (velocidade - 80) * 7
#kms = velocidade - 80
#if velocidade > 80:
#    print(f'Você ultrapassou a velocidade em {kms}km e foi multado em: {multa:.2f} reais.')
#else:
#1    print('Siga !!')
#print('FIM')