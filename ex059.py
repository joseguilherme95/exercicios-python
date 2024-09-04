#   Crie um programa que leia dois valores e mostre um menu na tela:
#   [1] - SOMAR
#   [2] - MULTIPLICAR
#   [3] - MAIOR
#   [4] - NOVOS NÚMEROS
#   [5] - SAIR DO PROGRAMA.
# seu programa deverá realizar a operação solicitada em cada caso.



v1 = float(input('Insira o primeiro valor: '))
v2 = float(input('Insira o segundo valor: '))
operacao = 0

while operacao != 5:
    print(''' 
                #   [1] - SOMAR
                #   [2] - MULTIPLICAR
                #   [3] - MAIOR
                #   [4] - NOVOS NÚMEROS
                #   [5] - SAIR DO PROGRAMA

 ''')
    operacao = int(input('Escolha a operação: '))
    if operacao == 1:
        print('Operação somar !!')
        print(f'A soma dos valores {v1} + {v2} é igual a: {v1+v2}')
    elif operacao == 2:
        print('Operacao Multiplicar !!')
        print(f'A multiplicação dos números {v1} e {v2} é igual a {v1*v2}')
    elif operacao == 3:
        if v1 > v2:
            maior = v1
        elif v2 > v1:
            maior = v2
        else:
            maior = str('VALORES IGUAIS')
        print('Operação MAIOR !!')
        print(f'Maior número é: {maior}')
    elif operacao == 4:
        print('Operação Novos Números !!')
        v1 = float(input('Insira o primeiro valor: '))
        v2 = float(input('Insira o segundo valor: '))

    elif operacao == 5:
        print('Finalizando o programa....')

    else:
        print('Escolha uma opcao correta !!')




























































#v1 = float(input('Insira um valor: '))
#v2 = float(input('Insira outro valor: '))
#opcao = 0
#while opcao != 5:
#    print('''
#    # ESCOLHA UMA OPERAÇÃO !!
#    #   [1] - SOMAR
#    #   [2] - MULTIPLICAR
#    #   [3] - MAIOR
#    #   [4] - NOVOS NÚMEROS
#    #   [5] - SAIR DO PROGRAMA.
 #         ''')
  #  opcao = int(input('QUal é sua opção:  '))
#
 #   if opcao == 1:
  #      print('Operação Somar')
   #     print(f'A soma dos valores {v1} e {v2} é: {v1 + v2}')
    #elif opcao == 2:
    #    print('Operação Multiplicar ')
    #    print(f'A Multiplicação dos números {v1} e {v2} é: {v1 * v2}')
    #    exit()
    #elif opcao == 3:
    #    print('Operação maior !!')
    #    if v1 > v2:
    #        print(f'O Maior valor é {v1}')
    #    else:
    #        print(f'O maior valor é {v2}')
    #    exit()
    #elif opcao == 4:
    #    print('Operação Novos números')
    #    v1 = float(input('Insira um valor: '))
    #    v2 = float(input('Insira outro valor: '))


   # elif opcao == 5:
     #   print('Finalizando... ')

    #else:
    #    print('Escolha uma opção correta !')
#print('Fim')
