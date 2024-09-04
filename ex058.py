#   Melhoro o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
#   só que agora o jogador vai advinhar até acertar mostrando no final quantos palpites
#   foram necessários para vencer.

#Escreva um programa que faça o ccomputador pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar
#descobrir qual foi o número escolhido pelo computador.
#o programa deverá escrever na tela se o usuario venceu ou perdeu.

import random

computador = random.randint(0, 10)
jogador = int(input('Insira um número: '))
contador = 0

while jogador != computador:
    jogador = int(input('Insira um número: '))
    contador += 1
print(f'Foram precisos {contador} palpites para acertar !!')


























#import random
#computador = random.randint(0, 10)
#contador = 0
#acertou = False

#while not acertou:
#    jogador = int(input('Qual seu Palpite ?'))
#    contador += 1##
#
#    if jogador == computador:
#        acertou = True
#    else:
#        if jogador > computador:
#            print('Menos, tente mais uma vez...')
#        elif jogador < computador:
#            print('Mais, tente mais uma vez ....')#
#
#print(f'Acertou com {contador} tentativas. Parabéns !!')

