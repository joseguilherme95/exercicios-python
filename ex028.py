#Escreva um programa que faça o ccomputador pensar em um número inteiro entre 0 e 5 e peça para o usuario tentar
#descobrir qual foi o número escolhido pelo computador.
#o programa deverá escrever na tela se o usuario venceu ou perdeu.
import random
from random import randint
from time import sleep

computador = randint(0, 5)
usuario = int(input('Insira um número: '))
print('Analisando....')
sleep(5)
if usuario == computador:
    print('Usuario Venceu !!')
else:
    print('Usuario Perdeu !!')
































#
#print('========== Jogo da Adivinhação !!! ==========')
#pc = randint(0, 5)
#user = int(input('Tente advinhar qual número o computador pensou: '))
#print('Analisando....')
#print(pc)
#sleep(3)
#if user == pc:
#    print('Parabéns você venceu a máquina !!')
#else:
#    print('Você perdeu, Tente novamente')
#print('FIM')
