#   Crie um programa que simule o funcionamento de um caixa eletronico
#   no inicio pergunte ao usuario qual será o valor do saque(num inteiro) e o programa vai informar quantas cedulas
#   de cada valor serão entregues
#   considere que o caixa possui cedulas de r$ 50, r$ 20, R$ 10 e r$ 1.

print('-' * 30)
print('{:^30}'.format('Banco do Gui'))
print('-' * 30)

valor = int(input('Qual valor você quer sacar ? R$: '))
total = valor
ced = 50
totalcéd = 0
while True:
    if total >= ced:
        total -= ced
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} celulas de r${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalcéd = 0
        if total == 0:
            break

























#print('Cédulas de: 50R$, 20R$, 10R$ e 1R$')
#valor_50 = 0
#valor_20 = 0
#valor_10 = 0
#valor_1 = 0
#saque = float(input('Qual será o valor do saque: '))
#
#while (saque // 50) != 0:
#    saque = saque / 50
 #   valor_50 = valor_50 + 1
#print(valor_50)


