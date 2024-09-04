#   Desenvolva um programa que leia o nome idade e sexo de 4 pessoas no final do programa mostre:
#   a media de idade do grupo
#   Qual é o nome do homem mais velho
#   quantas mulheres tem menos de 20 anos.


total_idade = 0
maior_idade = 0
nome_mais_velho = ''
menor_de_idade = 0
contador = 0
for c in range (1, 5):
    nome = str(input('Insira o nome: ')).strip().upper()
    idade = int(input('Insira a idade: '))
    sexo = str(input('Qual o sexo ? [F/M]: ')).strip().upper()
    total_idade += idade
    contador += 1

    if idade > maior_idade and sexo == 'M':
        maior_idade = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        menor_de_idade += 1

print(f'A média de idade do grupo é {total_idade / contador}')
print(f'Nome do homem mais velho: {nome_mais_velho}')
print(f'{menor_de_idade} mulheres tem menos de 20 anos.')



















#total_idade = 0
#mulheres_20 = 0
#nome_mais_velho = ''
#idade_homem = 0#
#
#for c in range(1, 5):
#    nome = str(input('Insira o nome: '))
#    idade = int(input('Qual sua idade: '))
#    sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()
#    total_idade = total_idade + idade
#    if sexo == 'F' and idade < 18:
#        mulheres_20 += 1
#    if sexo == 'M' and idade > idade_homem:
#        nome_mais_velho = nome
#        idade_homem = idade





#print(f'A media de idade é de {total_idade / 4}')
#print(f'{mulheres_20} mulheres são menores de idade.')
#print(f'Nome do homem mais velho é: {nome_mais_velho}')