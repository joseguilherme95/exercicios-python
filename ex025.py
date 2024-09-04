#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
nome = str(input('Insira o nome: ')).upper().split()
silva = 'SILVA' in nome

if silva == True:
    print('Tem silva no nome')
else:
    print('Não tem silva no nome')

















#nome = str(input('Insira o seu nome: ')).upper().split()
#resultado = 'SILVA' in nome
#if resultado == True:
#    print('O seu nome tem silva no nome !!!')
#else:
#    print('O seu nome não tem silva no nome ;/')