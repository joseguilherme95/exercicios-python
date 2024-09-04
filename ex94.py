#   Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
#   e todos os dicionarios em uma lista. No final mostre:
#   A - QUANTAS PESSOAS FORAM CADASTRADAS.
#   B - A MÉDIA DE IDADE DO GRUPO
#   C - Uma lista com todas as mulheres
#   D - Uma lista com pessoas com idade acima da média
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo: [F/M]: ')).strip().upper()
        if pessoa['sexo'] in 'FM':
            break
        print(f'Digite Corretamente o sexo !!!')
    pessoa['idade'] = int(input('Insira a idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        continuar = str(input('Deseja continuar ? [S/N]: ')).upper()
        if continuar in 'SN':
            break
        print('DIGITE UM VALOR CORRETO [S OU N]: ')
    if continuar == 'N':
        break
print(f'=-'*30)
print(galera)

print(f'foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'A média é igual a {soma / len(galera):.2f}')
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')
print()
print(f'Lista de pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print(f'    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('Encerrado')
