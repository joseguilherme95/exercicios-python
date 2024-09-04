#   a CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE
#   SUA CATEGORIA, DE ACORDO COM A IDADE:
#   ATE 9 ANOS - MIRIM
#   ATE 14 ANOS - INFANTIL
#   ATE 19 ANOS - JUNIOR
#   ATE 20 ANOS - SENIOR
#   ACIMA DE 20 - MASTER

import datetime
ano_nascimento = int(input('Qual ano de nascimento? '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('CATEGORIA MIRIM !!')
    print(f'Idade {idade} anos')
elif idade <= 14:
    print('CATEGORIA INFANTIL !!')
    print(f'Idade {idade} anos')
elif idade <= 19:
    print('CATEGORIA JUNIOR !!')
    print(f'Idade {idade} anos')
elif idade <= 20:
    print('CATEGORIA SENIOR !!')
    print(f'Idade {idade} anos')
else:
    print('CATEGORIA MASTER !!')
    print(f'Idade {idade} anos')







































#import  datetime
#x = (20 * '-=')
#print(f'{x} CONFEDERAÇÃO NACIONAL DE NATAÇÃO !! {x}')
#ano_nascimento = int(input('Insira seu ano de nascimento: '))
#ano_atual = datetime.date.today().year
#idade = (ano_atual - ano_nascimento)#####


#if idade <= 9:
#    print('CATEGORIA: MIRIM')
#elif idade <= 14:
#    print('CATEGORIA: INFANTIL')
#elif idade <= 19:
#    print('CATEGORIA: JUNIOR')
#elif idade <= 20:
#    print('CATEGORIA: SENIOR')
#elif idade > 20:
#    print('CATEGORIA: MASTER')