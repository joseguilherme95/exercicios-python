#   Faça um programa que jogue par ou impar com o computador, o jogo só será interrompido quando o jogador
#   perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu !!')
            v += 1
        else:
            print('Voce Perdeuu !!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu !!')
            v += 1
        else:
            print('Você perdeu !!')
            break
    print('Print vamos jogar novamente ...')
print(f'Você Ganhou {v} vezes')
























#print('Jogo do par ou impar !!!')
#from random import randint
#computador = randint(0, 100)
#jogador = int(input('Digite um número: '))
#palpite = str(input('Qual seu palpite: PAR/IMPAR:  ')).upper()
#palpite_maquina = ''
#if palpite == 'PAR':
#    palpite_maquina = 'IMPAR'
#elif palpite == 'IMPAR':
#    palpite_maquina = 'PAR'


