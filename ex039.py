#   Faça um programa que leia o ano de nascimento de um jovem e informe de acordo ccom sua idade:
#   a- se ele ainda vai se alistar ao serviço militar
#   b - se é hora de se alistar
#   c - se ja passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
#
import datetime
ano_nascimento = int(input('Insira seu ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = (ano_atual - ano_nascimento)


if idade < 18:
    print('Você ainda vai se alistar ao serviço militar !!')
    print(f'Faltam {18 - idade} anos para você se alistar')
elif idade == 18:
    print('Você deve se alistar pois já tem 18 anos !!!')
elif idade > 18:
    print('Você passou da data de alistamento, procure o serviço militar !!')
    print(f'Você passou {idade - 18} anos da data de alistamento')




























#no_nascimento = int(input('Insira o ano de nascimento: '))
#ano_atual = datetime.date.today().year
#idade = (ano_atual - ano_nascimento)







#if idade < 18:
#    print('Você ainda deve se alistar !!')
 #   print('Falta {} anos para o alistamento !!'.format(18 - idade))
#elif idade == 18:
 #   print('Ja é hora de se alistar !!!')
#elif idade > 18:
#    print('Ja se passaram {} anos do alistamento !!'.format(idade - 18))