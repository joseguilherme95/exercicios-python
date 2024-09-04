#   Crie um programa onde 4 jogadores jogue um dado e tenham resultados aleatórios.
#   Guarde esses resultados em um dicionário no final coloque esse dicionario em ordem.
#   Sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
lista = list()
ranking = list()
jogo = {
    'jogador1': randint(1, 8),
    'jogador2': randint(1, 8),
    'jogador3': randint(1, 8),
    'jogador4': randint(1, 8)
}
print(f'Valores sorteados !!')
for k, v in jogo.items():
    print(f'O {k} sorteou o numero {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')
    sleep(1)



