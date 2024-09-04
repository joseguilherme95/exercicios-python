#   Crie um programa que gerencie o aproveitamento de um jogador de futebol, o programa vai ler o nome do jogador
#   e quantas partidas ele jogou, depois vai ler a quantidade de gols feitos em cada partida.
#   no final tudo isso será guardado em um dicionário, incluindo o total de gols durante o campeonato.

jogador = dict()
partidas = list()

jogador['nome'] = str((input('Insira o nome do jogador: ')))
total = int(input(f'Quantas partidas o jogador {jogador["nome"]} disputou: '))

for x in range(1, total+1):
     partidas.append(int(input(f'Quantos gols o jogador fez na partida {x}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print(f'=-'*30)
print(jogador)
print(f'=-'*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'=-'*30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'        => Na partida {i+1} fez {v} Gols')
print(f'Foi um total de {jogador["total"]} gols')
