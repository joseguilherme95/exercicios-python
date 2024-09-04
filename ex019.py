#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajdue
# ele, lendo o nome deles e escrevendo o nome escolhido.

import random

al1 = str(input('Insira o 1ª Aluno: '))
al2 = str(input('Insira o 2ª Aluno: '))
al3 = str(input('Insira o 3ª Aluno: '))
al4 = str(input('Insira o 4ª Aluno: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')








































#import random
#al1 = str(input('Nome do primeiro aluno: '))
#al2 = str(input('Nome do segundo aluno: '))
#al3 = str(input('Nome do terceiro Aluno: '))
#al4 = str(input('Nome do quarto Aluno: '))
#lista = [al1, al2, al3, al4]
#escolhido = random.choice(lista)
#print(f'O escolhido para apagar o quadro é: {escolhido}'#)