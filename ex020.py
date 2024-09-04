#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
al1 = str(input('Aluno 1: '))
al2 = str(input('Aluno 2: '))
al3 = str(input('Aluno 3: '))
al4 = str(input('Aluno 4: '))

lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A ordem sorteada foi', lista)


















import random
al1 = str(input('Aluno1: '))
al2 = str(input('Aluno2: '))
al3 = str(input('Aluno3: '))
al4 = str(input('Aluno4: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(f'A ordem sorteada será: {lista}')