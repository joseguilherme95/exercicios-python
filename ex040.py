#Crie um programa que leia duas notas de aluno e calcule sua média, mostrando uma mensagem no final de acordo com a media
# a - abaixo de 5,00 REPROVADO
# B - MEDIA ENTRE 5.0 E 6.9 = RECUPERAÇÃO
# C - MEDIA 7.0 OU ACIMA = APROVADO


nota1 = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua média é igual a: {media}')
    print('Aprovado  !!!')
elif media >= 5:
    print(f'Sua média é igual a: {media}')
    print('Recuperação !!!')
elif media < 5:
    print(f'Sua média é igual a {media}')
    print('REPROVADO !!!')
else:
    print('INSIRA OS VALORES CORRETAMENTE !!')





































#nota1 = float(input('Insira a primeira nota: '))
#nota2 = float(input('Insira a segunda nota: '))
#media = (nota1 + nota2) / 2

#if media < 5:
#    print('REPROVADO !!!')
#elif media < 6.9:
#    print('RECUPERAÇÃO !!')
#elif media >= 7:
#    print('APROVADO !!!')
#print(media)