#   Faça um exércicio que leia o nome a média de um aluno, guardando também a situação em um dicionário. no final mostre
#   o conteudo da estrutura na tela.

dados = {'nome': '', 'media':'', 'situacao': ''}

dados['nome'] = str(input('Insira o nome: '))
dados['media'] = float(input('Insira a média: '))
situacao = ''

if dados['media'] >= 7:
    situacao = 'Aprovado'
elif dados['media'] == 5:
    situacao = 'Reforço'
else:
    situacao = 'Reprovado'
dados['situacao'] = situacao

for k, v in dados.items():
    print(f'{k} é igual a: {v}')
