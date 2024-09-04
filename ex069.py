#   Crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada o programa deverá
#   perguntar se o usuario quer ou não continuar, no final mostre:
#   a- quantas pessoas tem mais de 18 anos.
#   b- quantos homens foram cadastrados
#   c- quantas mulheres tem menos de 20 anos

continuar = 'S'
maior18 = 0
homens = 0
mulhermenos20 = 0

while continuar == 'S':
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo: [M/F]: ')).upper().strip()
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
    continuar = str(input('Deseja continuar ? [S/N]: ')).upper().strip()


print(f'Pessoas maiores de 18: {maior18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulhermenos20}')

