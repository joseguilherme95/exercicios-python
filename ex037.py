#   Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão
#   1 - binário   2 - octal  3 - hexadecimal.


n = int(input('Insira um número: '))
print('Escolha uma opção para conversão: ')
opcao = int(input('''
                    1 - Binário 
                    2 - Octal 
                    3 - Hexadecimal
escolha uma opção para conversão: 
'''))

if opcao == 1:
    print(f'O valor {opcao} convertido para binário será de: {bin(opcao)}')
elif opcao == 2:
    print(f'O valor {opcao} convertido para Octal será de: {oct(opcao)}')
elif opcao == 3:
    print(f'O valor {opcao} convertido para Hexadecimal será de: {hex(opcao)}')
else:
    print('Escolha um valor correto !!!')




















#x = (20 * '=')
#print(f'{x} Base de Conversão !! {x}')
#
#entrada = int(input('Insira um número: '))
#opcao = int(input('''
         #       1 - Binário
       #         2 - Octal
     #           3 - Hexadecimal
                
#Escolha uma Opção para Converão: '''))
#if opcao == 1:
#    print(f'O número {entrada} convertido para binário é: {bin(entrada)} ')
#elif opcao == 2:
#    print(f'O numero {entrada} convertido para octal é: {oct(entrada)}')
#elif opcao == 3:
#    print(f'O número {entrada} convertido para hexadecimal é: {hex(entrada)}')
#else:
#   print('Volte e Escolha uma opção Correta !!!')



