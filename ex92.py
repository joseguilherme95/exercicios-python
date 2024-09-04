#   Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário
#   se por acaso o CTPS for diferente de zero o dicionário receberá também o ano de contratação e o salário
#   calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dicionario = dict()
hoje = date.today().year

dicionario['nome'] = str(input('Insira o nome: '))
dicionario['ano_nascimento'] = int(input('Insira o ano de nascimento: '))
idade = hoje - dicionario['ano_nascimento']
dicionario['idade'] = idade
dicionario['carteira_trabalho'] = int(input('Insira o número da carteira de trabalho: '))

if dicionario['carteira_trabalho'] != 0:
    dicionario['ano_de_contratacao'] = int(input('Digite o ano de contratação: '))
    dicionario['salario'] = float(input('Digite o salário: '))
    dicionario['aposentadoria'] =dicionario['idade']+((dicionario['ano_de_contratacao'] + 35) - date.today().year)

for k, v in dicionario.items():
    print(f'{k} é igual a: {v}')
