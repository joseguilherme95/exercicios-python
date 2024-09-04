#   Aprimore o desafio 93 para que ele funcione com varias jogadores, incluindo um sistema de visualização
#   de detalhes do aproveitamento de cada jogador.


time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str((input('Insira o nome do jogador: ')))
    total = int(input(f'Quantas partidas o jogador {jogador["nome"]} disputou: '))
    partidas.clear()
    for x in range(1, total+1):
         partidas.append(int(input(f'Quantos gols o jogador fez na partida {x}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Deseja Continuar [S/N]: ')).strip().upper()
        if resp in 'NS':
            break
        print(f'Erro, digite corretamente.')
    if resp == 'N':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'-'*30)

while True:
    busca = int(input('Mostrar dados de qual jogador: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, o item buscado não existe !!')
    else:
        print(f'-- Leventamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} Gols ')
    print(f'-'*30)
print(f'Volte Sempre !!')


