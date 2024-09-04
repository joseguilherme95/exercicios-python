#   Refaça o desafio 051, lendo o primeiro termo e a razão de uma P.A, mostrando os 10 primeiros termos
#   da progressão usando a estrutura while.



print('''   Gerador de P.A  ''')
print('=' * 20)

p1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
termo = p1
cont = 0

while cont < 10:
    print(termo)
    termo += r
    cont += 1