#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errrado peça a digitação novamente até ter um valor correto.


sexo = str(input('Insira o sexo: ')).strip().upper()[0]

while sexo not in 'FfMm':
    print('Digite o valor corretamente !!')
    sexo = str(input('Insira o sexo: ')).strip().upper()

print('SEXO CADASTRADO COM SUCESSO !!')







































#sexo = str(input('Insira o sexo [M/F]: ')).strip().upper()[0]##
#
#while sexo not in 'MmFf':
#    sexo = str(input('Insira o sexo: [M/F]: ')).strip().upper()[0]#
#
#print('Sexo Cadastrado com sucesso !!!')