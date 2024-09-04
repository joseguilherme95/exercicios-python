#Elabora um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento:
# avista DINHEIRO/CHEQUE 10% de desconto
# avista no CARTÃO: 5% de desconto
# em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Valor do produto: '))
forma_pagamento = int(input('''
                            1 - Avista Dinheiro/Cheque = 10% de desconto
                            2 - Avista no Cartão = 5% de desconto 
                            3 - em até 2x no cartão = Preço Normal 
                            4 - 3x ou mais no cartão = 20% Juros.
                            Escolha a forma de pagamento    
'''))
desconto_5 = (valor_produto * 5) / 100
desconto_10 = (valor_produto * 10) / 100
juros_20 = (valor_produto * 20) / 100

if forma_pagamento == 1:
    print('Total a pgar com 10% de desconto {}'.format(valor_produto - desconto_10))
elif forma_pagamento == 2:
    print('Total a pagar com 5% de desconto {}'.format(valor_produto - desconto_5))
elif forma_pagamento == 3:
    print(valor_produto)
elif forma_pagamento == 4:
    print('Total a pagar com 20% de juros {}'.format(valor_produto + juros_20))


































#x = (10 * '-=')
#print(f'{x} LOJA TA BARATO {x}')
#valor_produto = float(input('Qual o valor do produto: '))
#opcao = int(input('''
 #                           ESCOLHA UMA OPÇÃO !!
 #                   1 = AVISTA DINHEIRO/CHEQUE: 10% DESCONTO
 #                   2 =  AVISTA NO CARTÃO: 5% DE DESONTO
 #                   3 = EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
 #                   4 = 3 x OU MAIS NO CARTÃO: 20% DE JUROS
 #                   OPCÃO: '''))

#if opcao == 1:
#    desconto = valor_produto - ((valor_produto * 10) / 100)
#    print(f'A sua compra de R${valor_produto} pagando avista DINHEIRO/CHEQUE será de R${desconto}')
#elif opcao == 2:
#    desconto = valor_produto - ((valor_produto * 5) / 100)
#    print(f'A sua compra de R${valor_produto} pagando avista no CARTÃO será de R${desconto}')
#elif opcao == 3:
#    print(f'A sua compra parcelada no cartão em 2x terá o valor de 2 x {valor_produto / 2}')
#elif opcao == 4:
#    acrescimo = valor_produto + ((valor_produto * 20) / 100)
#   print(f'A sua compra parcelada em 3x ou mais terá o valor de {acrescimo}')
#else:
#    print('Por Favor digite a opção corretamente !!')


