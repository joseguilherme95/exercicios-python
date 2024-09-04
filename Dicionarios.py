#DICIONÁRIOS !!
#   tuplas = ()
#   listas = []
#   dicionários = {}
#   dados = dict
# é possível personalizar os itens !!
#VARIÁVEIS COMPOSTAS.

dados = dict()
#Modelo de dicionário:
dados = {'nome':'Jose', 'idade':25}

#Inserir mais um elemento dentro do dicionários:
dados['sexo']='M'

#Remover um elemento do dicionário
del dados['idade']

print(dados)

filme = {
    'titulo':'Star Wars',
    'ano': 1997,
    'autor':'Jorge Lucas'
}
#   Visualizar o que está dentro do dicionário:
print(f'Visualizar os valores de um dicionário.')
print(filme.values())

#   Visualizar os titulos
print(f'Visualizar os titulos ')
print(filme.keys())

#   Visualizar os titulos e os valores dentro do dicionários
print(f'Visualização dos titulos e os valoes dentro do dicionário.')
print(filme.items())

#Utilizando o for no dicionário.
for k, v in filme.items():
    print(f'O k é {k} e o valor é {v}')

#É POSSÍVEL INCLUIR OS DICIONÁRIOS DENTRO DE UMA LISTA.
print('=*'*30)
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])

for c in range(0, 3):
    estado1['uf'] = str(input('Unidade Federativa: '))
    estado1['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado1.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

#Adicionando um dicionário a uma lista !
#time = lista / jogador = dicionário.
#   time.append(jogador.copy())
#Lembrar sempre de limpar o dicionário.