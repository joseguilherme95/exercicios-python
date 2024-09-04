#Crie uma tabela preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro
# na ordem de colocação, depois mostre:
# a - Apenas os 5 primeiros colocados
# b - os últimos 4 colocados
# c - Uma lista com os times em ordem alfabetica
# d - Em que posição da tabela esstá o time da chapecoense

tabela = ('Palmeiras', 'Atletico Paranaense', 'Atlético Mineiro', 'Corinthians', 'Internacional',
          'Fluminense', 'Flamengo', 'Santos', 'Sao Paulo', 'Botafogo', 'Avai', 'Bragantino', 'Ceará', 'Atlético Go',
          'Goias', 'Coritiba', 'America MG', 'Cuiaba', 'Juventude', 'Fortaleza')

print('Primeiros Colocados !! ')
for c in range(0, 5):
    print(f'{c + 1}° {tabela[c]}')
print('='*40)

print('Últimos colocados !!')
for x in range(-4, -0):
    print(f'{(20 + x)+1}° {tabela[x]}')
print('='*40)

print('Times em ordem Alfabética !')
print(sorted(tabela))
print('='*40)

print(f'''   
    O São Paulo está na {tabela.index('Sao Paulo')+1}° colocação

''')

