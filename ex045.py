#Crie um programa que faça o computador jogar jokenpô com você.
import random
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_pc = random.choice(lista)
jogador = str(input('Pedra, Papel ou Tesoura, Escolha: ')).strip().upper()
print('Jokenpoooo...')
sleep(2)
#JOGADOR GANHANDO
if jogador == 'PEDRA' and escolha_pc == 'TESOURA':
    print('Jogador Ganhou')
elif jogador == 'TESOURA' and escolha_pc == 'PAPEL':
    print('Jogador Ganhou')
elif jogador == 'PAPEL' and escolha_pc == 'PEDRA':
    print('Jogador Ganhou !!')
#MAQUINA GANHANDO
elif escolha_pc == 'PEDRA' and jogador == 'TESOURA':
        print('Maquina Ganhou')
elif escolha_pc == 'TESOURA' and jogador == 'PAPEL':
        print('Maquina Ganhou')
elif escolha_pc == 'PAPEL' and jogador == 'PEDRA':
        print('Maquina Ganhou !!')
#EMPATE
else:
    print('Empate !!')
print(f'Maquina = {escolha_pc}, Jogador = {jogador}')

